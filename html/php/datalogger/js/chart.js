let CHART;

// *** data for display ***
let DATA_SETS = [
    {
        label: "Temperature (温度:อุณหภูมิ)",
        borderColor: "rgba(220, 100, 0, 1)",
        yAxisID: 'y-axis-1',
        data: []
    },
    {
        label: "Humidity (湿度:ความชื้น)",
        borderColor: "rgba(0, 150, 220, 1)",
        backgroundColor: "rgba(0, 150, 255, 0.4)",
        yAxisID: 'y-axis-2',
        data: []
    },
];

$(function () {
    $("#date1, #date2").datepicker({
        dateFormat: "dd M yy"
    });
    let nowdate = new Date();
    let lastmonth = new Date();
    lastmonth.setDate(1);
    $("#date1").datepicker("setDate", lastmonth);
    $("#date2").datepicker("setDate", nowdate);

    $("#date1, #date2").change(function () {
        chartRemake();
    });

    // *** display chart ***
    var ctx = $("#chart").get(0).getContext("2d");
    CHART = new Chart(ctx, {
        type: 'line',
        data: {
            //            labels: LABELS,
            datasets: DATA_SETS,
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    type: 'time',
                    stacked: true,              //積み上げ棒グラフの設定
                    ticks: {
                        fontSize: 16,         // フォントサイズ
                        fontColor: "#DDD",
                    },
                    gridLines: {
                        color: "#444",
                    },
                }],
                yAxes: [
                    {
                        position: 'left',
                        id: 'y-axis-1',
                        scaleLabel: {            // 軸ラベル
                            display: true,          // 表示設定
                            labelString: 'Temperature [°C]',  // ラベル
                            fontSize: 20,         // フォントサイズ
                            fontColor: "#D93",
                        },
                        ticks: {
                            fontSize: 12,         // フォントサイズ
                            fontColor: "#DDD",
                            stepSize: 5,
                        },
                        gridLines: {
                            color: "#444",
                        },
                    },
                    {
                        position: 'right',
                        id: 'y-axis-2',
                        scaleLabel: {            // 軸ラベル
                            display: true,          // 表示設定
                            labelString: 'Humidity [%]',  // ラベル
                            fontSize: 20,         // フォントサイズ
                            fontColor: "#0AD",
                        },
                        ticks: {
                            fontSize: 12,         // フォントサイズ
                            fontColor: "#DDD",
                            stepSize: 5,
                        },
                        gridLines: {
                            color: "#444",
                            borderDash: [5, 10],
                        },
                    },
                ],
            },
            legend: {
                labels: {
                    boxWidth: 10,
                    padding: 10,        //凡例の各要素間の距離
                    fontSize: 16,
                    fontColor: "#FFF",
                },
                display: true,
            },
            elements: {
                line: {
                    tension: 0, // ベジェ曲線を無効にする
                }
            },
            // for straight line
            /* bezierCurve: false */
        }
    });
});

function chartRemake() {
    let start_millisec = $("#date1").datepicker("getDate").getTime();
    let end_millisec = new Date($("#date2").datepicker("getDate").getTime() + (24 * 60 * 60 * 1000)).getTime();

    // *** get & set data ***
    for (key in DATA_SETS) {
        DATA_SETS[key].data = [];
    }
    $.each(CHART_DATA, function (index, val) {
        let millisec = val.date * 1000;
        if (millisec < start_millisec) {
            return;
        }
        if (millisec > end_millisec) {
            return;
        }

        let d = new Date();
        d.setTime(millisec);

        DATA_SETS[0].data.push({
            x: d,
            y: val.tm,
        });
        DATA_SETS[1].data.push({
            x: d,
            y: val.hm,
        });
    });

    CHART.data.datasets = DATA_SETS;
    CHART.update({
        duration: 800,
    });
}
