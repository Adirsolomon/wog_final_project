from django.shortcuts import render, redirect
import random
import requests
from django.http import HttpResponse

def get_currency_rate():
    url = "https://api.freecurrencyapi.com/v1/latest"
    headers = {"apikey": "fca_live_5kFFeonQLtEovyXXfmdYkdghGAYjLw2knZI4sR5V"}
    resp = requests.get(url, headers=headers)
    data = resp.json()
    return data["data"]["ILS"]

def get_money_interval(difficulty):
    random_number = random.randint(1, 100)
    current_rate = get_currency_rate()
    correct_answer = random_number * current_rate
    allowed_range = 10 - difficulty
    # Convert range to list to avoid JSON serialization issue
    money_interval = list(range(int(correct_answer-allowed_range), int(correct_answer+allowed_range)))
    return money_interval, random_number

def play(request):
    if request.method == 'POST':
        level = request.session.get('level')
        if not level:
            return redirect('http://localhost:7072/')

        money_interval, random_number = get_money_interval(int(level))
        # Store list instead of range in session
        request.session['money_interval'] = money_interval
        request.session['random_number'] = random_number
        request.session['difficulty'] = int(level)

        return render(request, 'game/start.html', {'level': int(level), 'random_number': random_number})
    
    return render(request, 'game/play.html')

def check_guess(request):
    if request.method == 'POST':
        level = request.session.get('difficulty')
        money_interval = request.session.get('money_interval')

        if level is None or money_interval is None:
            return redirect('http://localhost:7072/') 

        user_guess = request.POST.get('guess')
        if user_guess and user_guess.isnumeric():
            user_guess = int(user_guess)
            if user_guess in money_interval:
                score = request.session.get('score', 0)
                score += (level * 3) + 5
                request.session['score'] = score

                return render(request, 'game/result.html', {'result': 'You win!', 'success': True, 'score': score})
            else:
                return render(request, 'game/result.html', {'result': 'You lose!', 'success': False})

    return redirect('play')

def quit_game(request):
    # Redirect to save_game with a parameter indicating a return to intro
    return redirect('http://localhost:7071/?next=intro')



