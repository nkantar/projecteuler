<?

$total = 0;

for($i = 1; $i < 1000; $i++) {
  if(!($i % 3)) {
    $total += $i;
  } elseif(!($i % 5)) {
    $total += $i;
  }
}

echo $total."\n\n";

?>
