from django.shortcuts import render, redirect

def game_picker(request):
    if request.method == 'POST':
        game_selected = request.POST.get('game_selected')
        level = request.POST.get('level')

        if game_selected in ['1', '2', '3'] and level in ['1', '2', '3', '4', '5']:
            request.session['level'] = level
            request.session.save()# Save the level in the session
            print(f"Set level to {level} in session")  # Debug print
            if game_selected == '1':  # Assuming '1' corresponds to the memory game
                return redirect('http://localhost:7073/')  # Redirect to memory_game
            elif game_selected == '2':
                return redirect('http://localhost:7074/')
        else:
            return render(request, 'game_picker.html', {'error': 'Invalid selection. Please try again.'})

    return render(request, 'game_picker.html')









