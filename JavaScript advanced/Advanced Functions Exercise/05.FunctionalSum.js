function add(num) {
    let sum = num;

    function inner(nextNum) {
        sum += nextNum;
        return inner;
    }

    inner.toString = () => sum;
    return inner;
}
