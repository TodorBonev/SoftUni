class Contact {
    constructor(firstName, lastName, phone, email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.phone = phone;
        this.email = email;
        this.online = false;
        this._element = null;
    }

    get online() {
        return this._online;
    }

    set online(value) {
        this._online = value;
        if (this._element) {
            this._element.querySelector(".title").classList.toggle("online", value);
        }
    }

    render(id) {
        const container = document.getElementById(id);

        const article = document.createElement("article");

        const titleDiv = document.createElement("div");
        titleDiv.className = "title";
        titleDiv.textContent = `${this.firstName} ${this.lastName}`;

        const toggleButton = document.createElement("button");
        toggleButton.innerHTML = "&#8505;";
        toggleButton.addEventListener("click", () => infoDiv.style.display = infoDiv.style.display === "none" ? "block" : "none");
        
        titleDiv.appendChild(toggleButton);

        const infoDiv = document.createElement("div");
        infoDiv.className = "info";
        infoDiv.style.display = "none";

        const phoneSpan = document.createElement("span");
        phoneSpan.innerHTML = `&#9742; ${this.phone}`;

        const emailSpan = document.createElement("span");
        emailSpan.innerHTML = `&#9993; ${this.email}`;

        infoDiv.appendChild(phoneSpan);
        infoDiv.appendChild(emailSpan);

        article.appendChild(titleDiv);
        article.appendChild(infoDiv);

        container.appendChild(article);

        this._element = article;
        this.online = this._online;
    }
}


