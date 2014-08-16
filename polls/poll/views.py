from django.shortcuts import render
from poll.models import Poll,Choice,Upload
from django.shortcuts import render_to_response,HttpResponseRedirect,HttpResponse
from django import forms
import datetime
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
# Create your views here.

def pollWeb(request):
    pollObj = Poll.objects.all()
    choiceObj = Choice.objects.all()
    form = UploadFileForm()
    url = "../download_file/"
    return render_to_response('pollWeb.html', {'Poll': pollObj,'Choice':choiceObj,'form':form,'url':url})
def submit(request):
    choiceObj = Choice.objects.all()
    h=0
    html="html"
    for choice in choiceObj:
        #htm=choice.poll_id
        choice_key = "choice_"+str(choice.poll_id)
        if choice_key in request.GET:
            html=html+str(request.GET[choice_key])
            if choice.id == int(request.GET[choice_key]):
                choice.votes += 1
                choice.save()
    return HttpResponseRedirect("/pollWeb/")
def handle_uploaded_file(title,f):
    now = datetime.datetime.now()
    diretionary = "upload_file/"  + f.name
    with open(diretionary, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    upload = Upload()
    upload.title = title
    upload.file = diretionary
    upload.save()
def upload_file(request):
  if request.method == 'POST':
     form = UploadFileForm(request.POST,request.FILES)
     if form.is_valid():
         handle_uploaded_file(request.POST['title'], request.FILES['file'])
         return HttpResponse("upload ok")
     else:
         return HttpResponseRedirect("/pollWeb/")
  else:
    return HttpResponseRedirect("/pollWeb/")
def download_file(request):
    file_1 = Upload.objects.filter(id = 5)
    f = open(file_1[0].file)
    file_content = f.read()
    f.close()
    response = HttpResponse(file_content,mimetype='application/octet-stream')
    name = file_1[0].title + file_1[0].file[-4:]
    response['Content-Disposition'] = 'attachment; filename=%s' % name
    return response
""" h = file.file
    f = open(file.file)
    file_content = f.read()
    f.close()

    response = HttpResponse(file_content,mimetype='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=%s' % file.file
    return response"""








