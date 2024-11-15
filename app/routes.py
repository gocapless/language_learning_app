from flask import Blueprint, jsonify, request, render_template
from . import db
from .models import Phrase
from .api import generate_phrase
from .fallbacks import get_fallback_phrase
from .utils import generate_audio

main = Blueprint('main', __name__)

@main.route('/phrase', methods=['GET'])
def get_phrase():
    """
    Handle the 'Next' button functionality.
    Dynamically generate a phrase or use a fallback from the database.
    """
    # Get user preferences for CEFR level and topic from query parameters
    cefr_level = request.args.get('cefr_level')
    topic = request.args.get('topic')

    # Attempt to generate a new phrase using OpenAI API
    phrase_text = generate_phrase(cefr_level, topic)
    
    if phrase_text:
        # Save the generated phrase to the database
        new_phrase = Phrase(
            text=phrase_text,
            cefr_level=cefr_level,
            topic=topic,
            seen=False,
            seen_count=0
        )
        db.session.add(new_phrase)
        db.session.commit()

        # Generate audio for the phrase
        audio_filename = generate_audio(new_phrase.id, new_phrase.text)
    else:
        # Use a fallback phrase if API call fails
        fallback_phrase = get_fallback_phrase(cefr_level, topic)
        audio_filename = generate_audio(fallback_phrase.id, fallback_phrase.text)
        phrase_text = fallback_phrase.text

    # Return the phrase and audio path as a JSON response
    return jsonify({"phrase": phrase_text, "audio": audio_filename})


@main.route('/', methods=['GET'])
def index():
    """
    Render the main page with the interface for selecting CEFR level and topic.
    """
    return render_template('index.html')

