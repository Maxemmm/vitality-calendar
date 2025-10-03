# 🎮 Changelog - CS2 Teams Calendar

## [Version 2.0.0] - 2024-01-XX

### ✨ Nouvelles Fonctionnalités
- **Mises à jour automatiques 2x par jour** (00h et 12h UTC)
- **Validation avancée de configuration** avec messages d'erreur explicites
- **Gestion robuste des erreurs** avec fallback gracieux
- **Limitation du nombre de matchs** par équipe (configurable)
- **Logging professionnel** avec emojis et niveaux adaptés
- **Métadonnées enrichies** dans les événements calendrier
- **Support de configuration avancée** avec valeurs par défaut

### 🔧 Améliorations Techniques
- **Workflow GitHub Actions optimisé** avec validation avant exécution
- **Script Python refactorisé** avec gestion d'erreurs avancée
- **Dépendances fixes** avec versions minimum garanties
- **Cache pip** dans les workflows pour des builds plus rapides
- **Timeout configuré** pour éviter les hangs
- **Commits plus sensés** avec emojis et timestamps

### 🐛 Corrections
- **Suppression du workflow dupliqué** generate.yml
- **Validation de configuration** avant traitement
- **Gestion des équipes introuvables** sans faire échouer le processus
- **Dates malformées** gérées proprement
- **Messages d'erreur** en français pour cohérence

### 📋 Changements Breaking
- Nouvelle structure de `config.json` avec options additionnelles
- Migration automatique des configurations existantes
- Changement des horaires par défaut des mises à jour (00h et 12h au lieu de 05h)

## [Version 1.x.x] - Historique précédent
Initial import des fonctionnalités de base.
