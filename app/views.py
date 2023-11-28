from django.shortcuts import render

# Create your views here.
def bootstrap_download(request):
    return render(request,'bootstrap_download.html')

def bootstrap2(request):
        return render(request,'bootstrap2.html')
    
def bootstrap3(request):
        return render(request,'bootstrap3.html')


