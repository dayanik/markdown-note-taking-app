#import language_tool_python

from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.http import HttpRequest

from notes import models, forms


# tool = language_tool_python.LanguageTool('ru-RU')


def index(request: HttpRequest):
    notes = models.Note.objects.all()
    grammar_result = None
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "save_text":
            text_form = forms.TextForm(request.POST)
            if text_form.is_valid():
                text = text_form.cleaned_data['text']
                title = "_".join(text_form.cleaned_data['title'].split()) + ".md"
                file = ContentFile(text.encode("utf-8"), name=title)
                note = models.Note()
                note.file.save(title, file)
                note.save()
                return redirect("index")
        elif action == "check":
            return
            matches = tool.check(text)
            grammar_result = []
            for match in matches:
                grammar_result.append(
                    {
                        "error": match.context,
                        "message": match.message,
                        "replacements": match.replacements
                    }
                )
        elif action == "upload_file":
            file_form = forms.NoteForm(request.POST, request.FILES)
            if file_form.is_valid():
                file_form.save()
            file_form = forms.NoteForm()
                
    else:
        text_form = forms.TextForm()
        file_form = forms.NoteForm()
    context = {
        "notes": notes, 
        "text_form": text_form, 
        "file_form": file_form,
        "grammar_result": grammar_result
    }
    return render(request, "notes/index.html", context=context)


def download_note(request: HttpRequest, note_id: int):
    pass


def html_note(request: HttpRequest, note_id: int):
    pass
