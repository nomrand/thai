let CHART_DATA = [
    //{
    // "date": 0,
    // "tm": 0,
    // "hm": 0,
    // "li": 0,
    //}
];

{
    let newestDate = 0;
    const DATA_KEY = "temperture_report";
    var storedData = store.get(DATA_KEY);
    if (storedData) {
        CHART_DATA = storedData;
        newestDate = CHART_DATA[CHART_DATA.length - 1].date;
    }

    db.collection("values")
        .where("date", ">", newestDate)
        .orderBy('date')
        .onSnapshot(function (snapshot) {
            let logdata = snapshot.docChanges();

            logdata.forEach(function (change) {
                if (change.type === "added") {
                    // Support Adding Only
                    let data = change.doc.data();
                    CHART_DATA.push(data);
                }
                if (change.type === "modified") {
                    console.log("Modified: ", change.doc.data());
                }
                if (change.type === "removed") {
                    console.log("Removed: ", change.doc.data());
                }
            });

            store.set(DATA_KEY, CHART_DATA);
            chartRemake();
        });
}

let CHART_DATA_INFO = [
];
if (INFOSW) {
    let newestDate = 0;
    const DATA_KEY = "temperture_report_info";
    var storedData = store.get(DATA_KEY);
    if (storedData) {
        CHART_DATA_INFO = storedData;
        newestDate = CHART_DATA_INFO[CHART_DATA_INFO.length - 1].date;
    }

    db.collection("infos")
        .where("date", ">", newestDate)
        .orderBy('date')
        .onSnapshot(function (snapshot) {
            let logdata = snapshot.docChanges();

            logdata.forEach(function (change) {
                if (change.type === "added") {
                    // Support Adding Only
                    let data = change.doc.data();
                    CHART_DATA_INFO.push(data);
                }
                if (change.type === "modified") {
                    console.log("Modified: ", change.doc.data());
                }
                if (change.type === "removed") {
                    console.log("Removed: ", change.doc.data());
                }
            });

            store.set(DATA_KEY, CHART_DATA_INFO);
            chartRemake();
        });
}