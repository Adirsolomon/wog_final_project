from django.shortcuts import render

def game_picker(request):
    if request.method == 'POST':
        game_selected = request.POST.get('game_selected')
        level = request.POST.get('level')

        if game_selected in ['1', '2', '3'] and level in ['1', '2', '3', '4', '5']:
            # Handle the game selection logic here
            pass
        else:
            return render(request, 'game_picker.html', {'error': 'Invalid selection. Please try again.'})

    return render(request, 'game_picker.html')

