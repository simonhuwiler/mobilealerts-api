<?php
  // ini_set('display_errors', 1);
  // ini_set('display_startup_errors', 1);
  // error_reporting(E_ALL);
  ini_set('display_errors', 0);

  header('Access-Control-Allow-Origin: *');
  header("Access-Control-Allow-Methods: POST");
  header('Content-Type: application/json; charset=utf-8');

  $headers = 'User-Agent:Dalvik/2.1.0 (Linux; U; Android 6.0; Android SDK built for x86 Build/MASTER)\r\n'.
             'Content-Type: application/x-www-form-urlencoded\r\n'.
             'Host:www.data199.com';

  $url = 'https://www.data199.com/api/v1/dashboard';
  $data = file_get_contents('php://input');

  // use key 'http' even if you send the request to https://...
  $options = array(
      'http' => array(
          'header'  => $headers,
          'method'  => 'POST',
          'content' => http_build_query(json_decode($data))
      )
  );
  $context  = stream_context_create($options);
  echo file_get_contents($url, false, $context);

?>