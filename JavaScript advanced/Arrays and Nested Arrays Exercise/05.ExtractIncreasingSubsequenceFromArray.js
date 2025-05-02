function extractNonDecreasingSubset(arr) {
    let result = [];
    let currentMax = arr[0];

    for (let num of arr) {
        if (num >= currentMax) {
            result.push(num);
            currentMax = num;
        }
    }

    return result;
}

