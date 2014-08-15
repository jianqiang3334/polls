from django.shortcuts import render
from poll.models import Poll,Choice
from django.shortcuts import render_to_response,HttpResponseRedirect,HttpResponse
from django import forms
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
# Create your views here.

def pollWeb(request):
    pollObj = Poll.objects.all()
    choiceObj = Choice.objects.all()
    return render_to_response('pollWeb.html', {'Poll': pollObj,'Choice':choiceObj})
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
def upload_file(request):
  if request.method == 'POST':
     form = UploadFileForm(request.POST,request.FILES)
     h="ok"
     if form.is_valid():
         h=h+"ok"
  return HttpResponse(h)
"""else:
        form = UploadFileForm()
        return HttpResponseRedirect("/pollWeb/") """






