class Company {
    #departments = {};

    addEmployee(username, salary, position, department) {
        if (!username || !position || !department || !salary || salary < 0) throw new Error("Invalid input!");

        (this.#departments[department] ||= []).push({ username, salary: Number(salary), position });
        return `New employee is hired. Name: ${username}. Position: ${position}`;
    }

    bestDepartment() {
        let [bestDept, maxSalary] = Object.entries(this.#departments)
            .map(([dept, employees]) => [dept, employees.reduce((sum, e) => sum + e.salary, 0) / employees.length])
            .reduce((best, current) => current[1] > best[1] ? current : best, ["", 0]);

        return `Best Department is: ${bestDept}
Average salary: ${maxSalary.toFixed(2)}
${this.#departments[bestDept]
    .sort((a, b) => b.salary - a.salary || a.username.localeCompare(b.username))
    .map(e => `${e.username} ${e.salary} ${e.position}`)
    .join("\n")}`;
    }
}

