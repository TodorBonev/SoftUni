function solve() {
    document.querySelector('#searchBtn').addEventListener('click', onClick);

    function onClick() {
        let searchElement = document.getElementById('searchField');
        let rowElements = document.querySelectorAll('.container tbody tr');
        let searchText = searchElement.value.trim().toLowerCase();

        rowElements.forEach(row => row.classList.remove('select'));

        rowElements.forEach(row => {
            if ([...row.children].some(td => td.textContent.toLowerCase().includes(searchText))) {
                row.classList.add('select');
            }
        });

        searchElement.value = '';
    }
}
