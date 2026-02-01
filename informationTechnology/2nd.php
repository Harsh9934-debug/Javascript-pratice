<?php
echo "Multiplication Table ";
echo "This is the table representaion form the 1 to 10 ";
echo "<table border= '1'cellspacing='0' cellpadding='5'>";
for($i=1;$i<=10;$i++){
  echo "<tr>";
  for($j=0;$j<=10;$j++){
    $result=$i*$j;
    echo "<td> $i X $j = $result </td>";
  }
 echo "</tr>";
}
echo "</table>"
?>