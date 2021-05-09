# Projet P2 - La ferme des 3 Chênes 🐮

## Table des matières
1. [Installation Linux](#Installation Linux)
2. [Installation Windows](#Installation Windows)
3. [Figure choisi](#Figure choisi)
4. [Context](#Context)
5. [Documents annexes](#Documents annexes)

## Installation Linux / macOS
#### /!\ Important avant de commancer /!\ 
> Avant de commencer, vérifier que vous avez bien installé python3, git, pip (il est nativement présent dans python3) et virtualenv sur votre ordinateur.

Ouvrez le terminal de commande et clonez le projet en local avec la commande 
```
git clone https://github.com/Emilevillette/Projet2-P2
```
déplacez-vous dans le projet avec la commande
```
cd /Projet2-P2
```
Créez un environnement virutel (venv) avec la commande
```
virtualenv --python python3 venv
```
Activez l'environnement virtuel avec
```
source venv/bin/activate
```
Le projet à besoin de quelques dépendances que vous allez pouvoir installer grâce à la commande
```
pip install -r requirements.txt
```
Entrer la commande ```Flask run``` ou ```python3 app.py``` pour lancer l'application.

Enfin, ouvrez votre navigateur et coller ```http://127.0.0.1:5000``` dans la barre d'adresse URL.

Et voilà! 

(Pour désactiver l'environnement virtuel, taper la commande```deactivate```)

<hr>

## Installation Windows
#### /!\ Important avant de commancer /!\ 
> Avant de commencer, vérifier que vous avez bien installé python3, git, pip (il est nativement présent dans python3) et virtualenv sur votre ordinateur.

Ouvrez l'invité de commande et clonez le projet en local avec la commande 
```
git clone https://github.com/Emilevillette/Projet2-P2
```
déplacez-vous dans le projet avec la commande
```
cd /Projet2-P2
```
Créez un environnement virutel (venv) avec la commande
```
virtualenv --python python3 venv
```
Activez l'environnement virtuel avec
```
source venv/bin/activate
```
Le projet à besoin de quelques dépendances que vous allez pouvoir installer grâce à la commande
```
pip install -r requirements.txt
```
Entrer la commande ```Flask run``` ou ```python3 app.py``` pour lancer l'application.

Enfin, ouvrez votre navigateur et coller ```http://127.0.0.1:5000``` dans la barre d'adresse URL.

Et voilà! 

(Pour désactiver l'environnement virtuel, taper la commande```deactivate```)

<hr>

## Figures choisi
1. Une croyance populaire chez certains éleveurs est que les naissances arrivent plus souvent à la pleine lune.
    > 1.1 Est-ce vrai ou pas ? Produire une heat map ou bar chart sur 28 jours avec le % de vêlage.

3. Il arrive malheureusement qu’un veau soit mort-né. Pour en diminuer le nombre, il est utile de savoir quelles peuvent en être certaines causes. 
    > 3.1 Y a-t-il un moment particulier durant l’année auquel plus de décès arrivent ? (chart ou bar plot sur l’année)
   
4. Il arrive qu’un veau décède dans ses premières semaines de vie. On parle alors de décès prématuré. Pour en diminuer le nombre, nous voulons savoir quelles peuvent en être les causes.
    > 4.1 Y a-t-il un moment particulier durant l’année lors duquel plus de décès prématurés arrivent ? (chart ou bar plot sur l’année)
    
7. Le vendeur de dose d’insémination nous propose de racheter des doses d’un taureau ou d’un enfant d’un taureau que nous avons déjà eu. Nous pouvons utiliser les données des veaux déjà nés pour évaluer le taureau au sein de notre ferme.
    > 7.1 Quel fut son utilisation ? (graphe par mois du nombre de veau né de ce taureau, veau de 2ème génération, de 3ème génération)

<hr>

## Context 
La ferme des trois chênes est une exploitation laitière et agricole. La gestion d’une telle exploitation ne s’improvise pas et nécessite une certaine organisation. Pour moderniser la gestion de la ferme, Mr. et Mme. Verhaeghe ont fait appel à nos services.

Vous aurez à votre disposition, dès la semaine 8, une base de données décrivant tous les animaux qui ont un jour vécu à la ferme depuis sa création en 1990. Ces données comprennent la liste des animaux, la liste des naissances, la race de certains animaux, les familles des vaches, etc. Votre mission consistera à créer un site web qui présente certaines informations dérivées de ces données et utiles à Mr. et Mme. Verhaeghe. Votre site web sera responsable de l’extraction de données pertinentes de la base de données, du calcul de statistiques de ces données, et de l’affichage du résultat sur une page web, soit en tableau, ou via un graphe. La [page suivante](http://linfo1002.eu.pythonanywhere.com) montre un exemple simple de résultat utile à la famille Verhaeghe.

<hr>

## Documents annexes
* [Projet 2 - Instructions](http://renaud-detry.net/teaching/1002/projet2inst.html)
* [La ferme des 3 Chênes](http://renaud-detry.net/teaching/1002/projet2.html)
* [Le world wide web (www)](http://renaud-detry.net/teaching/1002/web.html)
* [Le language HTML](http://renaud-detry.net/teaching/1002/html.html)
* [Les bases de données SQL](http://renaud-detry.net/teaching/1002/sql.html)
* [La visualisation via chart.js](http://renaud-detry.net/teaching/1002/chartjs.html)
* [Le framework flask](http://renaud-detry.net/teaching/1002/flask.html)
* [Tutoriel flask](https://sites.uclouvain.be/P2SINF/flask/tutorial/index.html#tutorial)
