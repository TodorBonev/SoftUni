function result() {
    let text = document.getElementById("text").value;
    let caseType = document.getElementById("naming-convention").value;
    let resultSpan = document.getElementById("result"); 

    if (caseType !== "Camel Case" && caseType !== "Pascal Case") {
        resultSpan.textContent = "Error!";
        return;
    }

    let words = text.toLowerCase().split(" ");
    let transformedText = words.map((word, index) => {
        let capitalizedWord = word.charAt(0).toUpperCase() + word.slice(1);
        return (caseType === "Camel Case" && index === 0) ? word : capitalizedWord;
    }).join("");

    resultSpan.textContent = transformedText;
}

