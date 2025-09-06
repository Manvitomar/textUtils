from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
 
def analyze(request):
    text = request.GET.get('text', 'default')
    operation=request.GET.get('operation','OFF')
    punctuations = '''.,;:!?'"`-_()[]{}<>/\|@#$%^&*~+=…―'''
    data = ""

    if operation == "removepunc":
        for char in text:
            if char not in punctuations:
                data = data + char
  
        params = {'purpose': 'Removed Punctuations', 'data': data}
        return render(request, 'analyze.html', params)
    
    elif operation=="capitalize":
        for char in text:
          data+=char.upper()
        params = {'purpose': 'Capitalize', 'data': data}
        return render(request, 'analyze.html', params)
  
    
    elif operation=="charCounter":
      count=0
      for char in text:
        if char==" ":
           pass
        else:
           count=count+1
      params = {'purpose': 'Character Counter', 'data': count}
      return render(request, 'analyze.html', params)
      
    elif operation=="spaceremove":
      for char in text:
        if char=='  ':
           pass
        else:
         data+=char
      params = {'purpose': 'Space Remover', 'data': data}
      return render(request, 'analyze.html', params)
    
    elif operation=="newlineremover":
      for char in text:
        if char=='\n':
           pass
        else:
         data+=char
      params = {'purpose': 'New Line Remover', 'data': data}
      return render(request, 'analyze.html', params)
    
    elif operation == "wordCounter":
     words = text.split() 
     count = len(words)  
     params = {'purpose': 'Word Counter', 'data': 'Number of Words: ' + str(count)}
     return render(request, 'analyze.html', params)

    else:
     return HttpResponse('''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Error</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
      body, html {
        margin: 0;
        padding: 0;
        height: 100%;
        font-family: Arial, sans-serif;
      }

      .cont {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #000;
        color: #fff;
        text-align: center;
        padding: 20px;
      }

      .box {
        background-color: #1c1c1c;
        padding: 50px 40px;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.5);
        max-width: 90%;
      }

      h2 {
        margin-bottom: 20px;
        font-size: 2rem;
      }

      .btn {
        margin-top: 30px;
        background-color: #007bff;
        color: #fff;
        padding: 12px 25px;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 250px;
      }

      .btn:hover {
        background-color: #0056b3;
        transform: scale(1.05);
      }

      .btn a {
        color: white;
        text-decoration: none;
        display: block;
      }

      @media (max-width: 500px) {
        .box {
          padding: 30px 20px;
        }

        .btn {
          width: 80%;
        }
      }
    </style>
  </head>
  <body>
    <div class="cont">
      <div class="box">
        <h2>Error</h2>
        <p>Something went wrong. Please try again.</p>
      </div>
      <button class="btn">
        <a href="http://127.0.0.1:8000/">Go Back</a>
      </button>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>''')
