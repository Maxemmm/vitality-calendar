# 🎮 Vitality Calendar

Calendrier automatique pour suivre les matchs de vos équipes CS2 préférées !

## ✨ Fonctionnalités

- **📅 Génération automatique** de calendrier iCalendar (.ics)
- **⚙️ Support multi-équipes** - suivez plusieurs équipes simultanément
- **⏱️ Durées intelligentes** basées sur le format des matchs (BO1, BO3, BO5, BO7)
- **🔄 Mise à jour automatique** via GitHub Actions
- **📱 Compatible** avec tous les calendriers (Outlook, Google Calendar, Apple Calendar, etc.)

## 🚀 Installation rapide

1. Clonez le repository :
```bash
git clone https://github.com/votre-username/vitality-calendar.git
cd vitality-calendar
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
vitality-calendar/
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

## 🔍 Trouver l'ID d'une équipe

Pour ajouter une nouvelle équipe à votre calendrier, vous devez connaître son nom exact. Voici quelques équipes populaires :

- **Vitality** - Equipe principale française
- **G2** - Equipe européenne  
- **NAVI** (Natus Vincere) - Equipe ukrainienne
- **FaZe** - Equipe internationale
- **Astralis** - Equipe danoise

💡 **Conseil** : Les noms doivent être exacts. Utilisez le script `scripts/find_team.py` pour vérifier les noms disponibles.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer des nouvelles fonctionnalités
- Améliorer la documentation

## 📄 Licence

MIT License - voir le fichier LICENSE pour plus de détails.