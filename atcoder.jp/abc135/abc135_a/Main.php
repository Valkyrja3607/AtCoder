<?php
fscanf(STDIN,"%d%d",$a,$b);
if (($a+$b)%2==0){
    print ($a+$b)/2;
}else{
    print("IMPOSSIBLE");
}
?>
