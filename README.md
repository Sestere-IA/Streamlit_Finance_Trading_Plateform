# Plateforme de Trading

Ce projet consiste à créer un outil d’aide à la décision financier dans le cadre
d’investissement boursier. Nous disposons d’une source de données issue du site Yahoo finance.

## Appendix

Il s’agit ici de créer une plateforme de trading basé sur des données récoltées sur le site
Yahoo Finance. Cette application devra comprendre ces trois blocs :
1. Front End Application
2. Backend Application
3. Déploiement d’application
   
## Authors

- [@Sestere-IA](https://github.com/Sestere-IA)
- [@Anassinho78](https://github.com/Anassinho78)

## Current Functionality
###Front End Application
1. Définition de l’utilisateur de l’application
- Nom de l’utilisateur
- Prénom de l’utilisateur
- Capital
- Date de création du compte 
  
Cette application devra être en mesure de sauvegarder les ordres passés précédemment.
- Sauvegarde des utilisateurs dans une table SQL/fichier csv
- Sauvegarde des actions sélectionnées, de la quantité associée ainsi que du capital restant

2. Passage de l’ordre
- Saisie du Ticker
- Saisie de la date de début de cotation
- Saisie de la date de fin de cotation (Par défaut, il s’agira de la date du jour)
- Ajout d’un radio bouton permettant d’ajouter un ou plusieurs cours (Cours unique –
Multiple cours)
  
Ce dashboard servira d’outil d’aide à la décision à l’achat d’action et devra permettre de
répondre aux questions suivantes :

- Evolution du cours de l’action sur la période définie 
- Rendement de l’action sur la période définie
- Courbe de tendance -Moyenne mobile des multiples cours

3. Liste des utilisateurs et historique des transactions

On affichera un dataframe comprenant l’historique des transactions passé. Il comprendra les
variables suivantes :
- Nom
- Prénom
- Date de passage de l’ordre (en format YYYY-mm-dd hh :mm :ss)
- Action choisie
- Quantité
- Valeurs de la transaction
- Multiple buy (Une indicatrice permettant de distinguer les passages d’ordre de
plusieurs actions simultanés de ceux qui ont été passés sur une seule action)
  
###Backend Application
Le back end devra être réalisé en Python. Il s’agira de permettra à l’utilisateur de passer l’ordre

- Récupération des données financières
- Passage d’une page à l’autre de l’application
- Gestion des erreurs dans la saisie des valeurs
- Prédiction du prix d’une action à 6 mois et un an à partir des données des données des années
2017, 2018, 2019 et 2020. On utilisera pour ce faire les modèles de ST (ARIMA, BATS, lissage
expo, Holt Winter ou ceux issues du package Facebook Prophet.
  
###Déploiement d’application
Rendu sur un repository Github et déployer sur une application Heroku

###ToKnow

- Connection to pre-existing client : Login=sestere / Mdp=j'aimelesfrites

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started (In progress).

Please adhere to this project's `code of conduct`.


## Installation

Install Python 3.7 on your machine and run with "streamlit run main_app.py"

## Deployment

Use "streamlit run main_app.py".
The result going to be enable in :
- Local URL: http://localhost:8501
- Network URL: http://192.168...

## FAQ

#### Quel est le but du projet ?

Nous voulons aider un novice à la prise décision financier dans le cadre d’investissement boursier

#### D'autres plateforme sont-il prévue ?

L'app sera hébergé sur un serveur Heroku.

#### French to English Translate in Web Site ?

Development under progress.

## 🚀 About Me
I'm a IA School Student. https://www.linkedin.com/in/dataandautomation/
## 🛠 Skills
All my skills in https://www.linkedin.com/in/dataandautomation/

## Acknowledgements

 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
 - [Anass Mourhiteddine](https://github.com/Anassinho78)
 - [IA School](https://www.intelligence-artificielle-school.com/)

## Features

- Connection à son compte bancaire
- Système de "re-trading" directement depuis l'app
- Developper l'agorithme ML pour une précision absolue
- Devlopper une partie Web Scrapping pour donner une vision global des ticker à l'utilisateur
- Mettre en transparence les transactions avec un système de block chain


## Feedback

If you have any feedback, please reach out to us at alexandre.nabyt75@gmail.com

## Roadmap

- Add possibility to do multiple actions
- Add Courbe de tendance
- Add moyenne mobile des multiples cours


