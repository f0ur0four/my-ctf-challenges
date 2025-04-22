<?php
session_start();

if (!isset($_SESSION['upload_dir'])) {
    $_SESSION['upload_dir'] = 'uploads/' . uniqid('upload_', true);

    if (!mkdir($_SESSION['upload_dir'], 0777, true)) {
        $error_message = "Failed to create upload directory.";
    }
}

$uploadDir = $_SESSION['upload_dir'];
$error_message = "";

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['file'])) {
    if ($_FILES['file']['error'] == UPLOAD_ERR_OK) {
        $fileName = $_FILES['file']['name'];

        if (strpos(strtolower($fileName), 'php') !== false || strpos(strtolower($fileName), 'phtml') !== false) {
            $error_message = "Error: File Types not allowed.";
        } else {
            $filePath = $uploadDir . '/' . basename($fileName);

            if (file_exists($filePath)) {
                $error_message = "Error: File already exists.";
            } else {
                if (move_uploaded_file($_FILES['file']['tmp_name'], $filePath)) {
                    $success_message = "File uploaded successfully.";
                } else {
                    $error_message = "Error moving uploaded file.";
                }
            }
        }
    } else {
        $error_message = "Error: " . $_FILES['file']['error'];
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f9;
        }
        .upload-container {
            background-color: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 400px;
            text-align: center;
        }
        h2 {
            margin-bottom: 20px;
            color: #333;
        }
        input[type="file"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            width: 100%;
            padding: 10px;
            border: none;
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 20px;
        }
        button:hover {
            background-color: #45a049;
        }
        .message {
            margin-top: 20px;
            font-weight: bold;
        }
        .success {
            color: #4CAF50;
        }
        .error {
            color: #FF0000;
        }
    </style>
</head>
<body>
    <div class="upload-container">
        <h2>Upload a File</h2>
        <form action="upload.php" method="POST" enctype="multipart/form-data">
            <input type="file" name="file" required><br><br>
            <button type="submit">Upload File</button>
        </form>

        <?php if (isset($success_message)): ?>
            <div class="message success">
                <?= htmlspecialchars($success_message) ?>
            </div>
        <?php elseif (isset($error_message)): ?>
            <div class="message error">
                <?= htmlspecialchars($error_message) ?>
            </div>
        <?php endif; ?>
    </div>
</body>
</html>
