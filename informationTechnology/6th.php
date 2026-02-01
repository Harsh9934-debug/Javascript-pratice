<?php
setcookie("time", date('d-m-y h:i:s'));
$msg = $_COOKIE["time"] ?? "You are visiting for the first time";
?>
<html>
<body>
<center><h2>last visited the person is</h2></center>
<br>
<?= $msg == "You are visiting for the first time" ? $msg : "Last time login is $msg"; ?>
</body>
</html>
