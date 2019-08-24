function pad0(digit, num) {
    for (let i = 0; num.length < digit; i++) {
        num = "0" + num;
    }
    return num;
}