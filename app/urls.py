from django import views
from django.urls import path,include
from . import views
urlpatterns = [
    path("testpage/",views.TestPage,name="testpage"),
    path("about/",views.aboutusbasePage,name="page-about.html"),
    path("aboutuslinumpage/",views.aboutuslinumPage,name="page-about-v2.html"),
    path("aboutuscyanuspage/",views.aboutuscyanusPage,name="page-about-v3.html"),
    path("ourteampage/",views.ourteamsPage,name="page-team.html"),
    path("walletv1page/",views.walletv1Page,name="page-wallets.html"),
    path("walletv2page/",views.walletv2Page,name="page-wallets-v2.html"),
    path("featurespage/",views.featuresPage,name="page-features.html"),
    path("tokensalespage/",views.tokansalesPage,name="page-token-sale.html"),
    path("roadmappage/",views.roadmapPage,name="page-roadmap.html"),
    path("downloadpage/",views.downloadPage,name="page-download.html"),
    path("faqspage/",views.faqsPage,name="page-faq.html"),
    path("contactbasepage/",views.contactbasePage,name="page-contact.html"),
    path("contactcyanuspage/",views.contactcyanusPage,name="page-contact-v2.html"),
    path("exchangecyanuspage/",views.exchangecyanusPage,name="page-exchange.html"),
    path("partnercyanuspage/",views.partnercyanusPage,name="page-partner.html"),
    path("carrercyuspage/",views.careercyanusPage,name="page-career.html"),  
    path("goldhistroypage/",views.GoldHistoryPage,name="goldhistorypage"),
    path("mutualfundpage/",views.MutualFundDataPage,name="mutualfundpage"),
    path("registrationform/",views.registrationform,name="page-register.html"),
    path("inputuser/",views.inputuser,name="input-user.html"),
    path("loginpage/",views.pagelogin,name="page-login.html"),



    ###################### Functionality URLS###########################
    path("registeruser/",views.RegisterUser,name="regsister"),
    path("loginuser/",views.LoginUser,name="loginuser"),
    

    

]
