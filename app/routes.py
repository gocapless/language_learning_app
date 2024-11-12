from flask import Blueprint, jsonify, render_template
from . import db
from .models import Phrase
from .utils import generate_audio
import random

main = Blueprint('main', __name__)

@main.route('/phrase', methods=['GET'])
def get_phrase():
    unseen_phrases = Phrase.query.filter_by(seen=False).all()
    if unseen_phrases:
        phrase = random.choice(unseen_phrases)
    else:
        phrases = Phrase.query.all()
        for p in phrases:
            p.seen = False
        db.session.commit()
        phrase = random.choice(phrases)
    
    phrase.seen = True
    phrase.seen_count += 1
    db.session.commit()

    audio_filename = generate_audio(phrase.id, phrase.text)

    return jsonify({"phrase": phrase.text, "audio": audio_filename})

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')
