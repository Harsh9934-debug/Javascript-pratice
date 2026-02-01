<?php
$arr = array(3, 6, 1, 2, 9);
$temp = 0;

echo "<h4>Before sorting the array:</h4>";
print_r($arr);

for ($i = 0; $i < count($arr); $i++) {
    for ($j = 0; $j < count($arr)-1; $j++) {
        if ($arr[$j] > $arr[$j+1]) {
            $temp = $arr[$j];
            $arr[$j] = $arr[$j+1];
            $arr[$j+1] = $temp;
        }
    }
}

echo "<h4>After sorting the array:</h4>";
print_r($arr);
?>
