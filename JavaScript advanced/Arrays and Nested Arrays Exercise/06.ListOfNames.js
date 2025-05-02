function sortAndNumberNames(names) {
    names.sort((a, b) => a.localeCompare(b));
    names.forEach((name, index) => console.log(`${index + 1}.${name}`));
}




