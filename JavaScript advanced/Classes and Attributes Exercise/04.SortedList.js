class List {
    constructor() {
        this.data = [];
        this.size = 0;
    }

    add(element) {
        this.data.push(element);
        this.data.sort((a, b) => a - b);
        this.size = this.data.length;
    }

    remove(index) {
        if (index >= 0 && index < this.data.length) {
            this.data.splice(index, 1);
            this.size = this.data.length;
        }
    }

    get(index) {
        return index >= 0 && index < this.data.length ? this.data[index] : undefined;
    }
}

