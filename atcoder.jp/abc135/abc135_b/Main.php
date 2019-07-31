<?php
  fscanf(STDIN,"%d",$n);
  $p=preg_split("/ /",trim(fgets(STDIN)));
  $c=0;
  for($i=1;$i<$n+1;$i++){
    if($i!=$p[$i-1]){
        $c++;
    }
  }

  if($c==0 or $c==2){
    print("YES\n");
  }else{
    print("NO\n");
  }
?>