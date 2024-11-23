<?php
if (isset($_GET['Submit'])) {
    // Get input
    $id = $_GET['id'];

    // Validate input
    if (!is_numeric($id)) {
        die('<pre>Invalid ID provided. Please use a numeric ID.</pre>');
    }

    // Database connection
    $mysqli = new mysqli('localhost', 'user', 'password', 'dvwa');

    if ($mysqli->connect_error) {
        die('Database connection failed: ' . $mysqli->connect_error);
    }

    // Secure query using prepared statements
    $stmt = $mysqli->prepare("SELECT first_name, last_name FROM users WHERE user_id = ?");
    $stmt->bind_param('i', $id); // 'i' specifies integer

    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $html = '<pre>User ID exists in the database.</pre>';
    } else {
        header($_SERVER['SERVER_PROTOCOL'] . ' 404 Not Found');
        $html = '<pre>User ID is MISSING from the database.</pre>';
    }

    $stmt->close();
    $mysqli->close();
}
?>
