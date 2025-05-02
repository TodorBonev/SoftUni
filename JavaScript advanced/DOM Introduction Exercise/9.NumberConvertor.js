function solve() {
    const menu = document.getElementById("selectMenuTo");

    const options = [
        { value: "binary", text: "Binary" },
        { value: "hexadecimal", text: "Hexadecimal" }
    ];

    options.forEach(opt => {
        const optionElement = document.createElement("option");
        optionElement.value = opt.value;
        optionElement.textContent = opt.text;
        menu.appendChild(optionElement);
    });

    document.querySelector("button").addEventListener("click", () => {
        const numberInput = document.getElementById("input").value;
        const convertTo = menu.value;
        const resultField = document.getElementById("result");

        if (!numberInput || isNaN(numberInput)) return;

        const number = Number(numberInput);
        let result = "";

        switch (convertTo) {
            case "binary":
                result = number.toString(2);
                break;
            case "hexadecimal":
                result = number.toString(16).toUpperCase();
                break;
        }

        resultField.value = result;
    });
}

