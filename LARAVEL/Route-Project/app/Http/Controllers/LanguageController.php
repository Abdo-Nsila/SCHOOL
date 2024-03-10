<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class LanguageController extends Controller
{
    public function showWelcomeMessage($lang)
    {
        // Déterminez le message de bienvenue en fonction de la langue
        $message = '';

        if ($lang == 'fr') {
            $message = 'Bienvenue';
        } elseif ($lang == 'eng') {
            $message = 'Hello';
        } else {
            abort(404); // Langue non prise en charge
        }

        // Retournez une vue avec le message
        return view('welcome_message')->with('message', $message);
    }
}
