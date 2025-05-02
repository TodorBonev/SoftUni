function sortedCatalog(products) {
    let catalog = {};

    products.forEach(product => {
        let [name, price] = product.split(" : ");
        let initial = name[0];

        if (!catalog[initial]) {
            catalog[initial] = [];
        }

        catalog[initial].push({ name, price: Number(price) });
    });

    let sortedKeys = Object.keys(catalog).sort();
    
    sortedKeys.forEach(initial => {
        console.log(initial);
        catalog[initial]
            .sort((a, b) => a.name.localeCompare(b.name))
            .forEach(product => console.log(`  ${product.name}: ${product.price}`));
    });
}
