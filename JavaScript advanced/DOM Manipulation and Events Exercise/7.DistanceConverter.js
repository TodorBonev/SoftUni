function attachEventsListeners() {
    const conversionRates = { km: 1000, m: 1, cm: 0.01, mm: 0.001, mi: 1609.34, yrd: 0.9144, ft: 0.3048, in: 0.0254 };
    
    document.querySelector('#convert').addEventListener('click', () => {
        const from = document.querySelector('#inputUnits').value;
        const to = document.querySelector('#outputUnits').value;
        const value = Number(document.querySelector('#inputDistance').value) * conversionRates[from] / conversionRates[to];

        document.querySelector('#outputDistance').value = value;
    });
}

