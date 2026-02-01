<?php
echo "Refresh Page";
$file = "count.txt";
$c=file_get_contents($file);
file_put_contents($file,$c+1);
echo "The number of users visited the page is:$c";

?>