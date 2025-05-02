function getTimeToUniversity(steps, stepLength, speed) {
    let distanceMeters = steps * stepLength;
    let speedMetersPerSecond = (speed * 1000) / 3600;
    let timeSeconds = Math.round(distanceMeters / speedMetersPerSecond);

    let restMinutes = Math.floor(distanceMeters / 500);
    let totalTimeSeconds = timeSeconds + restMinutes * 60;

    let hours = Math.floor(totalTimeSeconds / 3600);
    let minutes = Math.floor((totalTimeSeconds % 3600) / 60);
    let seconds = totalTimeSeconds % 60;

    console.log(`${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`);
}


