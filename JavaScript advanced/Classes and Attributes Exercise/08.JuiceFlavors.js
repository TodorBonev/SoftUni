function juiceProcessing(input) {
    let juices = new Map();
    let bottles = new Map();

    input.forEach(line => {
        let [juice, quantity] = line.split(" => ");
        quantity = Number(quantity);

        juices.set(juice, (juices.get(juice) || 0) + quantity);

        let bottleCount = Math.floor(juices.get(juice) / 1000);
        if (bottleCount > 0) {
            bottles.set(juice, (bottles.get(juice) || 0) + bottleCount);
            juices.set(juice, juices.get(juice) % 1000);
        }
    });

    return Array.from(bottles).map(([juice, count]) => `${juice} => ${count}`).join("\n");
}


