//    0: r-Max, g-0  , b-0
// Hue1: r-Max, g-Max, b-0
// Hue2: r-0  , g-Max, b-0
// Hue3: r-0  , g-Max, b-Max
// Hue4: r-0  , g-0  , b-Max
// Hue5: r-Max, g-0  , b-Max
// Hue6: r-Max, g-0  , b-0
const HueConst = [
    [255, 0, 0],
    [255, 255, 0],
    [0, 255, 0],
    [0, 255, 255],
    [0, 0, 255],
    [255, 0, 255],
    [255, 0, 0],
];
function hueRGB(huemax, huei) {
    while (huemax <= huei) {
        huei -= huemax;
    }

    let decAfter = (HueConst.length - 1) / huemax * huei;
    let decBefore = Math.floor(decAfter);
    decAfter -= decBefore;

    return toRGB(HueConst[decBefore], HueConst[decBefore + 1], decAfter);
}

function bkRGB(fromRGB, diff) {
    return toRGB(fromRGB, [0, 0, 0], diff);
}
function whRGB(fromRGB, diff) {
    return toRGB(fromRGB, [255, 255, 255], diff);
}
function toRGB(fromRGB, toRGB, diff) {
    return [
        Math.floor(fromRGB[0] + (toRGB[0] - fromRGB[0]) * diff),
        Math.floor(fromRGB[1] + (toRGB[1] - fromRGB[1]) * diff),
        Math.floor(fromRGB[2] + (toRGB[2] - fromRGB[2]) * diff),
    ];
}
function capRGB(fromRGB, top, bot) {
    return [
        Math.max(bot, Math.min(top, fromRGB[0])),
        Math.max(bot, Math.min(top, fromRGB[1])),
        Math.max(bot, Math.min(top, fromRGB[2])),
    ];
}
function rgbaStr(rgb, alpha) {
    if (typeof alpha === "undefined") {
        alpha = 1;
    }
    return "rgba(" + rgb[0] + ", " + rgb[1] + ", " + rgb[2] + ", " + alpha + ")";
}


