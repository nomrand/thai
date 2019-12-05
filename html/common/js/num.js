function flr(num, digit) {
    if (num == null) {
        return null;
    }
    let d = Math.pow(10, digit);
    return Math.floor(num * d) / d;
}