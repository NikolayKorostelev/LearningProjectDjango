from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main (request):
    return HttpResponse ('''<!DOCTYPE html>
<html>
 <head>
  <title>Заголовки разделенные</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
 </head>
 <body>
 
  <h1>Заголовки разделенные</h1>
  
  <h2>Это заголовок 1</h2>
  <p>Это какое-то текст.</p>
  <hr>

<h2>Это заголовок 2</h2>
  <p>Это какой-то другой текст.</p>
  <hr>

  <h2>Это заголовок 2</h2>
  <p>Это какой-то другой текст.</p>

 </body>
</html>''')