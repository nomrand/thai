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
    if (oneLine.length > 0) {
        ret.push(oneLine);
    }

    return ret;
}

function formatDate(date, format) {
    if (!format) format = 'YYYY-MM-DD hh:mm:ss.SSS';
    format = format.replace(/YYYY/g, date.getFullYear());
    format = format.replace(/MM/g, ('0' + (date.getMonth() + 1)).slice(-2));
    format = format.replace(/DD/g, ('0' + date.getDate()).slice(-2));
    format = format.replace(/hh/g, ('0' + date.getHours()).slice(-2));
    format = format.replace(/mm/g, ('0' + date.getMinutes()).slice(-2));
    format = format.replace(/ss/g, ('0' + date.getSeconds()).slice(-2));
    if (format.match(/S/g)) {
        var milliSeconds = ('00' + date.getMilliseconds()).slice(-3);
        var length = format.match(/S/g).length;
        for (var i = 0; i < length; i++) format = format.replace(/S/, milliSeconds.substring(i, i + 1));
    }
    return format;
};

function monthStr(mon) {
    var month = new Array();
    month[0] = "January";
    month[1] = "February";
    month[2] = "March";
    month[3] = "April";
    month[4] = "May";
    month[5] = "June";
    month[6] = "July";
    month[7] = "August";
    month[8] = "September";
    month[9] = "October";
    month[10] = "November";
    month[11] = "December";
    return month[mon];
};