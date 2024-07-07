from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

NBA_STATS_URL = 'https://www.nba.com/stats/players/'

def get_nba_stats(player_name):
    response = requests.get(NBA_STATS_URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the player stats in the HTML
    players_table = soup.find('table', {'class': 'players-list'})
    if not players_table:
        return None

    for row in players_table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        if len(columns) > 0 and player_name.lower() in columns[1].text.lower():
            stats = {
                "player": columns[1].text.strip(),
                "team": columns[2].text.strip(),
                "points_per_game": columns[3].text.strip(),
                "rebounds_per_game": columns[4].text.strip(),
                "assists_per_game": columns[5].text.strip()
            }
            return stats
    return None

@app.route('/')
def home():
    return "Welcome to the NBA Stats API!"

@app.route('/stats/<player_name>')
def stats(player_name):
    data = get_nba_stats(player_name)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Player not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
