function attachEventsListeners() {
    const timeUnits = {
        days: { hours: 24, minutes: 1440, seconds: 86400 },
        hours: { days: 1 / 24, minutes: 60, seconds: 3600 },
        minutes: { days: 1 / 1440, hours: 1 / 60, seconds: 60 },
        seconds: { days: 1 / 86400, hours: 1 / 3600, minutes: 1 / 60 }
    };

    Object.keys(timeUnits).forEach(unit => {
        document.getElementById(`${unit}Btn`).addEventListener("click", () => {
            const value = Number(document.getElementById(unit).value);
            if (!isNaN(value)) {
                Object.keys(timeUnits[unit]).forEach(targetUnit => {
                    document.getElementById(targetUnit).value = value * timeUnits[unit][targetUnit];
                });
            }
        });
    });
}

