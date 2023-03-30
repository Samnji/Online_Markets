from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email'] 
        password1 = request.POST['password1'] 
        password2 = request.POST['password1'] 

        # First check if the password are matching
        if password1 == password2:
            # Check if the username provided exists
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('signup')

            else:
                # Checking for password strength before saving the data
                score = 0
                length = 0
                lower = False
                upper = False
                number = False
                symbol = False
                numbers = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
                symbols = [ '!', '£', '$', '%', '&', '<', '*', '@', '#', '^']

                if len(password1) >= 8:
                    length = True

                for item in password1:
                    if item.islower():
                        lower = True

                    elif item.isupper():
                        upper = True

                    elif item in numbers:
                        number = True

                    elif item in symbols:
                        symbol = True

                if length:
                    score = score + 1

                if lower:
                    score = score + 1

                if upper:
                    score = score + 1


                if number:
                    score = score + 1

                if symbol:
                    score = score + 1


                context['score'] = score


                if score == 1 or score == 2:
                    messages.info(request, f"""Weak password, 
                        You password strength score is: {score}/5""")
                    return redirect('create')

                elif score == 3 or score == 4:
                    messages.info(request, "This password could be improved.")
                    return redirect('create')

                elif score == 5:
                    # Saving the data
                    user = Users.objects.create_user(username=username, email=email, password=password)
                    
                    return redirect('signin')
        else:
            messages.info('Password Not Matching')
            
            return redirect('signup')             

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email'] 
        password = request.POST['password']

        username_exists = auth.authenticate(username=username, password=password)
        email_exists = auth.authenticate(email=email, password=password)

        if username_exists:
            auth.login(request, username_exists)
            
            return redirect('home')

        if  email_exists:
            auth.login(request, email_exists)

            return redirect('home')

        else:
            messages.info(request, "Invalid Credentials")

            return redirect('signin')

    return render(request, 'signin.html')

def logout(request):
    auth.logout(request)

    return redirect('home')

def forgot_pass(request):
    return render(request, 'forgot_pass.html')

def change_pass(request):
    return render(request, 'change_pass.html')
