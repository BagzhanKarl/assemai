<?php
// Подключаемся к базе данных
require '../../db.php';

// Получаем данные из вебхука
$webhookData = file_get_contents('php://input');
$data = json_decode($webhookData, true);

// Логирование данных для отладки
file_put_contents('webhook.log', print_r($data, true));

// Проверяем наличие данных
if (isset($data['type']) && $data['type'] == 'messages') {
    foreach ($data['messages'] as $message) {
        // Создаём новую запись в таблице "messages"
        $msg = R::dispense('messages');
        $msg->message_id = $message['id'];
        $msg->from_me = $message['from_me'];
        $msg->type = $message['type'];
        $msg->chat_id = $message['chat_id'];
        $msg->timestamp = $message['timestamp'];
        $msg->source = $message['source'];
        $msg->body = isset($message['text']['body']) ? $message['text']['body'] : '';
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
