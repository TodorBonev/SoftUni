function test(input, sort) {
    return input.map(row => new (class Ticket {
        constructor(destination, price, status) {
            Object.assign(this, { destination, price: Number(price), status });
        }
    })(...row.split('|')))
    .sort((a, b) => sort === "price" ? a.price - b.price : a[sort].localeCompare(b[sort]));
}


