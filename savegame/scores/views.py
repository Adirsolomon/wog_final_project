from django.shortcuts import render, redirect
from django.http import HttpResponse
from scores.models import Player  # Correcting the model import

def save_score(request):
    # Retrieve username and score from the session
    username = request.session.get('username')
    score = request.session.get('score')

    # Check if username and score are in the session
    if not username or score is None:
        return HttpResponse("Error: No score data available to save.", status=400)

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




