<?php 
// Name: Sarvesh Sadhoo
// UTA ID: 1000980763
// URL: http://omega.uta.edu/~sxs0763/project5/board.php
//Final2
?>
<?php session_start();
error_reporting(E_ALL);
ini_set('display_errors','On');

$dbname = dirname($_SERVER["SCRIPT_FILENAME"]) . "/mydb.sqlite";
$dbh = new PDO("sqlite:$dbname");

if (isset($_POST['submit'])) {
	$cmd = $dbh->prepare("select * from users where username='".$_POST['username']."' and password='".md5($_POST['password'])."'");
	$cmd->execute();
	$user_data = $cmd->fetchAll();
	if (sizeof($user_data) > 0) {
		$full_name = $user_data[0][2];
		$_SESSION['fullname'] = $full_name;
		header( 'Location:message.php');
	}
	elseif (sizeof($user_data) == 0){
		header('Location:board.php');
	}	
}

?>
<html>
<head><title>Message Board</title></head>
<form method="post">
    User Name:<br>
    <input type="text" name="username"><br><br>
    Password:<br>
    <input type="password" name="password"><br><br>
    <input type="submit" name="submit" value="Sign In">
</form>

<form action="signup.php" method="post">
  New users must register here:
  <input type="submit" name="submit_register" value="Sign Up"> 
</form>

<body>

</body>
</html>
