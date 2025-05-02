function carRegister(input) {
    let carData = new Map();

    input.forEach(line => {
        let [brand, model, quantity] = line.split(" | ");
        quantity = Number(quantity);

        if (!carData.has(brand)) {
            carData.set(brand, new Map());
        }

        let models = carData.get(brand);
        models.set(model, (models.get(model) || 0) + quantity);
    });

    return Array.from(carData)
        .map(([brand, models]) => `${brand}\n${Array.from(models)
            .map(([model, quantity]) => `###${model} -> ${quantity}`)
            .join("\n")}`)
        .join("\n");
}


