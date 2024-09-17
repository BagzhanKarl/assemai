<?php
$webhookData = file_get_contents('php://input');
$data = json_decode($webhookData, true);
file_put_contents('webhook.log', print_r($data, true));
?>
