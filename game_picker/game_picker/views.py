from django.shortcuts import render, redirect

def game_picker(request):
    if request.method == 'POST':
        game_selected = request.POST.get('game_selected')
        level = request.POST.get('level')

        if game_selected in ['memory_game', 'guess_game', 'currency_roulette'] and level in ['1', '2', '3', '4', '5']:
            request.session['level'] = level
            request.session['game_selected'] = game_selected
            print(f"Game: {game_selected}, Level: {level} set in session.")

            game_redirects = {
                'memory_game': 'http://memory-game.local',
                'guess_game': 'http://guess-game.local',
                'currency_roulette': 'http://currency-roulette.local',
            }
            return redirect(game_redirects[game_selected])

        return render(request, 'game_picker.html', {'error': 'Invalid selection. Please try again.'})

    return render(request, 'game_picker.html')













