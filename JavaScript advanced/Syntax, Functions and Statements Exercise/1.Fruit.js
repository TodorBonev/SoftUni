function calculateFruitCost(fruit, weightInGrams, pricePerKg) {
    let weightInKg = weightInGrams / 1000;
    let totalCost = weightInKg * pricePerKg;

    console.log(`I need $${totalCost.toFixed(2)} to buy ${weightInKg.toFixed(2)} kilograms ${fruit}.`);
}