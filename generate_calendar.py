import asyncio
from cs2api import CS2
from ics import Calendar, Event
from datetime import datetime, timezone
import json

TEAM_NAME = "Vitality"

async def generate_calendar():
    async with CS2() as cs2:
        teams = await cs2.search_teams(TEAM_NAME)
        print("DEBUG teams raw response:")
        print(json.dumps(teams, indent=4))

        if not teams or 'results' not in teams or len(teams['results']) == 0:
            raise ValueError(f"Équipe {TEAM_NAME} introuvable dans la réponse API.")
        
        team_info = teams['results'][0]
        team_id = team_info['id']
        print(f"Team ID found: {team_id} ({team_info['name']})")

        try:
            matches = await cs2.get_team_upcoming_matches(team_id)
            print("DEBUG upcoming matches raw response:")
            print(json.dumps(matches, indent=4))
        except Exception as e:
            print(f"Erreur lors de la récupération des matchs : {e}")
            matches = []

        if not matches:
            print("Aucun match à venir trouvé.")
            return

        cal = Calendar()
        for match in matches:
            event = Event()
            event.name = f"{match['team1']['name']} vs {match['team2']['name']}"
            start_time = datetime.fromtimestamp(match['date'] / 1000, tz=timezone.utc)
            event.begin = start_time
            event.url = match.get('match_page', '')
            event.description = f"Tournoi : {match['tournament']['name']}\nLien : {match.get('match_page', '')}"
            cal.events.add(event)

        with open("vitality.ics", "w", encoding="utf-8") as f:
            f.writelines(cal)
        print("✅ Fichier vitality.ics généré")


if __name__ == "__main__":
    asyncio.run(generate_calendar())