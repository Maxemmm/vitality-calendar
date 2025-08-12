import asyncio
from cs2api import CS2
from ics import Calendar, Event
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import json

TEAM_NAME = "Vitality"
TIMEZONE = ZoneInfo("Europe/Paris")  # Change si besoin

async def generate_calendar():
    async with CS2() as cs2:
        # Recherche équipe
        print("📡 Recherche de l'équipe...")
        teams = await cs2.search_teams(TEAM_NAME)
        print("DEBUG: Réponse brute API search_teams() :")
        print(json.dumps(teams, indent=4))

        if not teams or 'results' not in teams or not teams['results']:
            raise ValueError(f"❌ Équipe {TEAM_NAME} introuvable.")
        
        team_info = teams['results'][0]
        team_id = team_info['id']
        print(f"✅ Équipe trouvée : {team_info['name']} (ID {team_id})")

        # Récupération matchs
        print("📡 Récupération des matchs à venir...")
        try:
            matches_raw = await cs2.get_team_upcoming_matches(team_id)
            print("DEBUG: Réponse brute API get_team_upcoming_matches() :")
            print(json.dumps(matches_raw, indent=4))

            # Extraire liste selon structure
            if isinstance(matches_raw, dict):
                if "results" in matches_raw:
                    matches = matches_raw["results"]
                else:
                    print("⚠ Structure inattendue, tentative d'utilisation directe comme liste vide.")
                    matches = []
            elif isinstance(matches_raw, list):
                matches = matches_raw
            else:
                print("⚠ Structure inconnue pour matches.")
                matches = []
        except Exception as e:
            print(f"❌ Erreur API : {e}")
            return

        if not matches:
            print("ℹ Aucun match à venir trouvé.")
            return

        # Tri par date
        matches.sort(key=lambda m: m.get('date', 0))

        # Création du calendrier
        cal = Calendar()
        for match in matches:
            try:
                team1 = match.get('team1', {}).get('name', 'TBD')
                team2 = match.get('team2', {}).get('name', 'TBD')
                date_ts = match.get('date')
                if date_ts:
                    start_time = datetime.fromtimestamp(date_ts / 1000, tz=timezone.utc).astimezone(TIMEZONE)
                else:
                    start_time = None
                url = match.get('match_page', '')
                tournoi = match.get('tournament', {}).get('name', 'Tournoi inconnu')

                event = Event()
                event.name = f"{team1} vs {team2}"
                if start_time:
                    event.begin = start_time
                event.url = url
                event.description = f"Tournoi : {tournoi}\nLien : {url}"
                cal.events.add(event)
            except Exception as e:
                print(f"⚠ Match ignoré : {e}")

        # Sauvegarde fichier
        with open("vitality.ics", "w", encoding="utf-8") as f:
            f.writelines(cal)
        print("✅ Fichier vitality.ics généré.")

if __name__ == "__main__":
    asyncio.run(generate_calendar())