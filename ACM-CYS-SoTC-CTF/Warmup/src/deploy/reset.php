<?php
session_start();

if (isset($_SESSION['upload_dir'])) {
    $dir = $_SESSION['upload_dir'];
    if (is_dir($dir)) {
        system("rm -rf " . escapeshellarg($dir));
    }
    unset($_SESSION['upload_dir']);
}

echo "Reset done";
?>
