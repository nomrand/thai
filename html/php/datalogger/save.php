<?php

$DLOGGED_DATE_FILE = 'logged';
$DATA_FILE = 'data.js';

#### CHECK PARAMETERS ####
$param = $_POST["data"];
#$param = $_GET["data"];
if (empty($param)) {
    echo ("NO DATA");
    return;
}
$data = explode(",", $param);
if(count($data) % 3 != 0){
    echo ("ILLEGAL DATA");
    return;
}

#### START LOOP ####
$logged_time = file_get_contents($DLOGGED_DATE_FILE);
$logged_time = intval($logged_time);
printf("<b>LOG START:%d</b><br>", $logged_time);

for($index=0; $index<count($data); $index+=3){
    $unixtime = intval($data[$index]);
    if($logged_time >= $unixtime){
        printf("* PASSED DATA:%d<br>", $unixtime);
        continue;
    }

    $tm = floatval($data[$index+1]);
    $hm = floatval($data[$index+2]);

    # data output
    file_put_contents(
        $DATA_FILE,
        "data.push({'date':'$unixtime', 'tm':'$tm', 'hm':'$hm'})\n",
        FILE_APPEND);
    printf("Write data:%d, tm:%d, hm:%d<br>", $unixtime, $tm, $hm);

    $logged_time = $unixtime;
}

#### SAVE THE NEWEST DATE IN DATA ####
printf("<b>LOG WRIGHT:%d</b><br>", $logged_time);
file_put_contents($DLOGGED_DATE_FILE, $logged_time);

?>
