from src.interfaces.api.game_routes import create_game_routes
from flask import Flask

app = Flask(__name__)

# Register API routes
app.register_blueprint(create_game_routes())

if __name__ == '__main__':
    app.run(debug=True)
