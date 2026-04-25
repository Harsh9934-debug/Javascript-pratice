<?php
echo "Multiplication Table (1 to 10) <table border='1' cellspacing='0' cellpadding='5'>";
for($i=1;$i<=10;$i++){
    echo "<tr>";
    for($j=0;$j<=10;$j++) echo "<td>$i X $j = ".($i*$j)."</td>";
    echo "</tr>";
}
echo "</table>";
?>