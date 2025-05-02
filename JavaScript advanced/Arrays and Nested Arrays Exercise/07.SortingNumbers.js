function specialSort(arr) {
    let sortedArr = arr.slice().sort((a, b) => a - b);
    let result = [];
    
    while (sortedArr.length > 0) {
        result.push(sortedArr.shift());
        if (sortedArr.length > 0) {
            result.push(sortedArr.pop());
        }
    }

    return result;
}

