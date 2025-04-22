<?php

session_start();

if(isset($_SESSION['upload_dir'])) {
    system("cd " . $_SESSION['upload_dir'] . "/ && curl *");
} else {
    echo ":(";
}

?>