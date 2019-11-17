<?php

require '../vendor/autoload.php';
header('content-type: application/json; charset=utf-8');

# Setting Variable
$TARGET_FILE_NAME="data.xlsx";
$TARGET_SHEET_NAME="DATA";
$CLASS_COLUMN='A';
$NUMBER_COLUMN='B';
$COMMENT_COLUMN='C';
$DATA_START_COLUMN='D'; # Column A-C are informations
$DATA_TITLE_ROW=2; # Data start at $DATA_TITLE_ROW+1

# Processing Start
$reader = \PhpOffice\PhpSpreadsheet\IOFactory::createReader('Xlsx');
$reader->setReadDataOnly(TRUE);
$spreadsheet = $reader->load($TARGET_FILE_NAME);

$worksheet = $spreadsheet->getSheetByName($TARGET_SHEET_NAME);


##################################
# Make JavaScript Data
##################################
echo 'let CHART_DATA = {' . PHP_EOL;

# Get Data Title
$workarray = [];
echo '"work" : [' . PHP_EOL;
$row = $worksheet->getRowIterator($DATA_TITLE_ROW)->current();
$cellIterator = $row->getCellIterator($DATA_START_COLUMN);
$cellIterator->setIterateOnlyExistingCells(FALSE);
foreach ($cellIterator as $cell) {
    if ($cell->getValue() != "") {
        if ($cellIterator->key() != $DATA_START_COLUMN){
            echo ',';
        }
        echo '"' . $cell->getValue() . '"';
        echo PHP_EOL;

        # remember valid work
        $workarray[] = $cell->getColumn();
    }
}
echo '],' . PHP_EOL;

# Get Data Body
echo '"data" : [' . PHP_EOL;
$rowIterator = $worksheet->getRowIterator($DATA_TITLE_ROW+1);
foreach ($rowIterator as $row) {
    if ($rowIterator->key() != $DATA_TITLE_ROW+1){
        echo ',';
    }
    echo '{' . PHP_EOL;
        $rindex = $row->getRowIndex();
        # Information
        echo '"class" : "' . $worksheet->getCell($CLASS_COLUMN . $rindex)
            . '",' . PHP_EOL;
        echo '"number" : "' . $worksheet->getCell($NUMBER_COLUMN . $rindex)
            . '",' . PHP_EOL;
        echo '"comment" : "' . $worksheet->getCell($COMMENT_COLUMN . $rindex)
            . '",' . PHP_EOL;

        # Points
        echo '"points" : [' . PHP_EOL;
            foreach ($workarray as $workcol) {
                if ($workarray[0] != $workcol){
                    echo ',';
                }
                echo $worksheet->getCell($workcol . $rindex);
                echo PHP_EOL;
            }
        echo ']';
    echo '}';
    echo PHP_EOL;
}
echo ']';
echo '};' . PHP_EOL;