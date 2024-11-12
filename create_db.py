from app import create_app, db
from app.models import Phrase

app = create_app()

with app.app_context():
    # Create tables in the database
    db.create_all()

    # Insert sample phrases if the table is empty
    if Phrase.query.count() == 0:
        sample_phrases = [
            "Bom dia!",
            "Como estás?",
            "Qual é o teu nome?",
            "Onde fica a estação?",
            "Preciso de ajuda.",
        ]
        for text in sample_phrases:
            new_phrase = Phrase(text=text)
            db.session.add(new_phrase)
        db.session.commit()
