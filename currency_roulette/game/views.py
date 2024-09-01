from django.shortcuts import render, redirect
import random
import requests

def get_currency_rate():
    url = "https://api.freecurrencyapi.com/v1/latest"
    headers = {"apikey": "fca_live_5kFFeonQLtEovyXXfmdYkdghGAYjLw2knZI4sR5V"}
    response = requests.get(url, headers=headers)
    return response.json()["data"]["ILS"]

def play(request):
    level = request.session.get('level')
    if not level:
        return redirect('http://game-picker.local')

    if request.method == 'POST':
        random_number = random.randint(1, 100)
        currency_rate = get_currency_rate()
        result_value = random_number * currency_rate
        allowed_range = 10 - int(level)
        money_interval = list(range(int(result_value - allowed_range), int(result_value + allowed_range)))

        request.session['random_number'] = random_number
        request.session['money_interval'] = money_interval

        return render(request, 'game/start.html', {'level': level, 'random_number': random_number})

    return render(request, 'game/play.html')

def check_guess(request):
    level = request.session.get('level')
    money_interval = request.session.get('money_interval')

    if not level or not money_interval:
        return redirect('http://game-picker.local')

    if request.method == 'POST':
        guess = int(request.POST.get('guess'))
        if guess in money_interval:
            score = request.session.get('score', 0)
            score += int(level) * 5
            request.session['score'] = score
            return render(request, 'game/result.html', {'result': 'You win!', 'score': score})
        else:
            return render(request, 'game/result.html', {'result': 'You lose!'})

    return redirect('play')

def quit_game(request):
    return redirect('http://savegame.local/?next=http://intro.local/')



