<?php
// Подключаемся к базе данных
require '../../db.php';

$webhookData = file_get_contents('php://input');
$data = json_decode($webhookData, true);

$message = $data['messages'][0];
$msg = R::dispense('webhooks');
$msg->messagid = $message['id'];
$msg->fromme = $message['from_me'];
$msg->messagetype = $message['type'];
$msg->chatid = $message['chat_id'];
$msg->timestamp = $message['timestamp'];
$msg->source = $message['source'];
$msg->body = $message['text']['body'];
$msg->number = $message['from'];
$msg->name = $message['from_name'];
$msg->channelid = $data['channel_id'];

// Сохраняем данные в базу
R::store($msg);
?>
