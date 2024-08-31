from django.shortcuts import render, redirect
import random

def generate_number(difficulty):
    """Generate a random number between 1 and the difficulty level."""
    return random.randint(1, difficulty)

def get_user_guess(request):
    """Retrieve the user's guess from the POST data."""
    guess = request.POST.get('guess')
    if guess and guess.isnumeric():
        return int(guess)
    return None

def play(request):
    if request.method == 'POST':
        # Get the level from the session, which was set by the game picker
        level = request.session.get('level')
        if not level:
            # If level isn't set in session, redirect back to the game picker
            return redirect('http://game-picker.local')
        
        # Generate a random number based on the difficulty level
        random_number = generate_number(int(level))
        request.session['random_number'] = random_number
        request.session['difficulty'] = int(level)  # Store the level in the session

        return render(request, 'game/start.html', {'level': int(level)})
    
    # If GET request, render the play screen
    return render(request, 'game/play.html')

def check_guess(request):
    if request.method == 'POST':
        # Retrieve the necessary information from the session
        level = request.session.get('difficulty')
        random_number = request.session.get('random_number')

        if level is None or random_number is None:
            # Handle the error by either redirecting or showing an error
            return redirect('http://game-picker.local')  # Redirect back to the picker

        # Get the user's guess from the POST data
        user_guess = get_user_guess(request)

        if user_guess is not None and user_guess == random_number:
            # Update the score
            score = request.session.get('score', 0)
            score += (level * 3) + 5
            request.session['score'] = score

            return render(request, 'game/result.html', {'result': 'You win!', 'success': True, 'score': score})
        else:
            return render(request, 'game/result.html', {'result': 'You lose!', 'success': False})

    return redirect('play')

def quit_game(request):
    # Redirect to savegame.local with a parameter indicating a return to intro.local
    return redirect('http://savegame.local/?next=http://intro.local/')



