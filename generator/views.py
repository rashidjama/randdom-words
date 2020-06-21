from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def words(request):
  if 'count' not in request.session:
    request.session['count'] = 0
  request.session['word'] = get_random_string(length=14)
  context = {
    'random_words': request.session['word'],
    'attempt': request.session['count']
  }
  return render(request, 'index.html', context)

def click(request):
  request.session['count'] += 1
  return redirect('/')
def reset(request):
  request.session.flush()
  return redirect('/words')