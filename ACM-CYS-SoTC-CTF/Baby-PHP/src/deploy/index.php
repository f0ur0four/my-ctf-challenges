<?php

if (isset($_POST['baby'])) {
    if (!preg_match('/[a-zA-Z0-9]/', $_POST['baby'])) {
        ob_start();
        eval("echo ". $_POST['baby'] . ";");
        $out = ob_get_clean();
        
        if (preg_match('/STC/i', $out)) {
            echo "This is a baby challenge, what do you expect? :)";
        } else {
            echo $out;
        }
    } else {
        echo "Dangerous code detected";
    }
}

?>
