<?php
require '../../db.php'; // Подключение к базе данных

// Получаем данные из вебхука
$webhookData = file_get_contents('php://input');
$data = json_decode($webhookData, true);
$hook = R::dispense('hooks');
$hook->web = $webhookData;
$hook->data = $data;
R::store($hook);
?>
