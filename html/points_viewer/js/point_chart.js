const BAR_HEIGHT_PER_STUDENT = 14;
const CTX = $("#chart").get(0).getContext("2d");
let CHART = null;
let UNDISP_CLASSES = [];

$(function () {
    $('input[name=undisp]').change(function () {
        chartRemake();
    })
    $("#chartdiv, #chart").css("height",
        (24 * BAR_HEIGHT_PER_STUDENT + 500) + "px");


    let labels = getLabel();
    let datasets = getData();

    // *** display chart ***
    CHART = new Chart(CTX, {
        type: 'horizontalBar',
        data: {
            labels: labels,
            datasets: datasets,
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                yAxes: [
                    {
                        barThickness: "flex",        //棒グラフの幅
                        autoSkip: false,
                        stacked: true,              //積み上げ棒グラフの設定
                        scaleLabel: {            // 軸ラベル
                            display: true,          // 表示設定
                            labelString: 'Students',  // ラベル
                            fontSize: 16,         // フォントサイズ
                        },
                    },
                ]
                , xAxes: [
                    {
                        position: 'top',
                        stacked: true,              //積み上げ棒グラフの設定
                        scaleLabel: {             // 軸ラベル
                            display: true,          // 表示設定
                            labelString: 'points',  // ラベル
                            fontSize: 16,          // フォントサイズ
                        }
                    }
                ]
            },
            legend: {
                labels: {
                    boxWidth: 10,
                    padding: 10,        //凡例の各要素間の距離
                },
                display: true,
            },
            tooltips: {
                mode: "index"
            }
        }
    });
    chartRemake();
});

function getLabel() {
    let undispClasses = [];
    $('input[name=undisp]').each(function () {
        if (!$(this).prop('checked')) {
            undispClasses.push($(this).val());
        }
    })

    return CHART_DATA.data.
        filter(val => !UNDISP_CLASSES.includes(val.class)).
        map(function (val, index) {
            if (UNDISP_CLASSES.length == 0) {
                return val.class + " No." + pad0(2, val.number);
            } else {
                return val.class + " No." + pad0(2, val.number) + "  " + val.name;
            }
        });
}
function getData() {
    return CHART_DATA.work.
        filter(val => !UNDISP_CLASSES.includes(val.class)).
        map(function (val, index) {
            let data = CHART_DATA.data.map(function (dval, dindex) {
                return dval.points[index];
            });

            return {
                label: val,
                data: data,
                borderColor: rgbaStr(hueRGB(50, index), 1),
                backgroundColor: rgbaStr(hueRGB(50, index), 0.4),
            };
        });
}

function updateCondition() {
    UNDISP_CLASSES = [];
    $('input[name=undisp]').each(function () {
        if (!$(this).prop('checked')) {
            UNDISP_CLASSES.push($(this).val());
        }
    })
}
function chartRemake() {
    updateCondition();
    CHART.data.labels = getLabel();
    CHART.data.datasets = getData();
    CHART.update();
}
