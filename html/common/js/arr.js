function avgarr(arr) {
    if (arr.length == 1) {
        return arr[0];
    }

    let result = {};
    let len_per_key = {};
    for (i in arr) {
        for (let key in arr[i]) {
            if (arr[i][key] == null) {
                continue;
            }
            if (result[key] == null) {
                result[key] = 0;
                len_per_key[key] = 0;
            }
            result[key] += arr[i][key];
            len_per_key[key]++;
        }
    }

    for (let key in result) {
        result[key] /= len_per_key[key];
    }
    return result;
}

function compressarr(arr, maxlen) {
    if (arr.length <= maxlen) {
        return arr;
    }

    let step = arr.length / maxlen;
    let result = [];
    for (let i = 0; parseInt(i + step, 10) < arr.length; i += step) {
        let start = parseInt(i, 10);
        let end = parseInt(i + step, 10);
        result.push(avgarr(arr.slice(start, end)));
    }
    return result;
}


function monthlyarr(arr) {
    let result = [[], [], [], [], [], [], [], [], [], [], [], [],];
    for (i in arr) {
        let d = new Date();
        d.setTime(arr[i].date * 1000);

        result[d.getMonth()].push(arr[i]);
    }
    return result;
}

function dayflatarr(arr) {
    let result = [];
    for (i in arr) {
        let d = new Date();
        d.setTime(arr[i].date * 1000);
        d.setFullYear(1900, 0, 1);

        let arrcopy = Object.create(arr[i]);
        arrcopy.date = d.getTime() / 1000;
        result.push(arrcopy);
    }
    result.sort(function (a, b) {
        return a.date - b.date;
    });
    return result;
}

function timeslicearr(arr, start, end) {
    let s = 0;
    let e = arr.length - 1;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i].date >= start) {
            s = i;
            break;
        }
    }
    for (let i = arr.length - 1; i >= 0; i--) {
        if (arr[i].date <= end) {
            e = i + 1;
            break;
        }
    }

    return arr.slice(s, e);
}
