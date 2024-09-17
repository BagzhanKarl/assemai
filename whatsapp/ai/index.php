<?php
require 'db.php'; // Подключение к базе данных

// Получаем данные из вебхука
$webhookData = file_get_contents('php://input');
$data = json_decode($webhookData, true);

// Проверяем, что данные пришли корректно
if (isset($data['messages']) && is_array($data['messages'])) {
    foreach ($data['messages'] as $message) {
        // Создаем новую запись в таблице "messages"
        $msg = R::dispense('messages');
        $msg->message_id = $message['id'];
        $msg->from_me = $message['from_me'];
        $msg->type = $message['type'];
        $msg->chat_id = $message['chat_id'];
        $msg->timestamp = $message['timestamp'];
        $msg->source = $message['source'];
        $msg->body = $message['text']['body'];
        $msg->from_number = $message['from'];
        $msg->from_name = $message['from_name'];

        // Сохраняем сообщение в базу данных
        R::store($msg);
    }

    echo 'Данные успешно сохранены!';
} else {
    echo 'Ошибка: Неверный формат данных';
}
?>
