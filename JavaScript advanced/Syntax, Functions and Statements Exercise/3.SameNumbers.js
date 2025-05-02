function checkDigits(num) {
    let numStr = num.toString();
    let allSame = numStr.split('').every(digit => digit === numStr[0]);
    let sumDigits = numStr.split('').reduce((sum, digit) => sum + Number(digit), 0);

    console.log(allSame);
    console.log(sumDigits);
}