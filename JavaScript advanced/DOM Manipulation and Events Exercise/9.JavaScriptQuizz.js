function quizGame() {
    const sections = document.querySelectorAll("section");
    const results = document.querySelector("#results h1");
    const correctAnswers = ["onclick", "JSON.stringify()", "A programming API for HTML and XML documents"];
    let currentSection = 0;
    let rightAnswers = 0;

    document.querySelectorAll("ul li").forEach(li => {
        li.addEventListener("click", (event) => {
            if (correctAnswers[currentSection] === event.target.textContent) {
                rightAnswers++;
            }

            sections[currentSection].style.display = "none";
            currentSection++;

            if (currentSection < sections.length) {
                sections[currentSection].style.display = "block";
            } else {
                document.querySelector("#results").style.display = "block";
                results.textContent = rightAnswers === correctAnswers.length ? 
                    "You are recognized as top JavaScript fan!" : 
                    `You have ${rightAnswers} right answers`;
            }
        });
    });
}
