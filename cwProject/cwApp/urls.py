from django.urls import path
from . import views

urlpatterns=[

path('alcohol/',views.alcohol,name="alcohol"), #Path to the 2nd exercise for the list of drinks
path('drinkInfo/<int:drinkID>/',views.drinkInfo,name='drinkContent'),  #gets info and list

#Page for exercise 1
path('exercise1/',views.exercise1,name="page1"),

#Website pages
path('home/<str:oldName>/',views.Home,name='home'),
path('page2/<str:oldName>/',views.page2,name="page2"),
path('page3/<str:oldName>/',views.page3,name="page3"),
path('page4/<str:oldName>/',views.page4,name="page4"),
path('page5/<str:oldName>/',views.page5,name="page5"),
]