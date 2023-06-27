from django.contrib import admin
from app.models import Note
# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display =['id','content','audio','video']
