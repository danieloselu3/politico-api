from app.main import main

@main.route('/')
def index():
    return "hello Dan, You can do this."