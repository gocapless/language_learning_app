import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'phrases.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
GOOGLE_APPLICATION_CREDENTIALS = "/home/ec2-user/ai-language-basics-2aaf2c68f906.json"
