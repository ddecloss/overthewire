<?
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

print hex2bin(strrev(base64_decode($encodedSecret)));

?>
