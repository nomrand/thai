function getData(sheetName) {
  // Get data
  var sheet = SpreadsheetApp.getActive().getSheetByName(sheetName);
  var rows = sheet.getDataRange().getValues();
  
  // Define
  const ROW_NUM_HEADERS = 2;
  const ROW_TITLES = 1;
  const ROW_MAX_POINTS = 0;
  const COL_POINT_START = 4;

  // Get sub-data
  var header = rows.splice(0, ROW_NUM_HEADERS);
  var titles = header[ROW_TITLES];
  var max_points = header[ROW_MAX_POINTS];
  
  // N-Lines Array Object (each line has each studen's data)
  var linesObject = rows.map(function(row) {
    var obj = {};
    // student data
    row.slice(0, COL_POINT_START).map(function(item, index) {
        // title-VALUE map
        obj[String(titles[index])] = String(item);
    });
    
    // points which get by each work
    obj["points"] = row.slice(COL_POINT_START);
    return obj;
  });
  
  return {
    data : linesObject,
    work : titles.slice(COL_POINT_START),
    maxpoints : max_points.slice(COL_POINT_START),
  };
}

// GET
function doGet() {
  var data = getData('Points');

  // Object to JSON
  return ContentService.createTextOutput(JSON.stringify(data, null, 2))
  .setMimeType(ContentService.MimeType.JSON);
}