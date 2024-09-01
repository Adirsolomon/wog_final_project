from django.shortcuts import render, redirect
import random

def generate_sequence(level):
    """Generate a sequence of random numbers based on the difficulty level."""
    sequence = [random.randint(1, 101) for _ in range(level)]
    return sequence

def get_user_list(request, level):
    """Retrieve the user's input list based on the difficulty level."""
    user_input = []
    for i in range(level):
        num = request.POST.get(f'num_{i+1}')
        if num and num.isnumeric():
            user_input.append(int(num))
        else:
            return None  # Invalid input
    return user_input

def play(request):
    if request.method == 'POST':
        # Get the level from the session
        level = request.session.get('level')
        if not level:
            # If level isn't set in session, redirect back to the game picker
            return redirect('http://game-picker.local')
        
        # Generate a sequence and store it in the session
        random_list = generate_sequence(int(level))
        request.session['random_list'] = random_list

        # Proceed to the sequence view
        return render(request, 'game/sequence.html', {'sequence': random_list, 'level': int(level)})
    
    # If GET request, show the play screen
    return render(request, 'game/play.html')

def check_memory(request):
    if request.method == 'POST':
        level = request.session.get('level')  # Get level directly from session
        random_list = request.session.get('random_list')
        user_list = get_user_list(request, int(level))
        
        if user_list and user_list == random_list:
            # Update score
            score = request.session.get('score', 0)
            score += (int(level) * 3) + 5
            request.session['score'] = score

            return render(request, 'game/result.html', {'result': 'You win!', 'success': True, 'score': score})
        else:
            return render(request, 'game/result.html', {'result': 'You lose!', 'success': False})

    return redirect('play')

def quit_game(request):
    # Redirect to savegame.local with a parameter indicating a return to intro.local
    return redirect('http://savegame.local/?next=http://intro.local/')







