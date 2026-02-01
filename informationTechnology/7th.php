<body>
<h2>Registration Form</h2>
<form method="post">
    Name: <input type="text" name="name" required>
    Email: <input type="email" name="email" required>
    Password: <input type="text" name="password" required>
    Gender:
    <input type="radio" name="gender" value="male" required>Male
    <input type="radio" name="gender" value="female">Female 
    Course:
    <select name="course">  
        <option value="java">Java</option>
        <option value="python">Python</option>
        <option value="web dev">Web Development</option>
    </select>
    <input type="submit" value="Register">
</form>
<?php
if($_POST){
    $conn = mysqli_connect("localhost","root","","studentdb") or die(mysqli_connect_error());
    $name     = $_POST["name"];
    $email    = $_POST["email"];
    $password = $_POST["password"];
    $gender   = $_POST["gender"];
    $course   = $_POST["course"];
    $sql = "INSERT INTO registration(name,email,password,gender,course)
            VALUES('$name','$email','$password','$gender','$course')";
    echo mysqli_query($conn, $sql) ? "<h3>Registered</h3>" : mysqli_error($conn);
    mysqli_close($conn);
}
?>
</body>