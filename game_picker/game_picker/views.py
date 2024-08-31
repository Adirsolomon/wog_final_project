from django.shortcuts import render, redirect

def game_picker(request):
    if request.method == 'POST':
        game_selected = request.POST.get('game_selected')
        level = request.POST.get('level')

        # Check if the game and level are valid selections
        if game_selected in ['memory_game', 'guess_game', 'currency_roulette'] and level in ['1', '2', '3', '4', '5']:
            request.session['level'] = level
            request.session.save()  # Save the level in the session
            print(f"Set level to {level} in session")  # Debug print
            
            # Redirect based on the selected game
            if game_selected == 'memory_game':  
                return redirect('http://memory-game.local')
            elif game_selected == 'guess_game':  
                return redirect('http://guess-game.local')
            elif game_selected == 'currency_roulette':  
                return redirect('http://currency-roulette.local')
        else:
            return render(request, 'game_picker.html', {'error': 'Invalid selection. Please try again.'})

    return render(request, 'game_picker.html')











