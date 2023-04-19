from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Books



# login
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'library/signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrec")

    return render (request,'library/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


# Home
@login_required(login_url='login')
def add_book(request):
    if request.method=='POST':
        # print('working')
        id_var = request.POST.get('book_id')
        book_title = request.POST.get('title')
        book_author = request.POST.get('author')
        book_publisher = request.POST.get('publisher')
        book_summary = request.POST.get('summary')
        b=Books()
        b.book_id = id_var
        b.title=book_title
        b.author=book_author
        b.publisher=book_publisher
        b.summary=book_summary
        b.save()
        print(b,'b')
        return redirect('/home/')

    return render (request,'library/add_book.html')

@login_required(login_url='login')
def home(request):
    books = Books.objects.all()
    # print(books)
    return render (request,'library/home.html',{'books':books}
)

@login_required(login_url='login')
def view_book(request,id):
    view = Books.objects.get(book_id=id)
    return render (request,'library/view_book.html',{'view':view})

@login_required(login_url='login')
def update_book(request,book_id):
    update=Books.objects.get(book_id=book_id)
    return render(request,'library/update_book.html',{'update':update})

@login_required(login_url='login')
def save_update_book(request,book_id):
        save_book_id = request.POST.get('book_id')
        save_book_title = request.POST.get('title')
        save_book_author = request.POST.get('author')
        save_book_publisher = request.POST.get('publisher')
        save_book_summary = request.POST.get('summary')
        
        update = Books.objects.filter(book_id=book_id).update(book_id=save_book_id,
                                                              title=save_book_title,
                                                              author=save_book_author,
                                                              publisher=save_book_publisher,
                                                              summary= save_book_summary
                                                              )

        # print(update.title,"update")
        # update.book_id = save_book_id
        # update.title=save_book_title
        # update.author=save_book_author
        # update.publisher=save_book_publisher
        # update.summary=save_book_summary
        # print(update.book_id,"ooo")
        # update.save()

        return redirect('/home/')

@login_required(login_url='login')
def delete_book(request,book_id):
    b=Books.objects.get(book_id=book_id)
    b.delete()
    return redirect('/home/')