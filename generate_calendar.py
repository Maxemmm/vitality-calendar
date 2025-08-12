import asyncio
from cs2api import CS2
from ics import Calendar, Event
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import json
import os

TEAM_NAME = "Vitality"
TIMEZONE = ZoneInfo("Europe/Paris")  # Change selon ton fuseau

async def generate_calendar():
    async with CS2() as cs2:
        # Recherche de l'équipe
        teams = await cs2.search_teams(TEAM_NAME)
        if not teams or 'results' not in teams or not teams['results']:
            raise ValueError(f"Équipe {TEAM_NAME} introuvable.")
        
        team_info = teams['results'][0]
        team_id = team_info['id']
        print(f"✅ Équipe trouvée : {team_info['name']} (ID {team_id})")

        # Récupération des matchs
        try:
            matches = await cs2.get_team_upcoming_matches(team_id)
        except Exception as e:
            print(f"❌ Erreur API : {e}")
            return
        
        if not matches:
            print("ℹ Aucun match à venir.")
            return

        # Tri par date
        matches.sort(key=lambda m: m.get('date', 0))

        cal = Calendar()
        for match in matches:
            try:
                team1 = match['team1']['name']
                team2 = match['team2']['name']
                start_time = datetime.fromtimestamp(match['date'] / 1000, tz=timezone.utc).astimezone(TIMEZONE)
                url = match.get('match_page', '')
                tournoi = match['tournament']['name']

                event = Event()
                event.name = f"{team1} vs {team2}"
                event.begin = start_time
                event.url = url
                event.description = f"Tournoi : {tournoi}\nLien : {url}"
                cal.events.add(event)
            except KeyError as e:
                print(f"⚠ Match ignoré, clé manquante : {e}")

        # Écriture du fichier
        with open("vitality.ics", "w", encoding="utf-8") as f:
            f.writelines(cal)
        print("✅ Fichier vitality.ics généré avec succès.")

if __name__ == "__main__":
    asyncio.run(generate_calendar())