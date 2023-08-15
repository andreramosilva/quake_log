from flask import Blueprint, jsonify
from src.app.controllers.game_controller import get_game_reports_route

def create_game_routes():
    game_routes = Blueprint('game_routes', __name__)

    @game_routes.route('/games', methods=['GET'])
    def get_game_reports():
        game_reports = get_game_reports_route()
        return jsonify(game_reports)


    return game_routes
