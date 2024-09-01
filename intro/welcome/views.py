from django.shortcuts import render, redirect

def welcome(request):
    if request.method == 'POST':
        # Clear the session data to reset for a new user
        request.session.flush()

        username = request.POST.get('name')
        request.session['username'] = username

        # Validate the username input
        if username.isnumeric():
            return render(request, 'welcome/welcome.html', {'error': "Name should not contain only numbers, please enter a valid name."})
        elif len(username) < 4:
            return render(request, 'welcome/welcome.html', {'error': "Name too short. Make it at least 4 characters."})
        elif len(username) > 7:
            return render(request, 'welcome/welcome.html', {'error': "Name too long! 7 characters max."})
        elif not username.isalnum():
            return render(request, 'welcome/welcome.html', {'error': "No special characters in the name, please."})
        else:
            # Greet the user
            greeting_message = f"Hi {username} and welcome to the World of Games: The Epic Journey"
            # Render the greeting and then redirect to game_picker
            # Generate the absolute URL for the redirect
            game_picker_url = request.build_absolute_uri('http://game-picker.local')
            return render(request, 'welcome/welcome.html', {'greeting': greeting_message, 'redirect': game_picker_url})

    return render(request, 'welcome/welcome.html')




