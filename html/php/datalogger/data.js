let CHART_DATA = [{
    // "date": 0,
    // "tm": 0,
    // "hm": 0,
}];

$.ajax({
    type: "GET",
    dataType: "json",
    url: "https://script.google.com/macros/s/AKfycbynwry1Y6hpy_D2WcmXC9-uqZ4IbWqA78ec5tCgwz8LGpMhYyQ/exec",
    success: function (data) {
        CHART_DATA = data;
        chartRemake();
    }
});
