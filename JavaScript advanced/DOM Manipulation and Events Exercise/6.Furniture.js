function solve() {
    const [inputArea, outputArea] = document.querySelectorAll('textarea');
    const tbody = document.querySelector('tbody');
  
    document.querySelectorAll('button').forEach(btn => btn.addEventListener('click', ({ target }) => {
      if (!inputArea.value) return;
  
      if (target.textContent === 'Generate') {
        JSON.parse(inputArea.value).forEach(({ img, name, price, decFactor }) => {
          tbody.innerHTML += `<tr>
            <td><img src="${img}"></td>
            <td><p>${name}</p></td>
            <td><p>${price}</p></td>
            <td><p>${decFactor}</p></td>
            <td><input type="checkbox"></td>
          </tr>`;
        });
      } else {
        const selected = [...document.querySelectorAll('input:checked')].map(input => input.closest('tr').children);
        const names = selected.map(row => row[1].textContent);
        const totalPrice = selected.reduce((sum, row) => sum + Number(row[2].textContent), 0);
        const avgDecFactor = selected.reduce((sum, row) => sum + Number(row[3].textContent), 0) / names.length || 0;
  
        outputArea.textContent = `Bought furniture: ${names.join(', ')}\nTotal price: ${totalPrice.toFixed(2)}\nAverage decoration factor: ${avgDecFactor}`;
      }
    }));
  }
  
