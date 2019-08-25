const BAR_HEIGHT_PER_STUDENT = 24;
const CTX = $("#chart").get(0).getContext("2d");
let CHART = null;
let DISPLAY_TARGET_DATA = [];

$(function () {
    const param = getUrlParam();
    if (param["class"]) {
        $('input#cls5' + param["class"]).prop('checked', true);
    }

    $('input[name=disp]').change(function () {
        chartRemake();
    })

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
                            fontSize: 20,         // フォントサイズ
                            fontColor: "#DDD",
                        },
                        ticks: {
                            fontSize: 12,         // フォントサイズ
                            fontColor: "#DDD",
                        },
                        gridLines: {
                            color: "#444",
                        },
                    },
                ],
                xAxes: [
                    {
                        position: 'top',
                        stacked: true,              //積み上げ棒グラフの設定
                        scaleLabel: {             // 軸ラベル
                            display: true,          // 表示設定
                            labelString: 'points',  // ラベル
                            fontSize: 20,          // フォントサイズ
                            fontColor: "#DDD",
                        },
                        ticks: {
                            fontSize: 16,         // フォントサイズ
                            fontColor: "#DDD",
                        },
                        gridLines: {
                            color: "#444",
                        },
                    }
                ]
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
            tooltips: {
                footerFontSize: 16,
                callbacks: {
                    footer: function (tooltipItem, chart) {
                        // comment                        
                        return separateWords(DISPLAY_TARGET_DATA[tooltipItem[tooltipItem.length - 1].index].comment, ' ', 40).join("\n");
                    },
                },
            },
        }
    });
    chartRemake();
});

function getLabel() {
    return DISPLAY_TARGET_DATA.map((val, index) => getLabelValue(val));
}
function getLabelValue(val) {
    return val.class + " No." + pad0(2, val.number);
}
function getData() {
    return CHART_DATA.work.
        map(function (val, index) {
            let data = DISPLAY_TARGET_DATA.map(function (dval, dindex) {
                return dval.points[index];
            });

            let cl = rgbaStr(whRGB(capRGB(hueRGB(20, Math.floor(index * 2.7)), 200, 50), 0.15));
            return {
                label: val,
                data: data,
                borderColor: cl,
                backgroundColor: cl,
            };
        });
}

function updateCondition() {
    let undispClass = [];
    $('input[name=disp]').each(function () {
        if (!$(this).prop('checked')) {
            undispClass.push($(this).val());
        }
    })
    DISPLAY_TARGET_DATA = CHART_DATA.data.filter(val => !undispClass.includes(val.class))

    $("#chartdiv, #chart").css("height",
        (DISPLAY_TARGET_DATA.length * BAR_HEIGHT_PER_STUDENT) + "px");
    CHART.resize();
}
function chartRemake() {
    updateCondition();
    CHART.data.labels = getLabel();
    CHART.data.datasets = getData();
    CHART.update({
        duration: 800,
    });
}
