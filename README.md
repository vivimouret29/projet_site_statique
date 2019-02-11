# Générateur de site statique

## Génerer un site statique

Les fichiers compris par un navigateur internet sont aux formats HTML/CSS/JavaScript. Vous n'avez peut-être pas envie de taper du HTML quand vous écrivez un blog. Il serait pratique de générer les pages web à partir d'un format textuel simple, comme le markdown, langage utilisé pour écrire le document que vous lisez actuellement.

## Projet

Le but était de réaliser un outil convertissant un dossier de fichiers markdown en un autre dossier contenant les fichiers d'un site statique. Du HTML est généré à partir du markdown, cet HTML est mélangé avec des modèles de pages web pour générer des pages toutes conformes au même modèle.  
Pour donner un ordre d'idée, la version la plus basique du projet peut être faite en moins de 100 lignes.  
Pour ce faire, il vous faut **préalablement installer** la dernière version de pip. Puis par Python, installer : `pip install markdown2` et  `pip install argparse` qui seront ensuite importés via le code.

## Réalisation d'une interface en ligne de commande

Nous avons utiliser un outil en ligne de commande pour générer les fichiers du site statique.  
Il prend en comptes ces paramètres :
* `-i ./md` ou `--input-directory ./md` :  le chemin du dossier de **fichiers source**
* `-o ./html` ou `--output-directory ./html` : le chemin du dossier où sont mis les **fichiers générés** pour le site statique 
* `-t ./template` ou `--template-directory ./template` : le dossier contenant des **modèles** de pages web
* `-h` ou `--help` : pour afficher de **l'aide** pour expliquer les paramètres de la commande
Nous avons dans ce cas là, utilisé **argparse**.

## Rendu sur Github

Pour générer la conversion et le site statique, il vous faudrat donc :
* réaliser l'installation de pip
* indiquer les dossiers des fichiers sources et générés
* rentrer cette commande en ayant naviguer dans le bon dossier : 
```  
python .\site_statique.py -i ./md -o ./html
```
Ainsi vous aurez lancés le programme.