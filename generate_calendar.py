from cs2api import BO3API
from ics import Calendar, Event
from datetime import datetime, timezone

TEAM_NAME = "Vitality"  # Nom exact de l'équipe

api = BO3API()

# Recherche de l'ID de l'équipe
teams = api.search_teams(TEAM_NAME)
if not teams:
    raise ValueError(f"Équipe {TEAM_NAME} introuvable.")
team_id = teams[0]["id"]

# Récupération des matchs à venir
matches = api.get_team_upcoming_matches(team_id)

cal = Calendar()

for match in matches:
    event = Event()
    event.name = f"{match['team1']['name']} vs {match['team2']['name']}"
    
    start_time = datetime.fromtimestamp(match['date'] / 1000, tz=timezone.utc)
    event.begin = start_time
    event.url = match['match_page']
    event.description = f"Tournoi : {match['tournament']['name']}\nLien : {match['match_page']}"
    
    cal.events.add(event)

with open("vitality.ics", "w", encoding="utf-8") as f:
    f.writelines(cal)

print("✅ Fichier vitality.ics généré")
