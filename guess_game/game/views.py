from django.shortcuts import render, redirect
import random

def generate_number(level):
    return random.randint(1, int(level))

def play(request):
    level = request.session.get('level')
    if not level:
        return redirect('http://game-picker.local')

    if request.method == 'POST':
        number = generate_number(level)
        request.session['number'] = number
        return render(request, 'game/start.html', {'level': level})

    return render(request, 'game/play.html')

def check_guess(request):
    level = request.session.get('level')
    number = request.session.get('number')

    if not level or not number:
        return redirect('http://game-picker.local')

    if request.method == 'POST':
        user_guess = int(request.POST.get('guess'))
        if user_guess == number:
            score = request.session.get('score', 0)
            score += int(level) * 5
            request.session['score'] = score
            return render(request, 'game/result.html', {'result': 'You win!', 'score': score})
        else:
            return render(request, 'game/result.html', {'result': 'You lose!'})

    return redirect('play')

def quit_game(request):
    return redirect('http://savegame.local/?next=http://intro.local/')


