<?php
	session_start(); 
	if(isset($_POST['btnLogin'])){
		require 'connect_db.php'; 
		$username =  $_POST['username'];
		$password = $_POST['password']; 
		
		$username = stripslashes($username); 
		$passsword = stripslashes($password); 
		
		$result = mysqli_query($connect,'SELECT studentID, password FROM students
		WHERE studentID="'.$username.'" AND password ="'.$password.'"');
				
		if(mysqli_num_rows($result)==1)
		{
			// if they are in the database register the user id
			$_SESSION['username'] = $username;
			header("Location: index.php");
		}
		else{
			echo"Error! Incorrect ID and/or password!"; 
			header("Location: login_student.php");
		}
}
?>


<!DOCTYPE html>

<head>
    <title>Login</title>
        <meta charset="windows-1252">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" type="text/css" href="myCSS.css">
</head>
<header><center>Login - Students </header></center>

	<table width="300" border="0" align="center" cellpadding="0" cellspacing="1" bgcolor="#CCCCCC">
	<tr>
		<form name="form1" method="post">
		<td>
		<table width="100%" border="0" cellpadding="3" cellspacing="1" bgcolor="#FFFFFF">
		<tr>
		<td colspan="3"><strong>Student Login </strong></td>
	</tr>
	<tr>
		<td width="78">Username</td>
		<td width="6">:</td>
		<td width="294"><input name="username" type="text" id="username" required></td>
		</tr>
	<tr>
		<td>Password</td>
		<td>:</td>
		<td><input name="password" type="password" id="password"required></td>
	</tr>
	<tr>
	<td>&nbsp;</td>
	<td>&nbsp;</td>
	<td><input type="submit" name="btnLogin" value="Login"></td>
	</tr>
		</table>
	</td>
	</form>
	</tr>
	</table>

</html>