<?php
setcookie("time", date("d-m-Y h:i:s"));

if (isset($_COOKIE["time"]))
    echo "Last visit: " . $_COOKIE["time"];
else
    echo "First visit";
?>







