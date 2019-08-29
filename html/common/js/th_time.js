const TH_DAY = ["อาทิตย์", "จันทร์",
    "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์"];
const TH_MONTH = ["มกราคม", "กุมภาพันธ์", "มีนาคม",
    "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน",
    "ตุลาคม", "พฤศจิกายน", "ธันวาคม"];
const TH_MONTH_S = ["ม.ค.", "ก.พ.", "ม.ค.",
    "เม.ย.", "พ.ค.", "มิ.ย.", "ก.ค.", "ส.ค.", "ก.ย.",
    "ต.ค.", "พ.ย.", "ธ.ค."];

function thdate(date, sep, hasDayName, monthShort, buddaYear) {
    let str = "";

    if (hasDayName) {
        str += TH_DAY[date.getDay()] + sep;
    }
    str += date.getDate() + sep;
    str += (monthShort ? TH_MONTH_S[date.getMonth()] : TH_MONTH[date.getMonth()]) + sep;
    str += date.getYear() + 1900 + (buddaYear ? 543 : 0);

    return str;
}
