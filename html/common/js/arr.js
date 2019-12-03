function compressarr(arr, maxlen) {
    if (arr.length <= maxlen) {
        return arr;
    }

    let step = arr.length / maxlen;
    let result = [];
    for (let i = 0; parseInt(i + step, 10) < arr.length; i += step) {
        let num = 0;
        let temp = [];
        for (let key in arr[0]) {
            temp[key] = 0;
        }
        for (let j = parseInt(i, 10); j < parseInt(i + step, 10); j++) {
            num++;
            for (let key in arr[0]) {
                temp[key] += arr[j][key];
            }
        }
        if (num > 1) {
            for (let key in arr[0]) {
                temp[key] /= num;
            }
        }
        result.push(temp);
    }
    return result;
}
