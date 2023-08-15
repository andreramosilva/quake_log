from flask import Blueprint, jsonify
from src.app.use_cases.parse_log_file import parse_log_file

def get_game_reports_route():
    game_reports = parse_log_file('games.log')
    return game_reports
