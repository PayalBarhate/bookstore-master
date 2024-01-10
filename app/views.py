from typing import List
from django.contrib import messages
from django.shortcuts import redirect, render
from.models import Product , Upcoming , Contact, Orders, Category, Slider, Testimonials, Working
from django.contrib.auth.models import User,auth
import random
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Q
from django.core import mail
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def index(request):
    product = Product.objects.all()
    upcoming = Upcoming.objects.all()
    category = Category.objects.all()
    slider = Slider.objects.all()
    category_id = request.GET.get('category')
    if category_id :
        product = Product.objects.filter(category = category_id)
    return render(request, 'index.html',{'product' : product,'upcoming' : upcoming, 'category' : category, 'slider' : slider })

def shop(request):
    product = None
    price_LTH = request.GET.get('PRICE_LTH')
    price_HTL = request.GET.get('PRICE_HTL')
    if price_LTH:
        product = Product.objects.filter().order_by('Price')
    elif price_HTL:
        product = Product.objects.filter().order_by('-Price')
    
    else:
        product = Product.objects.all()
    category = Category.objects.all()
    category_id = request.GET.get('category')
    print(category_id)
    if category_id :
        product = Product.objects.filter(category = category_id)
    return render(request, 'shop.html',{'product' : product, 'category' : category})


def about(request):
    working = Working.objects.all()
    testimonials = Testimonials.objects.all()
    return render(request, 'about.html',{'testimonials' : testimonials, 'working': working })

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone', '')
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')

        contact = Contact(name=name,email=email,subject=subject,message=message,phone=phone)
        contact.save()
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def product(request,myid):
    items = list(Product.objects.all())
    relatedproduct = random.sample(items,4)
    product = Product.objects.filter(id=myid)
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zipcode = request.POST.get('zipcode', '')
        phone = request.POST.get('phone', '')
        book = request.POST.get('book', '')
        price = request.POST.get('price', '')

        order = Orders(name=name, email=email, City=city, Address=address, Zip_code=zipcode, State=state, phone=phone, Book=book, price=price)
        order.save()
        id = order.id
        subject = "congralation for buying the game"  
        html_message = render_to_string('bill.html',{'name': name, 'id':id, 'phone': phone,'email': email,'book': book,'price': price})
        plain_message = strip_tags(html_message)
        to      =  email
        mail.send_mail(subject, plain_message, settings.EMAIL_HOST_USER,[to], html_message=html_message)
        

    return render(request, 'product.html',{'product' : product[0],'relatedproduct':relatedproduct})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            request.session['user_id'] = user.id
            request.session['email'] = user.email
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
       username = request.POST['username']
       password1 = request.POST['password']
       password2 = request.POST['password1']
       email = request.POST['email']

       if password1 == password2:
           if User.objects.filter(username=username).exists():
               messages.info(request,'name Taken')
               return redirect('login')
           elif User.objects.filter(email=email).exists():
               messages.info(request,'Email Taken')
               return redirect('login')
           else:
               user = User.objects.create_user(username=username, password=password1, email=email)
               user.save();
               subject = "Greetings"  
               msg     = " THANK YOU FOR VISITING OUT BOOK STORE "  
               to      = user.email
               res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
               
               print('user created')
               return redirect('login')
       else:
           messages.info(request, 'password not matching')
           return redirect('home')

       return redirect('/')
def logout(request):
    auth.logout(request)
    return redirect('/')


def search(request):
    if request.method == "POST":
        search = request.POST.get('search')
        product = Product.objects.filter(Q(Name__contains=search) | Q(category__Name__icontains=search))
        return render(request, 'search.html', {'search':search,'product':product})
    else:
        return render(request, 'search.html')
def bill(request):
    return render(request, 'bill.html')