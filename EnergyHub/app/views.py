from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password , check_password
from django.contrib.auth import logout
from .models import User
from .forms import Signup ,Signin 
from django.contrib import messages
# Create your views here.

def userView(req):
    return render(req,'index.html')

def signupView(request):
    if request.method == 'POST':
        form = Signup(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user_exists = User.objects.filter(email=email).exists()

            if user_exists:
                return render(request, 'index.html', {'signup_errors': 'Email already registered'})
            

            hashed_password = make_password(password)
            user = User(name=name, email=email, password=hashed_password)
            user.save()

            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            request.session['user_email'] = user.email


            return redirect('main')
        else:
            return render(request, 'index.html', {'signup_errors': form.errors})
    else:
        return render(request, 'index.html')

def signinView(request):
    if request.method == 'POST':
        form = Signin(request.POST)

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.filter(email=email)
            
            if user.exists():
                user_obj = user.first()

                if check_password(password, user_obj.password):
                    
                    request.session['user_id'] = user_obj.id
                    request.session['user_name'] = user_obj.name
                    request.session['user_email'] = user_obj.email
                    
                    return redirect('main')
                else:
                    return render(request, 'index.html', {'signin_errors': 'Wrong password'})
            else:
                return render(request, 'index.html', {'signin_errors': 'Email not found'})
        else:
            return render(request, 'index.html', {'signup_errors': form.errors})
    else:
        return render(request, 'index.html')

def mainView(request):
    if 'user_id' in request.session:
        user_name = request.session.get('user_name')
        return render(request,'main.html', {'user_name': user_name})
    else:
        return redirect('index')

def logoutView(request):
    if request.method == 'POST':
        request.session.flush()
        return redirect('index')
    else:
        return render(request, 'logout.html')

def energy_view(request):
    """Energy Solutions page"""
    if 'user_id' not in request.session:
        return redirect('index')
    user_name = request.session.get('user_name')
    return render(request, 'energy.html', {'user_name': user_name})

def gas_view(request):
    """Gas Solutions page"""
    if 'user_id' not in request.session:
        return redirect('index')
    user_name = request.session.get('user_name')
    return render(request, 'gas.html', {'user_name': user_name})

def power_view(request):
    """Power Generation page"""
    if 'user_id' not in request.session:
        return redirect('index')
    user_name = request.session.get('user_name')
    return render(request, 'power.html', {'user_name': user_name})

def sustainability_view(request):
    """Sustainability page"""
    if 'user_id' not in request.session:
        return redirect('index')
    user_name = request.session.get('user_name')
    return render(request, 'sustainability.html', {'user_name': user_name})

def resources_view(request):
    """Resources page"""
    if 'user_id' not in request.session:
        return redirect('index')
    user_name = request.session.get('user_name')
    return render(request, 'resources.html', {'user_name': user_name})

def contact_view(request):
    """Contact page"""
    if 'user_id' not in request.session:
        return redirect('index')
    user_name = request.session.get('user_name')
    
    if request.method == 'POST':
        # Handle contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # TODO: Save to database or send email
        # For now, just render the page with success message
        return render(request, 'contact.html', {
            'user_name': user_name,
            'success': 'Message sent successfully!'
        })
    
    return render(request, 'contact.html', {'user_name': user_name})

def support_view(request):
    """Support page"""
    if 'user_id' not in request.session:
        return redirect('index')
    user_name = request.session.get('user_name')
    return render(request, 'support.html', {'user_name': user_name})

# Similar for other pages...
# Similar for other pages...
# Similar for other pages...