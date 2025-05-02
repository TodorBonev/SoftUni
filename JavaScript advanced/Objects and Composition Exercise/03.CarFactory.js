function assembleCar(order) {
    const engines = [
        { power: 90, volume: 1800 },
        { power: 120, volume: 2400 },
        { power: 200, volume: 3500 }
    ];
    
    const carriages = {
        hatchback: (color) => ({ type: 'hatchback', color }),
        coupe: (color) => ({ type: 'coupe', color })
    };

    let engine = engines.find(e => e.power >= order.power);

    let wheelsize = order.wheelsize % 2 === 0 ? order.wheelsize - 1 : order.wheelsize;
    let wheels = Array(4).fill(wheelsize);

    return {
        model: order.model,
        engine: engine,
        carriage: carriages[order.carriage](order.color),
        wheels: wheels
    };
}

