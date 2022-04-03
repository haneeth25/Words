from django.shortcuts import redirect, render
from . import models

# Create your views here.

def display_words(requests):
    words = models.Words.objects.all()
    context = {'words':words}
    return render(requests,'display_words/home_page.html',context)
def word_form(requests):
    if requests.method == 'POST':
        word_entered = requests.POST.get('word')
        form = models.Words(
            word  = word_entered,
        )
        form.save()
    return render(requests,'display_words/word_form.html')
def update_word(requests,pk):
    update_word = models.Words.objects.get(id=pk)
    if requests.method == 'POST':
        word_entered = requests.POST.get('word')
        update_word.word = word_entered
        update_word.save()
        return redirect('display_words')
    return render(requests,'display_words/update_word.html')

def delete_word(request,pk):
    word_to_delete = models.Words.objects.get(id=pk)
    if request.method == 'POST':
        word_to_delete.delete()
        return redirect('display_words')
    return render(request,'display_words/delete_word.html',{'word':word_to_delete})
