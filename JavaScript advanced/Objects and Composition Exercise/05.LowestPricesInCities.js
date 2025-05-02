function findLowestPrices(data) {
    let products = {};

    for (let entry of data) {
        let [town, product, price] = entry.split(" | ");
        price = Number(price);

        if (!products[product] || products[product].price > price) {
            products[product] = { price, town };
        }
    }

    for (let product in products) {
        console.log(`${product} -> ${products[product].price} (${products[product].town})`);
    }
}
