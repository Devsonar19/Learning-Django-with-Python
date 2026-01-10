from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # context = {
    #     'name' : 'John Wick',
    #     'Weapon' : 'Guns, lots of guns..!',
    #     'age' : 45,
    # }
    return render(request, 'index.html')

def countWord(request):
    words = request.POST['words']
    count_of_words = len(words.split())
    return render(request, 'countWord.html', {'amount' : count_of_words})
