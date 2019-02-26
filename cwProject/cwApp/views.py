from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Cocktail
from .models import Page

#List of drinks
def alcohol(request):
    allDrinks= Cocktail.objects.all()
    context={
        'drinks':allDrinks
    }
    return render(request,'cwApp/Menu.html',context)
#Individual drinks
def drinkInfo(request,drinkID):
    whichDrink= get_object_or_404(Cocktail,pk=drinkID)
    context={
        'drinkName':whichDrink
    }
    return render(request,'cwApp/drinkName.html',context)


def exercise1(request):    #Placeholder page so It can go to a website
    allPages=Page.objects.all()
    content={
       'allPages':"None"
   }
    return render(request,'cwApp/Placeholder.html',content)

def Home(request,oldName):
    allPages=Page.objects.all()
    previous=oldName
    content={
        'allPages':allPages[0].name,
        'previous':previous
    }
    return render(request,'cwApp/Home.html',content)

def page2(request,oldName):
    allPages=Page.objects.all()
    previous=oldName
    content={
    'allPages':allPages[1].name,
    'previous':previous
    }
    return render(request,'cwApp/Page2.html',content)

def page3(request,oldName):
    allPages=Page.objects.all()
    previous=oldName
    content={
        'allPages':allPages[2].name,
        'previous':previous
    }
    return render(request,'cwApp/Page3.html',content)

def page4(request,oldName):
    allPages=Page.objects.all()
    previous=oldName
    content={
    'allPages':allPages[3].name,
    'previous':previous
    }
    return render(request,'cwApp/Page4.html',content)
def page5(request,oldName):
    allPages=Page.objects.all()
    previous=oldName
    content={
    'allPages':allPages[4].name,
    'previous':previous
    }
    return render(request,'cwApp/Page5.html',content)