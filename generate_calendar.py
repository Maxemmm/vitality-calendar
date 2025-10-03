import asyncio
from cs2api import CS2
from ics import Calendar, Event
from datetime import datetime, timedelta
import json

def load_config():
    """Charge la configuration depuis config.json"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print("[ERROR] Fichier config.json non trouvé !")
        raise
    except json.JSONDecodeError as e:
        print(f"[ERROR] Erreur de syntaxe dans config.json : {e}")
        raise

def detect_match_format(match):
    """Détecte le format du match (BO1, BO3, BO5, BO7)"""
    tournament_name = match.get('tournament', {}).get('name', '').lower()
    
    if 'bo7' in tournament_name:
        return 'bo7'
    elif 'bo5' in tournament_name or 'best of 5' in tournament_name:
        return 'bo5'
    elif 'bo3' in tournament_name or 'best of 3' in tournament_name:
        return 'bo3'
    elif 'bo1' in tournament_name or 'best of 1' in tournament_name:
        return 'bo1'
    else:
        # Par défaut, assume BO1 pour les matchs rapides
        return 'bo1'


async def generate_calendar():
    try:
        config = load_config()
    except:
        return
    
    async with CS2() as cs2:
        all_matches = []
        
        for team_name in config['teams']:
            print(f"[INFO] Recherche de l'équipe {team_name}...")
            teams = await cs2.search_teams(team_name)
            
            if not teams or 'results' not in teams or len(teams['results']) == 0:
                print(f"[WARNING] Équipe {team_name} introuvable.")
                continue
            
            team_info = teams['results'][0]
            team_id = team_info['id']
            print(f"[SUCCESS] Équipe trouvée : {team_info['name']} (ID {team_id})")

            try:
                print(f"[INFO] Récupération des matchs à venir pour {team_name}...")
                matches = await cs2.get_team_upcoming_matches(team_id)
                
                if matches and 'results' in matches and len(matches['results']) > 0:
                    # Ajouter le nom de l'équipe pour identifier à quelle équipe appartient le match
                    for match in matches['results']:
                        match['team_name'] = team_name
                    all_matches.extend(matches['results'])
                    print(f"[SUCCESS] {len(matches['results'])} match(s) trouvé(s) pour {team_name}")
                else:
                    print(f"[INFO] Aucun match à venir pour {team_name}")
                    
            except Exception as e:
                print(f"[ERROR] Erreur lors de la récupération des matchs pour {team_name} : {e}")

        if not all_matches:
            print("[INFO] Aucun match à venir trouvé pour toutes les équipes.")
            return

        cal = Calendar()
        
        for match in all_matches:
            event = Event()
            event.name = f"{match['team1']['name']} vs {match['team2']['name']}"

            # Parse start_date ISO8601 string en datetime
            event.begin = datetime.fromisoformat(match['start_date'].replace("Z", "+00:00"))
            
            # Détection du format du match et ajustement de la durée
            match_format = detect_match_format(match)
            duration_hours = config['match_durations'].get(match_format, 1.5)
            event.duration = timedelta(hours=duration_hours)
            
            # URL vers la page du match
            event.url = config['base_url'] + match['slug']
            
            # Description avec nom du tournoi, format et lien
            tournament_name = match['tournament']['name']
            event.description = f"Tournoi : {tournament_name}\nFormat : {match_format.upper()}\nDurée prévue : {event.duration}\nÉquipe suivie : {match['team_name']}\nLien : {event.url}"

            cal.events.add(event)

        with open(config['output_file'], "w", encoding="utf-8") as f:
            f.writelines(cal)

        print(f"[SUCCESS] Fichier {config['output_file']} généré avec {len(all_matches)} événement(s).")

if __name__ == "__main__":
    asyncio.run(generate_calendar())