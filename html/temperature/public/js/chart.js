const MAX_DATA_NUM = 200;
let CHART;

// *** data for display ***
const DATA_SETS = [
    {
        borderWidth: 2,
        label: "Temperature (温度:อุณหภูมิ)",
        borderColor: "rgba(220, 100, 0, 1)",
        yAxisID: 'y-axis-1',
        data: []
    },
    {
        borderWidth: 1,
        label: "Humidity (湿度:ความชื้น)",
        borderColor: "rgba(0, 120, 255, 0.5)",
        yAxisID: 'y-axis-2',
        data: []
    },
    {
        borderWidth: 1,
        pointRadius: 1,
        label: "Brightness (照度:ความสว่าง)",
        borderColor: "rgba(255, 255, 255, 0.1)",
        backgroundColor: "rgba(220, 220, 220, 0.1)",
        yAxisID: 'y-axis-3',
        data: []
    },
];

const MONTHLY_DATA = [];
for (let i = 0; i < 12; i++) {
    MONTHLY_DATA.push({
        borderWidth: 1,
        label: monthStr(i).slice(0, 3),
        borderColor: rgbaStr(hueRGB(12, i - 4)),
        data: []
    });
}

function getDateFormat(start, end) {
    let dif = end - start;
    let oneday = 1000 * 60 * 60 * 24;
    if (dif > oneday * 500) {
        return 'MMM YYYY';
    }
    if (dif > oneday * 200) {
        return 'MMM DD YYYY';
    }
    if (dif > oneday * 10) {
        return 'MMM DD YYYY ha';
    }
    return 'MMM DD YYYY h:mma';
}

$(function () {
    // datepicker
    $("#date1, #date2").datepicker({
        dateFormat: "M dd yy"
    });
    let nowdate = new Date();
    let lastmonth = new Date();
    if (window.innerWidth > 640) {
        lastmonth.setDate(1);
    }
    $("#date1").datepicker("setDate", lastmonth);
    $("#date2").datepicker("setDate", nowdate);

    $("#date1, #date2").change(function () {
        let start_millisec = $("#date1").datepicker("getDate");
        let end_millisec = $("#date2").datepicker("getDate");
        if (start_millisec.getTime() > end_millisec.getTime()) {
            $("#date1").datepicker("setDate", end_millisec);
            $("#date2").datepicker("setDate", start_millisec);
        }

        chartRemake();
    });

    // radio
    $('input[name="mode"]').change(function () {
        if ($(this).val() != "normal") {
            $("#date1, #date2").prop("disabled", true);
        } else {
            $("#date1, #date2").prop("disabled", false);
        }

        chartRemake();
    })

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
                    time: {
                        displayFormats: {
                            hour: '  MMM D, ha  ',
                        }
                    },
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
                            fontSize: 14,         // フォントサイズ
                            fontColor: "#F83",
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
                            fontSize: 14,         // フォントサイズ
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
                    {
                        id: 'y-axis-3',
                        display: false,
                        gridLines: {
                            color: "#444",
                            borderDash: [5, 10],
                        },
                        ticks: {
                            max: 100,
                            min: 0,
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
                    filter: function (items, chartData) {
                        let yesno = true;
                        if (DATA_SETS[2].label == items.text) {
                            yesno = false;
                        }
                        return yesno;
                    },
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

    chartRemake();
});

function chartRemake() {
    // *** get & set data ***
    for (key in DATA_SETS) {
        DATA_SETS[key].data = [];
        for (mon in MONTHLY_DATA) {
            MONTHLY_DATA[mon].data = []
        }
    }

    let isOneDay = false;

    // normal mode
    if ($('input[name="mode"]:checked').val() == "normal") {
        let start_millisec = $("#date1").datepicker("getDate").getTime();
        let end_millisec = new Date($("#date2").datepicker("getDate").getTime() + (24 * 60 * 60 * 1000)).getTime();
        if (end_millisec - start_millisec <= (24 * 60 * 60 * 1000)) {
            isOneDay = true;
        }
        let sliced = timeslicearr(CHART_DATA, start_millisec / 1000, end_millisec / 1000);

        $.each(compressarr(sliced, MAX_DATA_NUM), function (index, val) {
            let millisec = val.date * 1000;
            let d = new Date();
            d.setTime(millisec);

            DATA_SETS[0].data.push({
                x: d,
                y: flr(val.tm, 1),
            });
            DATA_SETS[1].data.push({
                x: d,
                y: flr(val.hm, 1),
            });
            DATA_SETS[2].data.push({
                x: d,
                y: flr(rt(val.li), 1),
            });
        });

        CHART.data.datasets = DATA_SETS;
        if (isOneDay) {
            CHART.options.scales.xAxes[0].time.displayFormats.hour = ' ha ';
        } else {
            CHART.options.scales.xAxes[0].time.displayFormats.hour = ' MMM D, ha ';
        }
        CHART.options.scales.xAxes[0].time.tooltipFormat = getDateFormat(start_millisec, end_millisec);
        CHART.options.scales.yAxes[0].display = true;
        CHART.options.scales.yAxes[1].display = true;
    }
    if ($('input[name="mode"]:checked').val() == "monthly") {
        // monthly mode
        isOneDay = true;
        let monthly = monthlyarr(CHART_DATA);
        for (mon in monthly) {
            $.each(hourlyarr(monthly[mon]), function (index, hourlys) {
                let val = avgarr(hourlys);

                let tmp = new Date();
                tmp.setHours(index);
                tmp.setMinutes(0);
                MONTHLY_DATA[mon].data.push({
                    x: tmp,
                    y: flr(val.tm, 1),
                });
            });
        }
        CHART.data.datasets = MONTHLY_DATA;
        CHART.options.scales.xAxes[0].time.displayFormats.hour = ' ha ';
        CHART.options.scales.xAxes[0].time.tooltipFormat = "h:mma";
        CHART.options.scales.yAxes[0].display = true;
        CHART.options.scales.yAxes[1].display = false;
    }
    CHART.update({
        duration: 800,
    });
}

function rt(val) {
    if (val == null) {
        return null;
    }
    return val;
}