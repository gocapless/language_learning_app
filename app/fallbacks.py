from .models import Phrase
from . import db
import random

def get_fallback_phrase(cefr_level=None, topic=None):
    """Fetch a fallback phrase from the database based on CEFR level and topic."""
    try:
        query = Phrase.query
        
        # Filter by CEFR level if provided
        if cefr_level:
            query = query.filter_by(cefr_level=cefr_level)
        
        # Filter by topic if provided
        if topic:
            query = query.filter_by(topic=topic)
        
        # Retrieve unseen phrases first
        unseen_phrases = query.filter_by(seen=False).all()
        if unseen_phrases:
            # Pick a random unseen phrase
            phrase = random.choice(unseen_phrases)
        else:
            # If no unseen phrases, reset all phrases to unseen
            phrases = query.all()
            for p in phrases:
                p.seen = False
            db.session.commit()
            # Pick a random phrase from the reset list
            phrase = random.choice(phrases)
        
        # Mark the phrase as seen and increment seen_count
        phrase.seen = True
        phrase.seen_count += 1
        db.session.commit()

        # Return the fallback phrase text
        return phrase.text
    except Exception as e:
        # Log and return a default fallback phrase in case of an error
        print(f"Error retrieving fallback phrase: {e}")
        return "Desculpe, ocorreu um problema. Tente novamente."
