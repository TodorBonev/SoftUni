function getArticleGenerator(articles) {
    return function () {
        if (articles.length === 0) return;

        const contentDiv = document.getElementById("content");
        const articleElement = document.createElement("article");
        articleElement.textContent = articles.shift();
        contentDiv.appendChild(articleElement);
    };
}
