from django.shortcuts import render, redirect
import random

def generate_sequence(level):
    return [random.randint(1, 101) for _ in range(int(level))]

def play(request):
    level = request.session.get('level')
    if not level:
        print("Level not found in session, redirecting to game-picker")
        return redirect('http://game-picker.local')

    if request.method == 'POST':
        sequence = generate_sequence(level)
        request.session['sequence'] = sequence
        return render(request, 'game/sequence.html', {'sequence': sequence, 'level': level})

    return render(request, 'game/play.html')

def check_memory(request):
    level = request.session.get('level')
    sequence = request.session.get('sequence')

    if not level or not sequence:
        print("Level or sequence not found in session, redirecting to game-picker")
        return redirect('http://game-picker.local')

    if request.method == 'POST':
        user_sequence = [int(request.POST.get(f'num_{i+1}')) for i in range(int(level))]
        if user_sequence == sequence:
            score = request.session.get('score', 0)
            score += int(level) * 5
            request.session['score'] = score
            return render(request, 'game/result.html', {'result': 'You win!', 'score': score})
        else:
            return render(request, 'game/result.html', {'result': 'You lose!'})

    return redirect('play')

def quit_game(request):
    return redirect('http://savegame.local/?next=http://intro.local/')








