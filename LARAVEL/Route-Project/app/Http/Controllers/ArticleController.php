<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Article; // Assurez-vous d'importer le modèle d'article

class ArticleController extends Controller
{
    public $articles = [
        ["id" => 1, "title" => "Core i9", "content" => "Cpu High End"],
        ["id" => 2, "title" => "KAMADO", "content" => "Demon Slayer Hachira"],
    ];

    //! Méthode pour afficher la liste des articles
    public function getAll()
    {
        return view('showArticles', ['articles' => $this->articles]);
    }



    //! Méthode pour afficher un article spécifique
    public function getSpec($id)
    {
        $filteredArticles = array_filter($this->articles, function ($article) use ($id) {
            return $article['id'] == $id;
        });

        // Check if article with given id exists
        if (!empty($filteredArticles)) {
            // Get the first article (assuming there is only one article with the given id)
            $article = reset($filteredArticles);
            return view('showArticle', ['article' => $article]);
        } else {
            // Handle the case where no article with the given id is found
            abort(404);
        }
    }



    // Méthode pour afficher le formulaire de création d'article
    public function create()
    {
        return view('createArticle');
    }

    // Méthode pour enregistrer un nouvel article
    public function store(Request $request)
    {
        $newArticle = [
            'id' => count($this->articles) + 1, // Generate a unique ID for the new article
            'title' => $request->title,
            'content' => $request->content,
        ];

        // Add the new article to the existing array of articles
        array_push($this->articles, $newArticle);

        // Redirect to the appropriate page after creating the article
        return redirect()->route('articles.index');
    }




    // Méthode pour afficher le formulaire d'édition d'un article existant
    public function edit($id)
    {
        // Find the article with the given ID
        $article = null;
        foreach ($this->articles as $a) {
            if ($a['id'] == $id) {
                $article = $a;
                break;
            }
        }

        // If the article with the given ID is found, pass it to the view for editing
        if ($article) {
            return view('editArticle', ['article' => $article]);
        } else {
            // If no article with the given ID is found, return a 404 error
            abort(404);
        }
    }

    // Méthode pour mettre à jour un article existant
    public function update(Request $request, $id)
    {
        // Find the index of the article with the given ID
        $index = null;
        foreach ($this->articles as $key => $article) {
            if ($article['id'] == $id) {
                $index = $key;
                break;
            }
        }

        // If the article with the given ID is found, update its data
        if ($index !== null) {
            $this->articles[$index]['title'] = $request->title;
            $this->articles[$index]['content'] = $request->content;

            // Redirect to the appropriate page after updating the article
            return redirect()->route('articles.index');
        } else {
            // If no article with the given ID is found, return a 404 error
            abort(404);
        }
    }
}
