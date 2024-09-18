<?php

$url = 'https://gate.whapi.cloud/';
$token = 'rmXQbivTFcJHwIpQtDWu58co0TaeqOCN';

$data = '{"messages":[{"id":"OoKFxugCJB.eOA-gOkSGu1bag","from_me":false,"type":"text","chat_id":"77761174378@s.whatsapp.net","timestamp":1726658279,"source":"mobile","text":{"body":"Добрый день!"},"from":"77761174378","from_name":"3D"}],"event":{"type":"messages","event":"post"},"channel_id":"DAREDL-B3F92"}';

$data = json_decode($data, true);
$messages = $data['messages'];
