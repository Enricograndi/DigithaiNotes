from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *
from notes.forms import *

@login_required(login_url='login')
def create_notes(request):
    # View for creating a new note.
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            # Create a new Notes object and save it to the database.
            notes = form.save(commit=False)
            notes.user = request.user
            notes.save()
            messages.success(request, 'Your note is saved')
        else:
            messages.error(request, 'Ops, something went wrong')
    else:
        form = NotesForm()
    
    context = {'form': form,'title':"Create note"}
    return render(request, 'create-notes.html', context)

@login_required(login_url='login')
def list_notes(request):
    # View for listing all notes or filtering based on a search query.
    search = request.GET.get('search')
    user = request.user

    if search:
        # If a search query is provided, filter the notes by the query.
        filter_params = Q(user=user, title__icontains=search)
        notes = Notes.objects.filter(filter_params)
    else:    
        # If no search query is provided, list all notes for the current user.
        notes = Notes.objects.filter(user=user)

    context = {'notes': notes, 'title':"Your notes"}
    return render(request, 'list-notes.html', context)


@login_required(login_url='login')
def show_note(request, id):
    # View for displaying a specific note by its ID.
    note = get_object_or_404(Notes, id=id)
    context = {'note': note, 'title':str(note.title)}
    return render(request, 'show-note.html', context)


@login_required(login_url='login')
def edit_notes(request, id):
    # View for editing a specific note by its ID.
    note = get_object_or_404(Notes, id=id)
    
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            # Save the edited note to the database.
            form.save()
            messages.success(request, 'Your note was updated')
        else:
            messages.error(request, 'Ops, something went wrong')
    else:
        form = NotesForm(instance=note)
    
    context = {'form': form, 'title':"Edit note"}
    return render(request, 'create-notes.html', context)


@login_required(login_url='login')
def delete_notes(request, id):
    # View for deleting a specific note by its ID.
    try:
        note = get_object_or_404(Notes, id=id)
        note.delete()
        messages.success(request, 'Your note was updated')
    except: 
        messages.error(request, 'Ops, something went wrong')


    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes}
    return render(request, 'list-notes.html', context)
