function checkDistance(x1, y1, x2, y2) {
    const isValid = (x1, y1, x2, y2) => Number.isInteger(Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2));

    console.log(`{${x1}, ${y1}} to {0, 0} is ${isValid(x1, y1, 0, 0) ? "valid" : "invalid"}`);
    console.log(`{${x2}, ${y2}} to {0, 0} is ${isValid(x2, y2, 0, 0) ? "valid" : "invalid"}`);
    console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is ${isValid(x1, y1, x2, y2) ? "valid" : "invalid"}`);
}


