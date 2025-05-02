function processOperations(start, ...operations) {
    let number = Number(start);

    const operationsMap = {
        chop: n => n / 2,
        dice: n => Math.sqrt(n),
        spice: n => n + 1,
        bake: n => n * 3,
        fillet: n => n * 0.8
    };

    operations.forEach(operation => {
        number = operationsMap[operation](number);
        console.log(number);
    });
}


