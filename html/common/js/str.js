function pad0(digit, num) {
    for (let i = 0; num.length < digit; i++) {
        num = "0" + num;
    }
    return num;
}

function getUrlParam() {
    let ret = {};
    let paramsArr = window.location.search.substring(1).split('&');
    paramsArr.forEach(function (keyval) {
        ret[keyval.split('=')[0]] = keyval.split('=')[1];
    });
    return ret;
};