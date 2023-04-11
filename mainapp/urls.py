from django.urls import path, include
from . import views
from .views import*

urlpatterns = [
    path('', views.home, name='home'),
      path('add_subject/', views.add_subject, name='add_subject'),
        path('add_topic/', views.add_topic, name='add_topic'),
          path('show_subject/', views.show_subject, name='show_subject'),
             path('add_subject/', views.add_subject, name='add_subject'),
                 path('show_topic/<int:id>/', views.show_topic, name='show_topic'),
                   path('info/', views.info, name='info'),
                       path('login/', views.login , name='login'),
                                 path('signup/', views.signup, name='signup'),
                                     path('Userlogout/', views.Userlogout, name='Userlogout'),
                                      path('search/', views.search, name='search'),
                                          path('revision/', views.revision, name='revision'),
                                              path('delete_subject/<int:id>/',views.delete_subject, name='delete_subject'),
                                     
    
]