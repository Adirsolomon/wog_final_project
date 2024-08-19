from django.shortcuts import render, redirect
from django.http import HttpResponse
from scores.models import Player  # Correcting the model import

def save_score(request):
    # Retrieve username and score from the session
    username = request.session.get('username')
    score = request.session.get('score')

    # Check if username is in the session
    if not username:
        return HttpResponse("Error: No username found in session.", status=400)

    # Check if score is None
    if score is None:
        # Score might have already been saved, or no score exists in session
        return render(request, 'savegame/success.html', {'message': f'No new score to save for {username}.'})

    # Save the score in the database
    try:
        # Check if the player already exists
        player, created = Player.objects.get_or_create(name=username)
        player.score += score  # Add the new score to the existing score
        player.save()
    except Exception as e:
        return HttpResponse(f"Error: Could not save score. {str(e)}", status=500)

    # Clear the score from the session after saving
    request.session.pop('score', None)

    # Render the success page and redirect to intro after confirmation
    return render(request, 'savegame/success.html', {'message': f'Score for {username} has been saved successfully!'})

def save_and_restart(request):
    # Save the score first
    save_score(request)
    # Clear the session and redirect to the intro page to start over
    request.session.flush()
    return redirect('http://localhost:7070/')  # Redirect to the intro app





