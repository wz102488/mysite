from django.shortcuts import render, render_to_response
from .models import *
from django.http import Http404, FileResponse
from django.utils.http import urlquote


# Create your views here.
def home(request):
    wenZhang = WenZhang.objects.all().order_by('-createTime')
    bt = Home.objects.all()
    fenlei = Fenlei.objects.all()
    return render_to_response('home.html', { 'bt':bt,'wenZhangs': wenZhang , 'fenleis':fenlei})

def wzlist(request, fenlei_id):
    try:
        fenlei = WenZhang.objects.filter(fenlei=fenlei_id)
    except WenZhang.DoesNotExist:
        raise Http404
    #wenZhang = WenZhang.objects.all().order_by('-createTime')
    return render_to_response('wzlist.html', {'fenLeis': fenlei})

def wz(request, wz_id):
    try:
        wenZhang = WenZhang.objects.get(id=wz_id)
    #    File = WenZhang.objects.get(fileLink=wz_id)
    except WenZhang.DoesNotExist:
        raise Http404
    #wenZhang = WenZhang.objects.all().order_by('-createTime')
    return render_to_response('wz.html', {'wenzhangs': wenZhang })

def download(request, file_id):
    try:
        url = Files.objects.get(id=file_id)
    except Files.DoesNotExist:
        raise Http404
    u = str(url.fileLink)
    try:
        file = open(u, 'rb')
    except :
        raise Http404
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"'%(urlquote(u))
    return response

def about(request):
    return render(request, 'about.html')

