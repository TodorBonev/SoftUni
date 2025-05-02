function formatText() {

    const inputText = document.getElementById("input").value;
    
    let sentences = inputText.split('.')

      .filter(sentence => sentence.trim().length > 0)
      .map(sentence => sentence.trim() + '.');
    
    const outputDiv = document.getElementById("output");
    
    outputDiv.innerHTML = '';
    
    for (let i = 0; i < sentences.length; i += 3) {

      const paragraphSentences = sentences.slice(i, i + 3);
      const paragraphText = paragraphSentences.join('');
      const paragraph = `<p>${paragraphText}</p>`;
      
      outputDiv.innerHTML += paragraph;
    }
  }