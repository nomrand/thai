// get.gs
function getData(sheetName) {
  // Get data
  var rowssum = [];
  
  var ss = SpreadsheetApp.getActive();
  for(var i=1; i<10; i++){
    var sheet = ss.getSheetByName(sheetName + parseInt(i, 10));
    if(sheet == null){
      continue;
    }
    var rows_i = sheet.getDataRange().getValues();
    rowssum = rowssum.concat(rows_i);
  }
  var sd = ss.getSheetByName(sheetName);
  var row_data = sd.getDataRange().getValues();
  rowssum = rowssum.concat(row_data);
    
  var obj = [];
  var t = 0;
  rowssum.map(function(row) {
    if (parseInt(row[1],10) > t){
      obj.push({
        "date": row[1],
        "tm": row[2],
        "hm": row[3],
      });
      t = parseInt(row[1],10);
    }
    return null;
  });
  
  return obj;
}


// rest.gs
function doGet() {
  var data = getData('data');

  // Object to JSON
  return ContentService.createTextOutput(JSON.stringify(data, null, 2))
  .setMimeType(ContentService.MimeType.JSON);
}