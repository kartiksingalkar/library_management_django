from django.urls import path
from django.contrib import admin
from libraryapp import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('signup/',views.SignupPage, name='signup'),
    path('',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('home/',views.home, name='home'),
    path('add-book/',views.add_book, name='add_book'),
    path('delete_book/<int:book_id>',views.delete_book, name='delete_book'),
    path('view_book/<int:id>',views.view_book, name='view_book'),
    path('update_book/<int:book_id>',views.update_book, name='update_book'),
    path('save_update_book/<int:book_id>',views.save_update_book, name='save_update_book'),


]