function diagonalSumMatrix(input) {

    const matrix = input.map(row => row.split(' ').map(Number));
    const size = matrix.length;
    
    let mainDiagonalSum = 0;
    for (let i = 0; i < size; i++) {
      mainDiagonalSum += matrix[i][i];
    }
    
    let secondaryDiagonalSum = 0;
    for (let i = 0; i < size; i++) {
      secondaryDiagonalSum += matrix[i][size - 1 - i];
    }
    
    if (mainDiagonalSum !== secondaryDiagonalSum) {
      return matrix.map(row => row.join(' ')).join('\n');
    }
    
    const result = [];
    for (let i = 0; i < size; i++) {
      const newRow = [];
      for (let j = 0; j < matrix[i].length; j++) {
        if (i === j || i === size - 1 - j) {
          newRow.push(matrix[i][j]);
        } else {
          newRow.push(mainDiagonalSum);
        }
      }
      result.push(newRow.join(' '));
    }
    
    return result.join('\n');
  }
  