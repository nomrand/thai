function compressarr(arr, maxlen) {
    if (arr.length <= maxlen) {
        return arr;
    }

    var step = arr.length / maxlen;
    var result = [];
    for (var i = 0; i < arr.length; i += step) {
        result.push(arr[parseInt(i, 10)]);
    }
    return result;
}
