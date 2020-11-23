from django.urls import path
from.import views

urlpatterns = [
    path('home/',views.home,name='home'), 
    path('contact/',views.contact,name='contact'), 
    path('signup/',views.user_signup,name='signup'),
    path('login/',views.user_login,name='login'),  
    path('logout/',views.user_logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('update/<int:id>/',views.update,name='update'),
    path('add/',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
]