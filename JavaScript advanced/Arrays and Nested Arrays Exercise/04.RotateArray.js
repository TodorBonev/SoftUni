function rotateArray(arr, rotations) {
    rotations = rotations % arr.length;
    for (let i = 0; i < rotations; i++) {
        arr.unshift(arr.pop());
    }
    console.log(arr.join(' '));
}

