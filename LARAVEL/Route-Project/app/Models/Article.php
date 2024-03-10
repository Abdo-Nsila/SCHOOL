<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Article extends Model
{
    protected $fillable = ['title', 'content']; // Specify which attributes are mass-assignable

    // Define relationships, if any
}
