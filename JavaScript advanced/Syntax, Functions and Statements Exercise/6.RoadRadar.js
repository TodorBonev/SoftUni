function checkSpeedLimit(speed, area) {
    const speedLimits = {
        motorway: 130,
        interstate: 90,
        city: 50,
        residential: 20
    };

    let limit = speedLimits[area];

    if (speed <= limit) {
        console.log(`Driving ${speed} km/h in a ${limit} zone`);
    } else {
        let difference = speed - limit;
        let status = difference <= 20 ? "speeding"
                    : difference <= 40 ? "excessive speeding"
                    : "reckless driving";
        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${limit} - ${status}`);
    }
}


