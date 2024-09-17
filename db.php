<?php
require "db/rb-mysql.php";
R::setup( 'mysql:host=localhost;dbname=configs',
    'atatek', 'atatek' );
session_start();

date_default_timezone_set('Asia/Almaty');
?>