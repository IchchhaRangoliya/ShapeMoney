from ast import Return
from urllib import request
from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def TestPage(request):
    return render(request,"app/index-gentian-multi.html")

def aboutusbasePage(request):
    return render(request,"app/page-about.html")        

def aboutuslinumPage(request):
    return render(request,"app/page-about-v2.html")

def aboutuscyanusPage(request):
    return render(request,"app/page-about-v3.html")        

def ourteamsPage(request):
    return render(request,"app/page-team.html")

def walletv1Page(request):
    return render(request,"app/page-wallets.html")

def walletv2Page(request):
    return render(request,"app/page-wallets-v2.html")

def featuresPage(request):
    return render(request,"app/page-features.html")   

def tokansalesPage(request):
    return render(request,"app/page-token-sale.html")        

def roadmapPage(request):
    return render(request,"app/page-roadmap.html")    

def downloadPage(request):
    return render(request,"app/page-download.html")

def faqsPage(request):
    return render(request,"app/page-faq.html")        

def contactbasePage(request):
    return render(request,"app/page-contact.html")

def contactcyanusPage(request):
    return render(request,"app/page-contact-v2.html")

def exchangecyanusPage(request):
    return render(request,"app/page-exchange.html")

def partnercyanusPage(request):
    return render(request,"app/page-partner.html")

def missioncyanusPage(request):
    return render(request,"app/page-mission.html")

def careercyanusPage(request):
    return render(request,"app/page-career.html")                    

def GoldHistoryPage(request):
    all_data = GoldHistory.objects.all()
    return render(request,"app/element-table.html",{'data':all_data})

def MutualFundDataPage(request):
    all_data = MutualFundData.objects.all()
    return render(request,"app/page-mutual.html",{'data':all_data})   


def registrationform(request):
    return render(request,"app/page-register.html")

def pagelogin(request):
    return render(request,"app/page-login.html")    


def inputuser(request):
    return render(request,"app/input-user.html")    


def InputUserData(request):
    pass


def RegisterUser(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    cpass = request.POST['confirmpass']

    if password==cpass:
        newuser = User.objects.create(name=name,email=email,password=password)
        message = "Register SucessFully"
        return render(request,"app/page-login.html",{'msg':message})
    else:
        message = "Password and Confirm Password doesn't match"
        return render(request,"app/page-register.html",{'msg':message})

def LoginUser(request):
    print("=========1=========")
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.get(email=email)
    if user:
        print("=========2=========")
        try:
            if user.password == password:
                print("=========3=========")
                request.session['name'] = user.name
                request.session['email'] = user.email
                request.session['password'] = user.password
                # return render(request,"app/index-gentian-multi.html")
                return redirect('testpage')
            else:
                print("=========4=========")
                message = "Password and Email is wrong"
                return render(request,"app/page-login.html",{'msg':message})
        except Exception as e:
            print("Login Exception : -------->",e)
    else:
        message = "User doesnot exist"
        return render(request,"app/page-login.html",{'msg':message})

