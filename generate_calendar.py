import asyncio
from cs2api import CS2
from ics import Calendar, Event
from datetime import datetime, timezone

TEAM_NAME = "Vitality"

async def generate_calendar():
    async with CS2() as cs2:
        teams = await cs2.search_teams(TEAM_NAME)
        print("DEBUG teams:", teams)  # Pour debug la structure
        
        if not teams:
            raise ValueError(f"Équipe {TEAM_NAME} introuvable.")
        
        # Récupérer le premier ID dans le dictionnaire
        team_id = list(teams.keys())[0]
        
        matches = await cs2.get_team_upcoming_matches(team_id)
        
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


if __name__ == "__main__":
    asyncio.run(generate_calendar())