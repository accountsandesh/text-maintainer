# I made this file - ME


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return HttpResponse("about app <a href='http://127.0.0.1:8000/'>Home</a>")

def analyze(request):
    # get the text
    djtext = request.POST.get('text','this is text default')
    removePunc = request.POST.get('removepunc','off')
    uppercase = request.POST.get('uppercase','off')
    newlineremove = request.POST.get('newlineremove','off')
    removeextraspace = request.POST.get('removeextraspace','off')
    charcount = request.POST.get('charcount','off')
    onofflist = []
    try:
        if removePunc == "on":
            # print(removePunc)
            punctuations = ''';:\|{}[]-_()!@#$%^&*<>?',"`~.'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            onofflist.append(removePunc)
            params = {'purpose':'Removed Punctuations','analyzed_text': analyzed,'onoff':onofflist}
            djtext = analyzed
    
        if uppercase == "on":
            # print(uppercase)
            analyzed = djtext.upper()
            onofflist.append(uppercase)
            params = {'purpose':'in UPPERCASE','analyzed_text': analyzed,'onoff':onofflist}
            djtext = analyzed

        if newlineremove == "on":
            analyzed = djtext.replace('\n','').replace('\r','')
            onofflist.append(newlineremove)
            params = {'purpose':'Removed new lines','analyzed_text': analyzed,'onoff':onofflist}
            djtext = analyzed

        if removeextraspace == "on":
            analyzed = ''
            for index, char in enumerate(djtext):
                # print(index,char)
                if not(djtext[index] == " " and djtext[index+1] == " "):
                    analyzed = analyzed + char
            # print(analyzed)
            onofflist.append(removeextraspace)
            params = {'purpose':'Removed Extra spaces','analyzed_text': analyzed,'onoff':onofflist}
            djtext = analyzed

        if charcount == 'on':
            for index, char in enumerate(djtext):
                analyzed = index + 1
            onofflist.append(charcount)
            params = {'purpose':'Count Characters','analyzed_text': analyzed,'onoff':onofflist}
            djtext = analyzed
    except Exception as e:
        print("Error Occured",e)        

    if(charcount == 'off' and newlineremove == 'off' and removeextraspace == 'off' and removePunc == 'off' and uppercase == 'off'):
        return HttpResponse("Nothing is selected")  

    # analyse the text
    
    return render(request, 'analyze.html', params)