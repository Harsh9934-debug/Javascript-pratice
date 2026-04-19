<?php
    setcookie("time", date('d-m-Y h:i:s'));
?>
<html>
<body>
    <center><h2>Last Visit Details</h2></center>
    <center>
    <?php
        if (isset($_COOKIE["time"])) {
            echo "Your last visit was on: " . $_COOKIE["time"];
        } else {
            echo "You are visiting for the first time!";
        }
    ?>
    </center>
</body>
</html>
