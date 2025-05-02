function sortStringsByCriteria(strings) {
    strings.sort((a, b) => a.length - b.length || a.localeCompare(b, undefined, { sensitivity: 'base' }));
    strings.forEach(str => console.log(str));
}

