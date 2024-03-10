<!DOCTYPE html>
<html>
<head>
    <title>Edit Article</title>
</head>
<body>
    <h2>Edit Article</h2>
    <form action="{{ route('articles.update', ['id' => $article['id']]) }}" method="POST">
        @csrf <!-- CSRF protection for Laravel -->
        @method('PUT') <!-- Use PUT method for updating the article -->
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" value="{{ $article['title'] }}"><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content">{{ $article['content'] }}</textarea><br><br>
        <button type="submit">Update</button>
    </form>
</body>
</html>

