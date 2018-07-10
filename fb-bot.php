<?php
// https://developers.facebook.com/docs/graph-api/reference/post

// $data['link'] = "https://skolakoda.org/";
$data['message'] = "Zdravo od PHP bota Škole koda.";
// $data['picture'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Coca_Cola_-_Mexican_death_sentence.jpg/470px-Coca_Cola_-_Mexican_death_sentence.jpg";
// $data['description'] = "Coca Cola - Mexican death sentence.";

$data['access_token'] = getenv('PAGE_ACCESS_TOKEN');
$post_url = 'https://graph.facebook.com/' . getenv('PAGE_ID') . '/feed';

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $post_url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
$return = curl_exec($ch);
curl_close($ch);

echo $return;
