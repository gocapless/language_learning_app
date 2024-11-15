from . import db

class Phrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(150), nullable=False)
    seen = db.Column(db.Boolean, default=False)
    seen_count = db.Column(db.Integer, default=0)
    cefr_level = db.Column(db.String(10), nullable=True)  # New field for CEFR level
    topic = db.Column(db.String(50), nullable=True)       # New field for topic

