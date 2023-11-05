from django.urls import path
from . import views
from .views import register,login_user,logout_user
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>', views.view_student, name='view_student'),
  path('add/', views.add, name='add'),
  path('edit/<int:id>/', views.edit, name='edit'),
  path('delete/<int:id>/', views.delete, name='delete'),
  path("register/",register, name="register"),
  path("login_user/",login_user, name="login_user"),
  path("logout_user/",logout_user, name="logout_user"),
  path('root/',views.root , name='root')
   
]
