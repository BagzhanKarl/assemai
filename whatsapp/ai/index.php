<?php
// Подключаемся к базе данных
require '../../db.php';

$webhookData = file_get_contents('php://input');
$data = json_decode($webhookData, true);
$check = R::findOne('webhooks', 'number = ?', [$data['from']]);

if($check){
    $check->status = 1;
    R::store($check);
}

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
$msg->status = 0;

$chats = R::dispense('chats');
$chats->phone = $message['from'];

if($message['from_me'] == true){
    $chats->side = 'out';
}
if($message['from_me'] == false){
    $chats->side = 'in';
}
$chats->text = $message['text']['body'];
$chats->time = time();
$chats->status = 0;
R::store($chats);
// Сохраняем данные в базу
R::store($msg);

$chekshook = R::dispense('just');
$chekshook->data = $data;
R::store($chekshook);
?>
