function isMagicalMatrix(matrix) {
    let targetSum = matrix[0].reduce((sum, num) => sum + num, 0);

    for (let row of matrix) {
        let rowSum = row.reduce((sum, num) => sum + num, 0);
        if (rowSum !== targetSum) return false;
    }

    for (let col = 0; col < matrix[0].length; col++) {
        let colSum = 0;
        for (let row = 0; row < matrix.length; row++) {
            colSum += matrix[row][col];
        }
        if (colSum !== targetSum) return false;
    }

    return true;
}
