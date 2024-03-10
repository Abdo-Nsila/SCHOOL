<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ArticleController;
use App\Http\Middleware\CheckAge;



/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

// Route::get('/', function () {
//     return view('welcome');
// });

Route::get('/laravel/public', function () {
    return view('public');
});

Route::get('/laravel/public/login', function () {
    return view('login');
});


Route::get('/laravel/public/page/{id}', function ($id) {
    return view('page');
});


Route::get('/redirection', function () {
    return view('redirection');
});
Route::get('/p', function () {
    return redirect('http://localhost:8000/redirection');
});


Route::get('/user/{id}', function ($id) {
    return view('user')->with('id', $id);
});


Route::get('/langue/{lang}', function ($lang) {
    $message = '';

    if ($lang == 'fr') {
        $message = 'Bienvenue';
    } elseif ($lang == 'eng') {
        $message = 'Hello';
    } else {
        abort(404); // Langue non prise en charge
    }

    // Retournez une vue avec le message
    return view('langue')->with('message', $message);
});

Route::get('/code-postal/{code}', function ($code) {
    $message = '';

    if (preg_match('/^[0-9]{5}$/', $code)) {
        $message = 'Code Postal: ' . $code;
    } else {
        $message = 'Le code postal est incorrect';
    }

    // Retournez une vue avec le message
    return view('codePostal')->with('message', $message);
});


//! Route nommées
Route::get('/profile', function () {
    return view('profile');
})->name('user.profile')->middleware([CheckAge::class]); // Nommez la route si nécessaire

Route::get('/', function () {
    $url = route('user.profile');
    return view('welcome', ['url' => $url]);
});

//! Regrouper Route
Route::prefix('/articles')->group(function () {
    Route::get('/', [ArticleController::class, 'getAll'])->name('articles.index');
    Route::get('/create', [ArticleController::class, 'create'])->name('articles.create');
    Route::post('/', [ArticleController::class, 'store'])->name('articles.store');
    Route::get('/{id}', [ArticleController::class, 'getSpec'])->name('articles.show');
    Route::get('/{id}/edit', [ArticleController::class, 'edit'])->name('articles.edit');
    Route::put('/{id}', [ArticleController::class, 'update'])->name('articles.update');
});





Route::view('/form', 'form');

//! Global Middleware
Route::middleware('age:user,18')->get('/check-age', function () {
    return view('profile');
});

//! Specifique Middleware
Route::middleware([CheckAge::class . ':admin,18'])->get('/check-age', function () {
    return view('profile');
});
