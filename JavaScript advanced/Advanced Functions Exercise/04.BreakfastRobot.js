function solution() {
    const stock = { protein: 0, carbohydrate: 0, fat: 0, flavour: 0 };

    const recipes = {
        apple: { carbohydrate: 1, flavour: 2 },
        lemonade: { carbohydrate: 10, flavour: 20 },
        burger: { carbohydrate: 5, fat: 7, flavour: 3 },
        eggs: { protein: 5, fat: 1, flavour: 1 },
        turkey: { protein: 10, carbohydrate: 10, fat: 10, flavour: 10 }
    };

    return function manager(command) {
        const [action, item, quantity] = command.split(" ");

        if (action === "restock") {
            stock[item] += Number(quantity);
            return "Success";
        }

        if (action === "prepare") {
            const required = Object.entries(recipes[item]).map(([ingredient, amount]) => [ingredient, amount * quantity]);

            for (const [ingredient, amount] of required) {
                if (stock[ingredient] < amount) {
                    return `Error: not enough ${ingredient} in stock`;
                }
            }

            required.forEach(([ingredient, amount]) => stock[ingredient] -= amount);
            return "Success";
        }

        if (action === "report") {
            return `protein=${stock.protein} carbohydrate=${stock.carbohydrate} fat=${stock.fat} flavour=${stock.flavour}`;
        }
    };
}
