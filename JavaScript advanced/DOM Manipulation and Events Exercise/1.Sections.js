function createContent(strings) {
    const content = document.getElementById("content");

    strings.forEach(text => {

        let div = document.createElement("div");

        let p = document.createElement("p");
        p.textContent = text;
        p.style.display = "none";

        div.addEventListener("click", () => {
            p.style.display = "block";
        });

        div.appendChild(p);
        content.appendChild(div);
    });
}
