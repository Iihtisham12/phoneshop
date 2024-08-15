from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.indexPage, name="IndexPage"),
    path('edit/<int:id>/', views.editData, name="EditData"),
    path('delete/<int:id>/', views.deleteData, name="DeletetData"),
    path('singup/', views.singUp, name="SingUpPage"),
    path('', views.loGinPage, name="LoginPage"),
    path('logout/', views.logoutMethod, name="LogoutMethod"),
    path('changepass/', views.change_password, name="ChangePass"),
]
