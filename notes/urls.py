from django.urls import path
from . import views as notes_views

urlpatterns = [
    # URL for creating a new note
    path('create-notes', notes_views.create_notes, name='create-notes'),

    # URL for listing all notes
    path('list-notes', notes_views.list_notes, name='list-notes'),

    # URL for editing a specific note by providing its ID as a parameter
    path('edit-notes/<int:id>', notes_views.edit_notes, name='edit-notes'),

    # URL for deleting a specific note by providing its ID as a parameter
    path('delete-notes/<int:id>', notes_views.delete_notes, name='delete-notes'),

    # URL for displaying a specific note by providing its ID as a parameter
    path('show-note/<int:id>', notes_views.show_note, name='show-note'),

    # URL for searching notes by providing the title as a parameter
    #path('search-note/<str:title>', notes_views.search_notes, name='search-note'),
]
