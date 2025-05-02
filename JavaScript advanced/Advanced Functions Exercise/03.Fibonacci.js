function getFibonator() {
    let [prev, current] = [0, 1];

    return function () {
        let next = prev + current;
        prev = current;
        current = next;
        return prev;
    };
}
