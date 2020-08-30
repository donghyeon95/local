import json
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'app/index.html')

def pdf_view(request):
    if request.method == 'GET':
        return render(request, 'app/viewer.html')
    elif request.method == 'POST':
        text = [request.POST.get("search", None),request.POST.get("title", None)] 
        return HttpResponse(text)
        #return render(request, 'app/index.html')

def result(request):
#    search_key = request.GET['search_key'] 
#    context = {'search_key':search_key} 
#    return render(request,'result/result.html',context)
    if request.is_ajax():
        return render(request,'result/result.html')
    else:
        return render(request,'result/result.html')

def post_result(request):
    keyword = request.POST.get('search_key', '')

    message = "임시 데이터. 적절하게 수정할 필요가 있다."

    context = {'secret_key': message }

    return HttpResponse(json(context), content_type="application/json")

#def searchText(request):
#   if request.method == 'GET':
#        pass
#    elif request.method == 'POST':
        
        
