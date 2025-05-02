function createHeroRegister(heroArray) {
    let heroes = heroArray
        .filter(hero => hero.trim() !== "")
        .map(hero => {
            let [name, level, items] = hero.split(" / ");
            return {
                name: name,
                level: Number(level),
                items: items ? items.split(", ").map(item => item.trim()) : []
            };
        });

    console.log(JSON.stringify(heroes));
}


