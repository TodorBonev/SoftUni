function argumentInfo(...args) {
    const typeCounts = {};

    args.forEach(arg => {
        const type = typeof arg;
        console.log(`${type}: ${arg}`);

        typeCounts[type] = (typeCounts[type] || 0) + 1;
    });

    Object.entries(typeCounts)
        .sort((a, b) => b[1] - a[1])
        .forEach(([type, count]) => console.log(`${type} = ${count}`));
}

