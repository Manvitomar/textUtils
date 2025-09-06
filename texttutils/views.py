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
    <title>Custom Modal</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
      body {
        height: 100vh;
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #000; /* Black background */
      }
      .modal-content {
        background: #1c1c1c; /* Dark grey/black modal */
        color: #fff;
        border-radius: 12px;
        box-shadow: 0 0 25px rgba(0, 0, 0, 0.8);
      }
      .modal-body h5 {
        color: #2196f3; /* Blue heading */
        font-weight: bold;
      }
      .modal-body p {
        color: #b0b0b0; /* Light grey text */
      }
      .modal-footer {
        border-top: none;
        background-color: #111;
      }
      .btn-custom {
        flex: 1;
        padding: 12px;
        font-size: 16px;
        border: none;
        border-radius: 0;
        transition: 0.3s;
      }

      .btn-cancel {
        background-color: #333;
        color: #fff;
      }
      .btn-cancel:hover {
        background-color: #555;
      }
    </style>
  </head>
  <body>
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-body text-center p-4">
          <h5>Error</h5>
          <p>Something went wrong. Please try again later.</p>
        </div>
        <div class="modal-footer p-0">
          <button class="btn-custom btn-cancel"><a href='http://127.0.0.1:8000/'>Go Back</button>
        </div>
      </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>''')
