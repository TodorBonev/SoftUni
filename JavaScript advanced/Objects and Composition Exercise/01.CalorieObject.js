function composeFoodObject(foodArray) {
    let foodObject = {};

    for (let i = 0; i < foodArray.length; i += 2) {
        foodObject[foodArray[i]] = Number(foodArray[i + 1]);
    }

    console.log(foodObject);
}

