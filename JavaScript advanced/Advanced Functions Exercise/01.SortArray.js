function sortArray(array, order) {
    return order === 'asc' ? array.sort((a, b) => a - b) : array.sort((a, b) => b - a);
}

