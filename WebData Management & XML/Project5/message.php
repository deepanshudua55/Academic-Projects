<?php 
// Name: Sarvesh Sadhoo
// UTA ID: 1000980763
// URL: http://omega.uta.edu/~sxs0763/project5/message.php
//Final2
?>
<?php
if(isset($_POST['logout'])){
	session_destroy();
	header('Location: board.php');
}
?>
<?php session_start();
//$full_name = ($_SESSION['fullname']);
$dbname = dirname($_SERVER["SCRIPT_FILENAME"]) . "/mydb.sqlite";
$dbh = new PDO("sqlite:$dbname");

if (isset($_POST['submit_post'])) {
	$created_date = date('Y-m-d H:i:s');
	$dbh->exec("insert into posts(id,postedby,datetime,message) values('".uniqid()."','". $_SESSION['fullname']."','".$created_date."','".$_POST['post_message']."')");

}

if (isset($_POST['submit_post'])){

	$query = "SELECT users.username, users.fullname , posts.datetime, posts.message FROM users, posts WHERE users.fullname = posts.postedby;";
	$stmt = $dbh->prepare($query);
	$stmt->execute();
	$post_user = $stmt->fetchAll();
	echo "<table align = 'right' border = 1 >";
	echo "<tr>";
	echo "<td>"."<b>"."User Name"."</b>"."</td>";
	echo "<td>"."<b>"."Full Name"."</b>"."</td>";
	echo "<td>"."<b>"."Date Time"."</b>"."</td>";
	echo "<td>"."<b>"."Post Message"."</b>"."</td>";
	echo "</tr>";
	foreach ($post_user as $inner_array) {
		echo "<tr>";
		echo "<td>".$inner_array[0]."</td>";
		echo "<td>".$inner_array[1]."</td>";
		echo "<td>".$inner_array[2]."</td>";
		echo "<td>".$inner_array[3]."</td>";
		echo "</tr>";
	}
	echo "<table border = 1>";
}
?>

<html>
<body>
<form method="post">
<h3> Enter your message:</h3>
<input type="text" name="post_message" style="width: 200px; height: 50px; padding: 2px"></br></br>
<input type="submit" name="submit_post" value="Submit Post"> 
<input type="submit" value="Logout" name = "logout">
</form>
</body>
</html>