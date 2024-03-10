<!DOCTYPE html>
<html>

<head>
    <title>Add New Article</title>
</head>

<body>
    <h2>Add New Article</h2>
    <form action="{{ route('articles.store') }}" method="POST">
        @csrf <!-- CSRF protection for Laravel -->
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title"><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content"></textarea><br><br>
        <button type="submit">Submit</button>
    </form>
</body>

</html>