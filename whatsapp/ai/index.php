<?php
// Подключаемся к базе данных
require '../../db.php';

// Получаем данные из вебхука
$webhookData = file_get_contents('php://input');
$data = json_decode($webhookData, true);

// Логируем данные для проверки
file_put_contents('webhook.log', print_r($data, true));

// Сохраняем данные в базу как есть
$msg = R::dispense('webhooks');
$msg->data = $webhookData;
R::store($msg);

echo 'Данные успешно сохранены!';
?>
