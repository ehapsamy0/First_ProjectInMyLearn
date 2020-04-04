from django.shortcuts import render , redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
from .models import Note
from .forms import NoteForm
from accounts.models import Profile




#Show All Notes
def all_notes(request):
    user =request.user
    profile = get_object_or_404(Profile,user=user)

    all_notes = Note.objects.filter(user=user)
    context = {
        'all_notes':all_notes,
        'profile':profile,


    }

    return render(request,'notes.html',context)


#Show One Note
def detail(request , slug):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    note = Note.objects.get(slug=slug)
    context = {
        'note' : note,

        'profile': profile,
    }

    return render(request , 'one-note.html' , context)




def note_add(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'add Notes')
            return redirect('/notes')
    else:
        form = NoteForm()
    context = {
        'profile': profile,
        'form': form,


    }
    return render(request , 'add.html' , context)



def edit(request , slug):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    note = get_object_or_404(Note , slug = slug)
    if request.method == 'POST':
        form = NoteForm(request.POST , instance = note)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'edit Notes')
            return redirect('/notes')
    else:
        form = NoteForm(instance = note)

    context = {
        'profile': profile,
        'form': form,

    }
    return render(request , 'create.html' , context)