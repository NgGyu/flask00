from app import app, db
from app.models import User, Post

# Shell에서 바로 접근할 수 있게 해주는 함수
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
