import asyncio
from cs2api import CS2
from ics import Calendar, Event
from datetime import datetime, timedelta, timezone
import json

TEAM_NAME = "Vitality"

async def generate_calendar():
    async with CS2() as cs2:
        print("📡 Recherche de l'équipe...")
        teams = await cs2.search_teams(TEAM_NAME)
        print("DEBUG: Réponse brute API search_teams() :")
        print(json.dumps(teams, indent=4))

        if not teams or 'results' not in teams or len(teams['results']) == 0:
            raise ValueError(f"Équipe {TEAM_NAME} introuvable dans la réponse API.")
        
        team_info = teams['results'][0]
        team_id = team_info['id']
        print(f"✅ Équipe trouvée : {team_info['name']} (ID {team_id})")

        try:
            print("📡 Récupération des matchs à venir...")
            matches = await cs2.get_team_upcoming_matches(team_id)
            print("DEBUG: Réponse brute API get_team_upcoming_matches() :")
            print(json.dumps(matches, indent=4))
        except Exception as e:
            print(f"Erreur lors de la récupération des matchs : {e}")
            matches = {}

        if not matches or 'results' not in matches or len(matches['results']) == 0:
            print("Aucun match à venir trouvé.")
            return

        cal = Calendar()
        base_url = "https://bo3.gg/match/"

        for match in matches['results']:
            event = Event()
            event.name = f"{match['team1']['name']} vs {match['team2']['name']}"

            # Parse start_date ISO8601 string en datetime
            event.begin = datetime.fromisoformat(match['start_date'].replace("Z", "+00:00"))
            # Durée fixée à 1 heure
            event.duration = timedelta(hours=1)
            # URL vers la page du match
            event.url = base_url + match['slug']
            # Description avec nom du tournoi et lien
            event.description = f"Tournoi : {match['tournament']['name']}\nLien : {event.url}"

            cal.events.add(event)

        with open("vitality.ics", "w", encoding="utf-8") as f:
            f.writelines(cal)

        print("✅ Fichier vitality.ics généré.")


if __name__ == "__main__":
    asyncio.run(generate_calendar())