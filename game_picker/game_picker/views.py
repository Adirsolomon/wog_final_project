from django.shortcuts import render, redirect

def game_picker(request):
    if request.method == 'POST':
        game_selected = request.POST.get('game_selected')
        level = request.POST.get('level')

        if game_selected in ['memory_game', 'guess_game', 'currency_roulette'] and level in ['1', '2', '3', '4', '5']:
            request.session['level'] = level
            request.session.save()  # Save the level in the session
            print(f"Set level to {level} in session")  # Debug print
            if game_selected == 'memory_game':  # Redirect to memory_game
                return redirect('http://localhost:7073/')
            elif game_selected == 'guess_game':  # Redirect to guess_game
                return redirect('http://localhost:7074/')
            elif game_selected == 'currency_roulette':  # Redirect to currency_roulette
                return redirect('http://localhost:7075/')
        else:
            return render(request, 'game_picker.html', {'error': 'Invalid selection. Please try again.'})

    return render(request, 'game_picker.html')










