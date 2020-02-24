let CHART_DATA = [
    //{
    // "date": 0,
    // "tm": 0,
    // "hm": 0,
    // "li": 0,
    //}
];

// $.ajax({
//     type: "GET",
//     dataType: "json",
//     url: "XXXXX",
//     success: function (data) {
//         CHART_DATA = data;
//         chartRemake();
//     }
// });

db.collection("values").orderBy('date').onSnapshot(function (snapshot) {
    let logdata = snapshot.docChanges();

    logdata.forEach(function (change) {
        if (change.type === "added") {
            // Support Adding Only
            let data = change.doc.data();
            data["date"] = Number(data["date"]);
            data["tm"] = Number(data["tm"]);
            data["hm"] = Number(data["hm"]);
            data["li"] = Number(data["li"]);
            CHART_DATA.push(data);
        }
        if (change.type === "modified") {
            console.log("Modified: ", change.doc.data());
        }
        if (change.type === "removed") {
            console.log("Removed: ", change.doc.data());
        }
    });
    chartRemake();
});

const BATCH_DATA = [
];
let count = 2000;
function batchUpdate(arr) {
    let target = arr.splice(0, 500);

    // Get a new write batch
    var batch = db.batch();

    // Set the value
    target.forEach(element => batch.set(db.collection("values").doc((count++).toString(10)), element));

    // Commit the batch
    batch.commit().then(function () {
        if (arr.length > 0) {
            batchUpdate(arr);
        }
    });
}
// batchUpdate(BATCH_DATA);
