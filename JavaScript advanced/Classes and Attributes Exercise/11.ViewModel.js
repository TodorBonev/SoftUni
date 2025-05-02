class Textbox {
    constructor(selector, invalidSymbols) {
        this._elements = document.querySelectorAll(selector);
        this._invalidSymbols = invalidSymbols;
        this._value = this._elements.length > 0 ? this._elements[0].value : "";

        this._elements.forEach(el => el.addEventListener("input", (e) => this.value = e.target.value));
    }

    get value() {
        return this._value;
    }

    set value(newValue) {
        this._value = newValue;
        this._elements.forEach(el => el.value = newValue);
    }

    get elements() {
        return this._elements;
    }

    isValid() {
        return !this._invalidSymbols.test(this._value);
    }
}

