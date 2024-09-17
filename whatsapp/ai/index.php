<?php
require '../../db.php'; // Подключение к базе данных

// Получаем данные из вебхука
$webhookData = file_get_contents('php://input');
$data = json_decode($webhookData, true);

$hooks = R::dispense('hooks');
$hooks->data = $data;
R::store($hooks);
?>