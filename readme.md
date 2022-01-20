            --------------------------------------
            | NOM       | Myjob  |           
            --------------------------------------
            |      TP INFO 3055                  |
            --------------------------------------
            |Niveau     | licence 3 informatique |


### DESCRIPTION DU PROJET

Comme dans le monde entier, le Cameroun connait une 
De nos jours chercher une opportunité d’emploi n’est pas facile soit parce que nous ne savons pas vers qui se tourner soit nous avons l’informations très tard et pas assez de temps pour postuler à l’offre de plus il est fatiguant de chercher sur les sites entreprises cas peut parmi eu font des sites vitrine dynamique de plus avec les situations sanitaires actuelle il y a une restriction de personne dans les lieux public.

### liste de membre du projet Myjob

            -------------------------------------------------------------------------------
            |Matricule       |  NOM ET PRENOMS                   |     NOM SUR GITHUB      |
            -------------------------------------------------------------------------------
            | 19M2310        |  NOUTCHEU LIBERT JORAN            |       noutc123          |
             ------------------------------------------------------------------------------
            | 18T2814        | TCHIAGUIA CHRISTOPHE              |    chrisAfrotech        |
             ------------------------------------------------------------------------------
            | 18T2737        |TABANTSA ZEMBOUG ARMAND            |  tabantsa               |
             ------------------------------------------------------------------------------
            |  19M2245      |     MEKEUTIBOUA TAFEUTSOP DARELLE  |  Darell20               |                       
             ------------------------------------------------------------------------------
            |  18T2578      |     TAMO MBOBDA  ERIC Arnaud       |                         |                  
             ------------------------------------------------------------------------------
             
## Prerequis
      ## pour Demarer le serveur django
      il faut intsalller au prealable django 4.0
      afin de pouvoir lancer notre api 
          * cree un environement virtuel a la racine du dossier myjob 
          * installer les dependances pour le projet en backend
          * pip install -r requirements.txt
          * aller dans le dossier ./src/myjob 
          * lancer la commande 
            ->   python manage.py migrate pour appliquer les migrations de la bd 
            ->   python manage.py makemigrations  pour appliquer les migrations du models
            ->   python manage.py migrate 
            ->   python manage.py runserver 
          *aller a l'adresse localhost:8000/api/v1 ou localhost:8000/api/docs pour voire la documentation de l'api 
              
 
      ## pour le frontend 
       il faut intsalller au Vuejs 3.0
      afin de pouvoir lancer notre site 
          * installer les dependances pour le projet
          * aller dans le dossier ./src/myjob/ui/web/
          * lancer la commande 
            ->   yarn install
            ->   yarn start pour lancer le projet
          *aller a l'adresse http://localhost:8080/accueil
