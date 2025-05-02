(() => {
    String.prototype.ensureStart = function (str) {
        return this.startsWith(str) ? this.toString() : str + this;
    };

    String.prototype.ensureEnd = function (str) {
        return this.endsWith(str) ? this.toString() : this + str;
    };

    String.prototype.isEmpty = function () {
        return !this.length;
    };

    String.prototype.truncate = function (n) {
        if (this.length <= n) return this.toString();
        return n < 4 ? '.'.repeat(n) : this.includes(' ') 
            ? this.slice(0, this.lastIndexOf(' ', n - 3)) + '...' 
            : this.slice(0, n - 3) + '...';
    };

    String.format = (string, ...params) => string.replace(/{(\d+)}/g, (_, index) => params[index] ?? `{${index}}`);
})();


