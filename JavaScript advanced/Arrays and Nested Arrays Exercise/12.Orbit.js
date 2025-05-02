function generateOrbits([width, height, x, y]) {
    let matrix = Array.from({ length: height }, () => Array(width).fill(0));

    for (let row = 0; row < height; row++) {
        for (let col = 0; col < width; col++) {
            matrix[row][col] = Math.max(Math.abs(row - x), Math.abs(col - y)) + 1;
        }
    }

    matrix.forEach(row => console.log(row.join(' ')));
}
