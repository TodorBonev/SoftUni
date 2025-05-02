function solve() {
    const [name, hall, price] = [...document.querySelectorAll('#container input')];
    const btnOnScreen = document.querySelector('#container button');
    const ulMoviesElement = document.querySelector('#movies > ul');
    const ulArchiveElement = document.querySelector('#archive > ul');
    const buttonClearElement = document.querySelector('#archive > button');

    btnOnScreen.addEventListener('click', (e) => {
        e.preventDefault();
        if (!name.value || !hall.value || !price.value || isNaN(price.value)) return;

        const liElement = document.createElement('li');
        liElement.innerHTML = `
            <span>${name.value}</span>
            <strong>Hall: ${hall.value}</strong>
            <div>
                <strong>${Number(price.value).toFixed(2)}</strong>
                <input placeholder="Tickets Sold">
                <button>Archive</button>
            </div>
        `;

        ulMoviesElement.appendChild(liElement);
        [name.value, hall.value, price.value] = ["", "", ""];

        const archiveBtn = liElement.querySelector('button');
        archiveBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const ticketCount = liElement.querySelector('input').value;
            if (!ticketCount || isNaN(ticketCount)) return;

            const totalAmount = (Number(ticketCount) * Number(liElement.querySelector('div > strong').textContent)).toFixed(2);
            const liArchiveElement = document.createElement('li');
            liArchiveElement.innerHTML = `
                <span>${liElement.querySelector('span').textContent}</span>
                <strong>Total amount: ${totalAmount}</strong>
                <button>Delete</button>
            `;

            ulArchiveElement.appendChild(liArchiveElement);
            liElement.remove();

            liArchiveElement.querySelector('button').addEventListener('click', () => liArchiveElement.remove());
        });
    });

    buttonClearElement.addEventListener('click', (e) => {
        e.preventDefault();
        ulArchiveElement.innerHTML = "";
    });
}
