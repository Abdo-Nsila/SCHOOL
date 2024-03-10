<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\Response;

// class CheckAge {
//     public function handle(){
//         $age = 2;
//         if ($age < 18){
//             return abort(404);
//         }
//         return redirect('/profil-utilisateur');
//     }
// }

class CheckAge
{
    public function handle($request, Closure $next, $role, $minAge)
    {
        if ($request->role == $role && $request->age > $minAge) {
            return $next($request);
        }
        return redirect('/form');
    }
}

class CheckAg1
{
    public function handle($request, Closure $next, $role)
    {
        if ($request->role == $role && $request->age > 18) {
            return $next($request);
        }
        return redirect('/age-form');
    }

    public function handle2(Request $request, Closure $next): Response
    {
        return $next($request);
    }

    /**
     * Handle tasks after the response has been sent to the browser.
     */
    public function terminate(Request $request, Response $response): void
    {
        // ... Check response 
    }
}
