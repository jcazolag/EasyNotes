from django.shortcuts import render
import whisper as wp
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Transcripciones, Resumen

import os

# Create your views here.


def whisper(request):
    if request.method == 'GET':
        return render(request, 'transcribe.html')
    else:
        if request.method == 'POST' and request.FILES['audio_file']:
            try:
                model = wp.load_model("base")
                audio = request.FILES["audio_file"]
                print(audio.size)
                fs = FileSystemStorage()
                filename = fs.save(audio.name, audio)
                name= audio.name
                result = model.transcribe("media/" + name, language="es", fp16 = False)
                if os.path.exists('media/' + name):
                    os.remove('media/' + name)
                return render(request,'transcribe.html', {'result': result, 'mensaje':'Este es el resultado de la transcripcion: '})
            except Exception as e:
                return render(request, 'transcribe.html', {'result': e})

    #return render(request, 'transcribe.html',{"result": result })

def detail(request, transcripcion_id):
    transcripcion = get_object_or_404(Transcripciones,pk=transcripcion_id)
    resumen = Resumen.objects.filter(transcripcion_id = transcripcion_id)
    return render(request, 'detail.html',{'transcripcion':transcripcion, 'resumen': resumen})

def Notes(request):
    transcripcion = Transcripciones.objects.all()
    return render(request, 'notes.html', {'transcripciones': transcripcion})