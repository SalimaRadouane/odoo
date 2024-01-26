# Gestion des Formations avec Odoo

## Introduction

Ce projet est une solution complète de gestion des formations développée avec Odoo. Il vise à simplifier les processus de gestion des sessions de formation, des participants et des finances au sein d'une organisation.

## Auteurs

- Salima Radouane
- Aya Bouchantouf
## Fonctionnalités Principales

- **Gestion des Sessions de Formations:** Enregistrement des informations sur chaque session, gestion de l'état, suivi des participants, affectation des formateurs, suivi des dépenses et revenus, envoi d'e-mails, création de rapports.

- **Gestion des Participants et Formateurs:** Enregistrement des informations, attribution d'images, association à des sessions, communication via e-mails et SMS.

- **Gestion des Dépenses et Revenus:** Enregistrement des dépenses et revenus liés à chaque session, calcul du revenu net.

- **Gestion des Paiements:** Enregistrement des paiements des participants.

## Structure du Projet

- **Models:** Définition des modèles de données pour les formateurs, participants, sessions, dépenses, revenus, paiements, etc.

- **Views:** Configuration des vues pour afficher, ajouter, modifier et gérer les données via l'interface utilisateur d'Odoo.

- **Static:** Stockage des fichiers statiques tels que CSS, JavaScript, images.

- **Data:** Fichiers XML spécifiant les données initiales à charger dans la base de données lors de l'installation du module.

- **Reports:** Fichiers de modèle de rapport pour générer des rapports PDF ou HTML.

- **Controller:** Définition des contrôleurs pour le traitement des demandes HTTP et l'interaction avec l'interface utilisateur.

- **Security:** Définition des règles de sécurité pour le module.



## Installation

1. Clonez le dépôt : `git clone https://github.com/SalimaRadouane/odoo.git`
3. Exécutez Odoo : `./odoo-bin -c odoo.conf`

