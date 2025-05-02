function generateReport() {
    const inputElements = Array.from(document.querySelectorAll('input[type="checkbox"]'));
    const checkedCols = inputElements
        .map((input, index) => input.checked ? index : -1)
        .filter(index => index !== -1);

    const rows = Array.from(document.querySelectorAll('tbody tr'));
    const resultArr = [];

    for (const row of rows) {
        const cells = Array.from(row.children);
        const obj = {};

        for (const colIndex of checkedCols) {
            const key = inputElements[colIndex].name;
            const value = cells[colIndex]?.textContent?.trim() || "";
            obj[key] = value;
        }

        resultArr.push(obj);
    }

    document.getElementById('output').value = JSON.stringify(resultArr, null, 2);
}

