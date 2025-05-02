function solve() {
    const table = document.querySelector('table');
    const checkParagraph = document.querySelector('#check p');
    const buttons = document.querySelectorAll('button');

    const checkBtn = buttons[0];
    const clearBtn = buttons[1];

    checkBtn.addEventListener('click', () => {
        const inputs = [...document.querySelectorAll('input')];

        if (inputs.some(input => !input.value || isNaN(input.value) || input.value < 1 || input.value > 3)) {
            return updateResult(false);
        }

        const rowsValid = validateRows(inputs);
        const colsValid = validateColumns(inputs);

        updateResult(rowsValid && colsValid);
    });

    clearBtn.addEventListener('click', () => {
        document.querySelectorAll('input').forEach(input => input.value = '');
        table.style.border = '';
        checkParagraph.textContent = '';
    });

    function updateResult(isSolved) {
        table.style.border = `2px solid ${isSolved ? 'green' : 'red'}`;
        checkParagraph.textContent = isSolved ? 'You solve it! Congratulations!' : 'NOP! You are not done yet...';
        checkParagraph.style.color = isSolved ? 'green' : 'red';
    }

    function validateRows(inputs) {
        for (let i = 0; i < inputs.length; i += 3) {
            if (new Set(inputs.slice(i, i + 3).map(input => input.value)).size !== 3) {
                return false;
            }
        }
        return true;
    }

    function validateColumns(inputs) {
        for (let i = 0; i < 3; i++) {
            if (new Set([inputs[i].value, inputs[i + 3].value, inputs[i + 6].value]).size !== 3) {
                return false;
            }
        }
        return true;
    }
}

