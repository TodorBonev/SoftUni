function solve() {
    document.querySelector('#btnSend').addEventListener('click', onClick);
    
    function onClick() {

       const inputTextarea = document.querySelector('textarea');
       const bestRestaurantOutput = document.querySelector('#bestRestaurant p');
       const bestWorkersOutput = document.querySelector('#workers p');
       
       try {
          const restaurants = processRestaurants(JSON.parse(inputTextarea.value));
          const bestRestaurant = findBestRestaurant(restaurants);
          
          if (bestRestaurant) {
             displayResults(bestRestaurant, bestRestaurantOutput, bestWorkersOutput);
          } else {
             bestRestaurantOutput.textContent = "No valid restaurant data found.";
             bestWorkersOutput.textContent = "";
          }
       } catch (error) {
          bestRestaurantOutput.textContent = `Error: ${error.message}`;
          bestWorkersOutput.textContent = "";
          console.error(error);
       }
    }
    
    function processRestaurants(input) {
       const restaurants = new Map();
       
       input.forEach(line => {

          const parts = line.match(/[^-,\s]+/g) || [];
          if (parts.length < 2) return;
          
          const restaurantName = parts[0];
          const workerData = parts.slice(1);
          

          const workers = [];
          const salaries = [];
          
          for (let i = 0; i < workerData.length; i += 2) {
             const worker = workerData[i];
             const salary = parseFloat(workerData[i + 1]);
             
             if (worker && !isNaN(salary)) {
                workers.push(worker);
                salaries.push(salary);
             }
          }
          
          if (workers.length === 0) return;
          

          if (restaurants.has(restaurantName)) {
             const restaurant = restaurants.get(restaurantName);
             restaurant.workers.push(...workers);
             restaurant.salaries.push(...salaries);
             restaurant.averageSalary = calcAverageSalary(restaurant.salaries);
             restaurant.highestSalary = Math.max(...restaurant.salaries);
          } else {
             restaurants.set(restaurantName, {
                name: restaurantName,
                workers,
                salaries,
                averageSalary: calcAverageSalary(salaries),
                highestSalary: Math.max(...salaries)
             });
          }
       });
       
       return restaurants;
    }
    
    function findBestRestaurant(restaurants) {
       if (restaurants.size === 0) return null;
       
       let bestRestaurant = null;
       let highestAvgSalary = -1;
       
       for (const restaurant of restaurants.values()) {
          if (restaurant.averageSalary > highestAvgSalary) {
             highestAvgSalary = restaurant.averageSalary;
             bestRestaurant = restaurant;
          }
       }
       
       return bestRestaurant;
    }
    
    function calcAverageSalary(salaries) {
       if (salaries.length === 0) return 0;
       return salaries.reduce((sum, salary) => sum + salary, 0) / salaries.length;
    }
    
    function displayResults(restaurant, restaurantOutput, workersOutput) {

       const sortedWorkers = restaurant.workers
          .map((worker, i) => ({ name: worker, salary: restaurant.salaries[i] }))
          .sort((a, b) => b.salary - a.salary);
       

       restaurantOutput.textContent = `Name: ${restaurant.name} Average Salary: ${restaurant.averageSalary.toFixed(2)} Best Salary: ${restaurant.highestSalary.toFixed(2)}`;
       

       workersOutput.textContent = sortedWorkers
          .map(worker => `Name: ${worker.name} With Salary: ${worker.salary}`)
          .join(' ');
    }
 }
