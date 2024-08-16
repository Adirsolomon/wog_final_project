from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Score  # Assuming you have a UserScore model to save the score

def save_score(request):
    # Retrieve username and score from the session
    username = request.session.get('username')
    score = request.session.get('score')

    # Check if username and score are in the session
    if not username or score is None:
        return HttpResponse("Error: No score data available to save.", status=400)

    # Save the score in the database
    try:
        user_score = Score(username=username, score=score)
        user_score.save()
    except Exception as e:
        return HttpResponse(f"Error: Could not save score. {str(e)}", status=500)

    # Clear the score from the session if needed
    request.session.pop('score', None)

    # Render a confirmation page or redirect to a confirmation page
    return render(request, 'savegame/save_score.html', {'message': f'Score for {username} has been saved successfully!'})


