from django.shortcuts import render
# from portfolio import views
from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import Contact


def index(request):
#  
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname, email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you Soon!")

        return redirect('/')

    # return render(request,'contact.html')
    return render(request,'index.html')

def Portfoliodetails(request):
    return render(request,'portfolio-details.html')

def Innerpage(request):
    return render(request,'inner-page.html')