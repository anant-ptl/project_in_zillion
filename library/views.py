from django.shortcuts import render

# Create your views here.
from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from library.templates import *
from .models import *

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import authenticate,login,logout


from datetime import timedelta
from django.utils import timezone


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return render(request, 'register_page.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return render(request, 'register_page.html')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        if user_type == 'librarian':
            usertype = UserProfile.objects.create(user = user, is_librarian = True)
        else:
            usertype = UserProfile.objects.create(user = user, is_librarian = False)
        usertype.save()
        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login_page')

    return render(request, 'register_page.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        user_type = UserProfile.objects.get(user = user)
        if user is not None:
            login(request, user)
            if user_type.is_librarian:
                return redirect('librarian')
            else:
                return redirect('normal_user')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login_page.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login_page')





# for librarina

@login_required(login_url='login_page')
def librarian_page(request):

    if request.method == 'POST':
        book = request.POST.get('title')
        author = request.POST.get('author')
        copies = request.POST.get('copies')
        created_at = request.POST.get('date')

        if Book.objects.filter(title=book).exists():
            messages.error(request, 'Username already taken')

        user = Book.objects.create(
                title=book,
                author=author,
                total_copies=copies,
                available_copies=copies,
                created_at=created_at
            )
        return redirect('librarian')
    return render(request, "librarian.html")


@login_required(login_url='login_page')
def stock_status(request):
    user = request.user
    print(user)
    books = Book.objects.all()
    selected_book = None

    if request.method == "POST":
        book_title = request.POST.get("book")
        selected_book = Book.objects.get(title=book_title)
    
    return render(request, 'library/stock_status.html', {
        'books': books,
        'selected_book': selected_book,
    })


@login_required(login_url='login_page')
def approved_request(request):
    book_requests = BookRequest.objects.filter(approved=False)
    user = request.user
    print(user)

    if request.method == 'POST':
        request_id = request.POST.get('request_id')
        try:
            book_request = BookRequest.objects.get(id=request_id)

            if book_request.book.available_copies > 0:
                book_request.approved = True
                book_request.book.available_copies -= 1
                book_request.book.save()

                # Set renewal date to 45 days from now
                book_request.renewal_date = (timezone.now() + timedelta(days=45)).date()
                book_request.save()

                messages.success(request, "Book request approved successfully.")
                return redirect('approved_request')
            else:
                messages.error(request, "No available copies to approve this request.")
        except BookRequest.DoesNotExist:
            messages.error(request, "The book request does not exist.")

    return render(request, 'library/approved_request.html', {'book_requests': book_requests})



@login_required(login_url='login_page')
def assign_books(request):
    books = BookRequest.objects.filter(approved = True)
    print(books)

    return render(request, 'library/assign_books.html', {'books' : books})























# for normal user


@login_required(login_url='login_page')
def normal_user(request):
    return render(request, "index.html")


@login_required(login_url='login_page')
def available_books(request):
    books = Book.objects.all()
    user = request.user
    print(user)
    
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        user = request.user
        
        try:
            book = Book.objects.get(title=book_name)
            
            existing_request = BookRequest.objects.filter(user=user, book=book, approved=False).first()
            if existing_request:
                messages.info(request, "You have already requested this book.")
            else:
                BookRequest.objects.create(user=user, book=book)
                messages.success(request, f"Book '{book.title}' has been requested successfully.")
        
        except Exception as e:
            messages.error(request, "An unexpected error occurred. Please try again later.")

    return render(request, 'user_library/available_books.html', {'books': books, 'user':user})


@login_required(login_url='login_page')
def assigned_books(request):
    user = request.user
    books_name = BookRequest.objects.filter(user=user, approved=True)

    return render(request, 'user_library/assigned_books.html', {'books_name': books_name})
