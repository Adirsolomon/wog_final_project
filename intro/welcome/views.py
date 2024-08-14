from django.shortcuts import render, redirect
from django.http import HttpResponse

def welcome(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name.isnumeric():
            return render(request, 'welcome/welcome.html', {'error': "Name should not contain only numbers, please enter a valid name."})
        elif len(name) < 4:
            return render(request, 'welcome/welcome.html', {'error': "Name too short. Make it at least 4 characters."})
        elif len(name) > 7:
            return render(request, 'welcome/welcome.html', {'error': "Name too long! 7 characters max."})
        elif not name.isalnum():
            return render(request, 'welcome/welcome.html', {'error': "No special characters in the name, please."})
        else:
            # Greet the user
            greeting_message = f"Hi {name} and welcome to the World of Games: The Epic Journey"
            # Render the greeting and then redirect to game_picker
            return render(request, 'welcome/welcome.html', {'greeting': greeting_message, 'redirect': True})
    
    return render(request, 'welcome/welcome.html')



