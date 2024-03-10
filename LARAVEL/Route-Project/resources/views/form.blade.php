<!-- resources/views/age-form.blade.php -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Age Verification Form</title>
</head>

<body>
    <h1>Age Verification Form</h1>
    <form action="/check-age" method="GET">
        @csrf
        <label for="age">Enter your age:</label>
        <input type="number" id="age" name="age" required>
        <!-- ----------------------- -->
        <label for="role">Role:</label>
        <input type="text" id="role" name="role" required>
        <button type="submit">Submit</button>
    </form>
</body>

</html>
