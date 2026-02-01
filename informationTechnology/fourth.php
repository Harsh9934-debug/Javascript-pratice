<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="p4.php?course=BCA&college=presidency" method="post">
        FirstName: <input type="text" name="firstname" id="firstname">
        <br>
        LastName: <input type="text" name="lastname" id="lastname">
        <br>
        Email: <input type="email" name="email" id="email">
        <br>
        Password: <input type="password" name="password" id="password">
        <br>
        Gender: <input type="radio" name="gender" id="gender">
        <br>
        Age:<input type="number" name="age" id="age">
        <br>
        Address:<input type="text" name="address" id="address">
        <br>
        <input type="submit" value="Submit">
    </form>
</body>

<?php
    if($_SERVER["REQUEST_METHOD"] == "POST"){
       $firstname = $_POST["firstname"];
       $lastname = $_POST["lastname"];
       $email = $_POST["email"];
       $password = $_POST["password"];
       $gender = $_POST["gender"];
       $age = $_POST["age"];
       $address = $_POST["address"]; 
       echo "<h1>Form Data</h1>";
       echo "<p>First Name: $firstname</p>";
       echo "<p>Last Name: $lastname</p>";
       echo "<p>Email: $email</p>";
       echo "<p>Password: $password</p>";
       echo "<p>Gender: $gender</p>";
       echo "<p>Age: $age</p>";
       echo "<p>Address: $address</p>";
    }
?>  
</html>