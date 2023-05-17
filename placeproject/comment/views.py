from django.shortcuts import render, redirect

# Create your views here.
def commenthome(request) :
    return render(request, 'comment_index.html')
