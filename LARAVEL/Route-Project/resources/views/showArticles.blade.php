<!DOCTYPE html>
<html>

<head>
    <title>Articles</title>
</head>

<body>
    <h1>Articles</h1>

    <!-- <?php echo '<pre>';
            print_r($articles);
            echo '</pre>';
            ?> -->

    <table border="2">
        <thead>
            <tr>
                <th>Title</th>
                <th>Content</th>
            </tr>
        </thead>
        <tbody>
            @foreach ($articles as $article)
            <tr>
                <td>{{ $article['title'] }}</td>
                <td>{{ $article['content'] }}</td>
            </tr>
            @endforeach
        </tbody>
    </table>

</body>

</html>