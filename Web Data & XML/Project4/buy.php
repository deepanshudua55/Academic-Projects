<?php 
// Name: Sarvesh Sadhoo
// UTA ID: 1000980763
// URL: http://omega.uta.edu/~sxs0763/project4/buy.php
// Final2
?>
<?php 
// Starts the session and destroys the session on "Empty Basket"
session_start(); 
if (isset($_GET['clear'])) {
	session_destroy();
	header("location:"."buy.php");

} 
?>
<html>
<head><title>Buy Products</title></head>
<body>
<p>Shopping Basket:</p>

<?php
// Create a Sesion that stores the id of the product seleected to put in shopping cart
if(!isset($_SESSION['id'])){
	$_SESSION['id'] = array();
}
if(isset($_GET['buy'])){
	array_push($_SESSION['id'], $_GET['buy']);
}
?>
<?php
// Puts the product in the session shopping cart with respect to the product id passed
if(!isset($_SESSION['shopping_cart']))
	$_SESSION['shopping_cart'] = array();
if(isset($_GET['buy'])){
	foreach ($_SESSION['id'] as $i) {
		foreach ($_SESSION['data'] as $key => $value) {
			if($i===$value[0]){
				array_push($_SESSION['shopping_cart'], $value);
			}
		}
	}
}

?>
<?php 
// Deletes duplicate product
$shopping_Array = $_SESSION['shopping_cart'];
$outputArray = array();
$key = array(); 
foreach ($shopping_Array as $inside_Arr) { 
    if (!in_array($inside_Arr[0], $key)) { 
        $key[] = $inside_Arr[0]; 
        $outputArray[] = $inside_Arr; 
    }
}
$_SESSION['shopping_cart'] = $outputArray;
?>

<?php
//Deletes the sected product
if(isset($_GET['delete'])){
	foreach ($_SESSION['shopping_cart'] as $key => $value) {
			if (in_array($_GET['delete'], $value)){
				unset($_SESSION['shopping_cart'][$key]);
		}	
	}
} 
?>
<?php 
//Displays the shoppng cart and calculates sum
$sum = 0;
if(isset($_SESSION['shopping_cart'])){
	echo "<table border='1'>";
	
	foreach ($_SESSION['shopping_cart'] as $inner_array) {
		echo "<tr>";
		//echo "<td>".$inner_array[0]."</td>";
		echo "<td><a href=".$inner_array[4]."><img src=\"".$inner_array[1]."\"></td>";
		echo "<td>".$inner_array[2]."</td>";
		echo "<td>"."$".$inner_array[3]."</td>";
		echo "<td><a href=buy.php?delete=".$inner_array[0].">delete</a></td>";
		$sum += $inner_array[3];
		echo "</tr>";
	}
	echo "<table border='1'>";

}

?>
<p/>
Total: <?php echo "$".$sum ?><p/>
<form action="buy.php" method="GET">
<input type="hidden" name="clear" value="1"/>
<input type="submit" value="Empty Basket"/>
</form>
<p/>
<form action="buy.php" method="GET">
<fieldset><legend>Find products:</legend>
<label>Search for items: <input type="text" name="search"/><label>
<input type="submit" name="Submit" value="Search"/>
</fieldset>
</form>
<p/>

<?php
//Displays shopping cart according to the search criteria
error_reporting(E_ALL);
ini_set('display_errors','Off');

if (isset($_GET['Submit'])) {
	$url = "http://sandbox.api.ebaycommercenetwork.com/publisher/3.0/rest/GeneralSearch?apiKey=78b0db8a-0ee1-4939-a2f9-d3cd95ec0fcc&trackingId=7000610&keyword=";
	$encode_url = $url.urlencode($_GET['search']);
	$xmlstr = file_get_contents($encode_url);
	$xml = new SimpleXMLElement($xmlstr);
	header('Content-Type: text/html');

	global $main_Array;
	$main_Array = array();
	$_SESSION['data'] = array();
		if($xml){
			global $product_array;
			foreach($xml->categories->category->items->product as $product) {	
				$product_array = array();
				$imag_url =(string)$product->images->image->sourceURL;
				$prod_name = (string) $product->name;
				$prod_price = (string)$product->minPrice;
				$prod_id = (string)$product->attributes();
				$offerURL = (string)$product->productOffersURL;
				array_push($product_array,$prod_id,$imag_url, $prod_name, $prod_price,$offerURL);
				array_push($_SESSION['data'], $product_array); 
			}
			
		}
		echo "<table border='1'>";
			foreach ($_SESSION['data'] as $inner_array) {
					echo "<tr>";
					//echo "<td>".$inner_array[0]."</td>";
					echo "<td><a href=buy.php?buy=".$inner_array[0]."><img src=\"".$inner_array[1]."\"></td>";
					echo "<td>".$inner_array[2]."</td>";
					echo "<td>"."$".$inner_array[3]."</td>";
					//echo "<td>".$key[2]."</td>";
					echo "</tr>";
			}
		echo "<table border='1'>";
	}
?>
</body>
</html>
