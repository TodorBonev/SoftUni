function search() {

    const searchText = document.getElementById('searchText').value.toLowerCase();
    

    const townsList = document.getElementById('towns').children;
    
    for (let i = 0; i < townsList.length; i++) {
      townsList[i].style.fontWeight = 'normal';
      townsList[i].style.textDecoration = 'none';
    }
    
    if (!searchText) {
      document.getElementById('result').textContent = '0 matches found';
      return;
    }
    
    let matches = 0;
    
    for (let i = 0; i < townsList.length; i++) {
      const townName = townsList[i].textContent.toLowerCase();
      
      if (townName.includes(searchText)) {

        townsList[i].style.fontWeight = 'bold';
        townsList[i].style.textDecoration = 'underline';
        matches++;
      }
    }
    
    document.getElementById('result').textContent = `${matches} matches found`;
  }
