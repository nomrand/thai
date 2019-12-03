function flr(num, digit) {
    let d = Math.pow(10, digit);
    return Math.floor(num * d) / d;
}