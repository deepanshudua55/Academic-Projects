<?php 
// Name: Sarvesh Sadhoo
// UTA ID: 1000980763
// URL: http://omega.uta.edu/~sxs0763/project5/signup.php
//Final2
?>
<?php 
if (isset($_POST['sub_register'])){
	$username = $_POST['username'];
	print_r($username);
	function usernameCheck($username) {
		echo "string";
		$dbname = dirname($_SERVER["SCRIPT_FILENAME"]) . "/mydb.sqlite";
		$dbh = new PDO("sqlite:$dbname");
	    $stmt = $dbh->prepare("SELECT username FROM users WHERE username = :name");
	    $stmt->bindParam(':name', $username);
	    $stmt->execute();
	    $table = $stmt->fetchAll();
	    if (sizeof($table) > 0) {
	        echo "exists!";
	        header('Location:board.php');
	    } 
	    else {
	        echo "non existant";
	        $query="insert into users values('".$_POST['username']."','".md5($_POST['password'])."','".$_POST['fname']."','".$_POST['email']."')";
			$command = $dbh->prepare($query);
			$command->execute();
			header('Location:board.php');
	    }
	}
usernameCheck($username);
}
?>
<html>
<h2>New User Registration Form</h2>
</head>
<body>
<form name="register" method="post">
<table width="510" border="0">
<tr>
<td>Full Name:</td>
<td><input type="text" name="fname" maxlength="20"></td>
</tr>
<tr>
<td>Username:</td>
<td><input type="text" name="username"></td>
</tr>
<tr>
<td>Password:</td>
<td><input type="password" name="password"></td>
</tr>
<tr>
<td>Email:</td>
<td><input type="text" name="email"></td>
</tr>
<tr>
<td>&nbsp;</td>
<td><input type="submit" value="Register" name="sub_register"/></td>
</tr>
</table>
</form>
</body>
</html>
