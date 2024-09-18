<?php
// Подключаемся к базе данных
require '../../db.php';

// Получаем данные из вебхука
$webhookData = file_get_contents('php://input');
$data = json_decode($webhookData, true);

$messages = $webhookData['messages'];
// Сохраняем данные в базу как есть
$msg = R::dispense('webhooks');
$msg->messageid = $messages['id'];
$msg->from_me = $messages['from_me'];
$msg->type = $messages['type'];
$msg->chat_id = $messages['chat_id'];
$msg->phone = $messages['phone'];
$msg->text = $messages['text']['body'];
$msg->timestamp = $messages['timestamp'];
R::store($msg);

echo 'Данные успешно сохранены!';
?>
