# Objectif
L'objectif de ce mini projet est d'apprendre l'utilisation de jinja2 pour la mise en pratique dans DBT

# Le Projet MiniCv est structuré comme suit : 

1. Définition du modèle de CV : Un fichier Jinja template avec des champs dynamiques (nom, compétences, expériences…).

2. Données en entrée : Un fichier JSON ou une base de données où chaque mini CV est stocké.

3. Génération du CV : Utilisation de Jinja pour transformer les données en fichier HTML.

5. Conversion en PDF : Une bibliothèque comme WeasyPrint ou wkhtmltopdf pour convertir le HTML en PDF.

# Pré-requis
- Installation de la machine virtuel python
- Installation de jinja
- Créer un repot git

# Programme
3. Créer les dossier 'template' et 'build' (pour les générations automatique)
4. Installer jinja2 et htmlmin (minificateur du code html pour aléger les fichiers html)

# Déjà fait
1. Installation de la machine virtuel python
2. Créer un repot git
3. Créer les dossier 'template' et 'build' (pour les générations automatique)
4. Installer jinja2 et htmlmin (minificatuer du code html pour aléger les fichiers html)

# Procedure
1. Installation de la machine virtuel python (nommée venv)
    A partir de vscode, dans le dossier du projet faire : 
    "python.exe -m venv venv"


2. Créer un repot git (localement)
- Initialiser le dépot git :
 Dans vscode, aller sur le dossier contenant le projet (cd )
 Faire : "git init"
- Dans github, créer le dépot dans lequel sera pusher le dépot local après les avoir liés
- Changer le non de la branch master en main
    git branch -M main
- Lié le dépot local au dépot distant créé
    git remote add origin https://github.com/Tedngoye/Jinja_Mini_CV.git
- Faire le premier push du projet en local vers le distant
    git push -u origin main

4. Installer jinja2 et htmlmin (minificatuer du code html pour aléger les fichiers html)
    pip install jinja2
    pip install htmlmin
# En cours
