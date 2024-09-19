<?php
// Подключаемся к базе данных
require '../../db.php';

// Получаем данные из вебхука
$webhookData = file_get_contents('php://input');
$data = json_decode($webhookData, true);

// Проверяем, что данные корректны
if (isset($data['messages'][0])) {
    // Извлекаем данные из массива
    $message = $data['messages'][0];
    $event = $data['event'];

    // Подготавливаем объект для сохранения
    $msg = R::dispense('webhooks');
    $msg->message_id = $message['id'];
    $msg->from_me = $message['from_me'];
    $msg->message_type = $message['type'];
    $msg->chat_id = $message['chat_id'];
    $msg->timestamp = $message['timestamp'];
    $msg->source = $message['source'];
    $msg->body = $message['text']['body'];
    $msg->from_number = $message['from'];
    $msg->from_name = $message['from_name'];
    $msg->event_type = $event['type'];
    $msg->event_event = $event['event'];
    $msg->channel_id = $data['channel_id'];

    // Сохраняем данные в базу
    R::store($msg);

    echo 'Данные успешно сохранены!';
} else {
    echo 'Некорректные данные';
}
?>
