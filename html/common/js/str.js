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

function separateWords(str, sep, maxCharNum) {
    let ret = [];
    if (!str) {
        return ret;
    }

    let oneLine = "";
    for (key in str.split(sep)) {
        let word = str.split(sep)[key];
        while (word.length > 0) {
            if (oneLine.length + sep.length + word.length > maxCharNum) {
                if (oneLine.length == 0) {
                    ret.push(word.substring(0, maxCharNum));
                    word = word.substring(maxCharNum);
                } else {
                    ret.push(oneLine);
                }
                oneLine = "";
            } else {
                oneLine += sep + word;
                word = "";
            }
        }
    }

    return ret;
}