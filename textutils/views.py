from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return HttpResponse("Hello World <a href='removepunc/'>FB</a>")

def about(request):
    return render(request,'index.html',{'name':'minhal'})

def removepunc(request):
    analyzwd_text=request.POST.get('text','default')
    remove_punc=request.POST.get('removepunc','off')
    capiltal=request.POST.get('capitalize','off')
    new_line_remover=request.POST.get('newlineremover','off')
    space_remover=request.POST.get('spaceremover','off')
    punctuation='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed=""
    if remove_punc == 'on':
        for char in analyzwd_text:
            if char not in punctuation:
                analyzed=analyzed+char
        return render(request,'analyze.html',{'purpose':'Removing Punctuation','analyzed_text':analyzed})    
    elif capiltal == "on":
        for char in analyzwd_text:
            analyzed=analyzed+char.upper()
        return render(request,'analyze.html',{'purpose':'Removing Punctuation','analyzed_text':analyzed})     
    elif new_line_remover == "on":
        for char in analyzwd_text:
            if char != '\n' and char != '\r':
                analyzed=analyzed+char.upper()
        return render(request,'analyze.html',{'purpose':'Removing Punctuation','analyzed_text':analyzed}) 
    elif space_remover == "on":
        for i,char in enumerate(analyzwd_text):
            if analyzwd_text[i] == ' ' and analyzwd_text[i+1] == ' ' :
                pass
            else:
                analyzed=analyzed+char.upper()
        return render(request,'analyze.html',{'purpose':'Removing Punctuation','analyzed_text':analyzed})                
    else:
        return HttpResponse("ERROR")

def capitalizefirst(request):
    return HttpResponse("capitalizefirst")

def newlineremove(request):
    return HttpResponse("newlineremove")  

def spaceremover(request):
    return HttpResponse("spaceremover")  

def charcounter(request):
    return HttpResponse("charcounter")  