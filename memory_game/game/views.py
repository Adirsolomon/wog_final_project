from django.shortcuts import render, redirect
import random


def generate_sequence(difficulty):
    sequence = [random.randint(1, 101) for _ in range(difficulty)]
    return sequence

def get_user_list(request, difficulty):
    user_input = []
    for i in range(int(difficulty)):
        num = request.POST.get(f'num_{i+1}')
        if num and num.isnumeric():
            user_input.append(int(num))
        else:
            return None  # Invalid input
    return user_input

def play(request):
    if request.method == 'POST':
        # Get the level from the session, which was set by the game picker
        level = request.session.get('level')
        if not level:
            # If level isn't set in session, redirect back to the game picker
            return redirect('http://localhost:7072/')
        
        random_list = generate_sequence(int(level))  # Ensure level is an integer
        request.session['random_list'] = random_list
        request.session['difficulty'] = int(level)  # Ensure level is stored as an integer

        return render(request, 'game/sequence.html', {'sequence': random_list, 'level': int(level)})
    
    # If GET request, redirect to play screen
    return render(request, 'game/play.html')

def check_memory(request):
    if request.method == 'POST':
        level = request.session.get('difficulty')
        
        # Add a check for None level
        if level is None:
            # Handle the error by either redirecting or showing an error
            return redirect('http://localhost:7072/')  # Redirect back to the picker
            
        random_list = request.session.get('random_list')
        user_list = get_user_list(request, level)
        
        if user_list and user_list == random_list:
            # Update score
            score = request.session.get('score', 0)
            score += (level * 3) + 5
            request.session['score'] = score

            return render(request, 'game/result.html', {'result': 'You win!', 'success': True, 'score': score})
        else:
            return render(request, 'game/result.html', {'result': 'You lose!', 'success': False})

    return redirect('play')

def quit_game(request):
    # Redirect to save_game app to save the score
    return redirect('http://localhost:7071/')




