import language_tool_python
import mistune
import os

from django.core.files.base import ContentFile
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, Http404, FileResponse

from notes import models, forms


tool = language_tool_python.LanguageTool(
    'ru-RU',
    remote_server=os.getenv("LANGUAGE_TOOL_HOST")
)


def index(request: HttpRequest):
    notes = models.Note.objects.all()
    grammar_result = None
    text_form = forms.TextForm()
    file_form = forms.NoteForm()
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
            text_form = forms.TextForm(request.POST)
            if text_form.is_valid():
                text = text_form.cleaned_data['text']
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

    context = {
        "notes": notes, 
        "text_form": text_form, 
        "file_form": file_form,
        "grammar_result": grammar_result
    }
    return render(request, "notes/index.html", context=context)


def download_note_file(request: HttpRequest, note_id: int):
    note = get_object_or_404(models.Note, note_id=note_id)
    file_path = note.file.path
    if os.path.exists(file_path):
        return FileResponse(
            open(file_path, "rb"), 
            as_attachment=True,
            filename=os.path.basename(file_path)
        )
    else:
        raise Http404("файд не найден")


def get_html_note(request: HttpRequest, note_id: int):
    try:
        note = get_object_or_404(models.Note, note_id=note_id)
        with note.file.open() as file:
            text = file.read().decode("utf-8")
        html = mistune.markdown(text)
        context = {"html_text": html}
    except Http404:
        context = {"html_text": "that note is not found"}
    except:
        context = {"html_text": "that file is not found"}

    return render(request, "notes/text.html", context=context)
