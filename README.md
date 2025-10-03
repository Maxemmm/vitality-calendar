# 🎮 CS2 Teams Calendar

Calendrier automatique pour suivre les matchs de vos équipes CS2 préférées !

## ✨ Fonctionnalités

- **📅 Génération automatique** de calendrier iCalendar (.ics) pour CS2
- **⚙️ Support multi-équipes** - suivez plusieurs équipes simultanément  
- **⏱️ Durées intelligentes** basées sur le format des matchs (BO1, BO3, BO5, BO7)
- **🔄 Mise à jour automatique** via GitHub Actions
- **📱 Compatible** avec tous les calendriers (Outlook, Google Calendar, Apple Calendar, etc.)
- **🎮 Spécialisé Counter-Strike 2** avec API bo3.gg

## 🚀 Installation rapide

1. Clonez le repository :
```bash
git clone https://github.com/votre-username/cs2-teams-calendar.git
cd cs2-teams-calendar
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurez vos équipes dans `config.json` (obligatoire !)

4. Lancez le script :
```bash
python generate_calendar.py
```

## ⚙️ Configuration

Le fichier `config.json` est **obligatoire** ! Créez-le avec :

```json
{
  "teams": ["Vitality", "G2", "NAVI"],
  "match_durations": {
    "bo1": 1.5,
    "bo3": 4.0,
    "bo5": 6.5,
    "bo7": 9.0
  },
  "output_file": "matches.ics",
  "base_url": "https://bo3.gg/matches/"
}
```

### Options de configuration

- **`teams`** : Liste des équipes à suivre (obligatoire)
- **`match_durations`** : Durées estimées selon le format (en heures)
- **`output_file`** : Nom du fichier .ics généré (par défaut: matches.ics)
- **`base_url`** : URL de base pour les liens des matchs

## 🔄 Mise à jour automatique

Le projet utilise GitHub Actions pour se mettre à jour automatiquement :
- **Planifié** : Tous les jours à 12h UTC
- **Manuel** : Via l'onglet "Actions" de GitHub
- **Automatique** : Le fichier .ics est commité et poussé automatiquement

## 📁 Structure du projet

```
cs2-teams-calendar/
├── .github/workflows/update-calendar.yml  # GitHub Actions
├── generate_calendar.py                   # Script principal
├── config.json                           # Configuration
├── requirements.txt                       # Dépendances Python
├── matches.ics                           # Calendrier généré (toutes équipes)
├── .gitignore                           # Fichiers ignorés par Git
└── README.md                            # Documentation
```

## 🎯 Formats de matchs supportés

- **BO1** : 1h30 (match rapide)
- **BO3** : 4h (meilleur de 3)
- **BO5** : 6h30 (meilleur de 5)
- **BO7** : 9h (meilleur de 7)

## 🔍 Équipes CS2 populaires

Pour ajouter une équipe à votre calendrier, vous devez connaître son nom exact dans l'API. Voici les principales équipes CS2 :

- **Vitality** - Équipe française (Top mondial)
- **NAVI** (Natus Vincere) - Équipe ukrainienne
- **G2** - Équipe européenne
- **FaZe** - Équipe internationale  
- **Astralis** - Équipe danoise (ancienne puissance)
- **Cloud9** - Équipe américaine
- **Liquid** - Équipe internationale
- **C9** - Cloud9 format court

💡 **Conseil** : Le script trouvera automatiquement l'ID correspondant dès que vous tapez le nom de l'équipe.

## 🔗 API utilisée

Ce projet utilise l'API **[bo3.gg](https://bo3.gg)** qui fournit :
- Les données des équipes CS2
- Les matchs en temps réel
- Les informations des tournois
- Les liens directs vers les pages des matchs

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des nouvelles fonctionnalités
- Améliorer la documentation

## 📄 Licence

MIT License - voir le fichier LICENSE pour plus de détails.