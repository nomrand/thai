let CHART_DATA = {
    "data": [
    ],
    "work": [
    ],
    "maxpoints": [
    ]
};

$.ajax({
    type: "GET",
    dataType: "json",
    url: "point.php",
    success: function (data) {
        CHART_DATA = data;
        chartRemake();
    }
});
