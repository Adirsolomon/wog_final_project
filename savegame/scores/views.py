from django.shortcuts import render, redirect
from django.http import HttpResponse
from scores.models import Player  # Correcting the model import

def save_score(request):
    # Retrieve username and score from the session
    username = request.session.get('username')
    score = request.session.get('score')

    # Check if username and score are in the session
    if not username:
        return HttpResponse("Error: No username found in session.", status=400)

    if score is None:
        # Score might have already been saved, or no score exists in session
        # Check if we need to display a message or redirect the user
        return render(request, 'savegame/save_score.html', {'message': f'No new score to save for {username}.'})

    # Save the score in the database
    try:
        # Check if the player already exists
        player, created = Player.objects.get_or_create(name=username)
        player.score += score  # Add the new score to the existing score
        player.save()
    except Exception as e:
        return HttpResponse(f"Error: Could not save score. {str(e)}", status=500)

    # Clear the score from the session if needed
    request.session.pop('score', None)

    # Render a confirmation page or redirect to a confirmation page
    return render(request, 'savegame/save_score.html', {'message': f'Score for {username} has been saved successfully!'})




