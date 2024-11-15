from app import create_app, db

app = create_app()

with app.app_context():
    # Create tables in the database
    db.create_all()

