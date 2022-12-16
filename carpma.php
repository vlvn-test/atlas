<?php

function topla() {
  $toplam = 0;
  $argumanSayisi = func_num_args();
  for ($i = 0; $i < $argumanSayisi; $i ++) {
    $toplam += func_get_arg($i);
  }
  return $toplam;
}

function carpma() {
  $carpim = 1;
  $argumanSayisi = func_num_args();
  for ($i = 0; $i < $argumanSayisi; $i ++) {
    $carpim *= func_get_arg($i);
  }
  return $carpim;
}

// Ornek Kullanim
// echo carpma(2, 3, 4); // 24 dondurur