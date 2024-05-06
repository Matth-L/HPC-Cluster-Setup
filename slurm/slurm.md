Slurm sera utilisé afin de gérer les ressources de calcul. 

Nous utiliserons les serveurs XXX pour ce service car XXX . 

Il est nécessaire de créer des partitions pour chaque projet.
Chaque partition sera associée à un projet et un utilisateur sera rattaché à 
une partition.

# Configuration de Slurm

- Permettra aux utilisateurs du cluster de soumettre leurs jobs sur les différents types de nœuds
de calcul

Nous allons créer des partitions pour chaque projet, chaque partition sera associée à un projet
cela permettra aux utilisateurs de soumettre leurs jobs sur les différents types de noeuds de calcul.

```conf
NodeName=AC[Deb-Fin] Sockets=XXX RealMemory=XXX State=UNKNOWN
NodeName=AL[Deb-Fin] Sockets=XXX RealMemory=XXX State=UNKNOWN
NodeName=AX[Deb-Fin] Sockets=XXX RealMemory=XXX State=UNKNOWN
```

- Optimisera l’ordonnancement des jobs et le choix des nœuds lors de leur allocation.

Pour notre configuration Slurm, nous utiliserons le "backfill" pour l'ordonnancement des jobs,
cela permettra à un job moins prioritaire de s'exécuter tant qu'il ne modifie pas le démarrage
d'autre job. De plus, pour le choix des noeuds, il nous est demandé de permettre aux utilisateurs
de choisir leurs noeuds, et non de choisir certains cpus en particulier. Nous utiliserons donc
la sélection de noeuds complets "linear", même si nous pensons que celle-ci n'est pas la plus optimales.

- Mettra en place une comptabilité des ressources consommées

Afin d'avoir une comptabilité des ressources consommées, il sera nécessaire d'utiliser slurmdbd, 
cela nous permettra d'avoir une persistance des données. Il est donc nécessaire 
d'avoir une base de données, nous utiliserons MariaDB qui est une base de donnée MySQL.

# Restreindre l’allocation des ressources

Juste faire des parents pour chaque projet et leur attribuer un pourcentage de ressources.

- Limiter le nombre de jobs et de ressources utilisées par défaut par utilisateur ,

Il est nécessaire de rajouter dans le fichier de configuration de Slurm :

```conf
MaxJobsPerUser=XX
MaxSubmitJobsPerUser = XX
```

La limite des 
- Offrir la possibilité aux utilisateurs des projets 1 et 2 de tourner rapidement des jobs pour debugger mais en restreignant encore plus le nombre de ces jobs ainsi que leur durée,

```bash
sacctmgr -i create QOS name=debug priority=10 maxjobs=2 maxwall=10:00 
```

Il faudra ensuite associer les utilisateurs aux QOS.

- Ne pas donner l’accès aux nœuds de la partition AX des utilisateurs du projet0,

Il suffit de préciser dans la partie PartionName=projet0 que les noeuds de la partition AX ne sont pas accessibles.

- Attribuer respectivement aux 4 projets 15 %, 20 %,40 %, 25 % d’utilisation de la machine.

Il faut créer des utilisateurs parents pour chaque projet.

```bash
sacctmgr create account name=projet0 faishare=15 
sacctmgr create account name=projet1 faishare=20 
sacctmgr create account name=projet2 faishare=40 
sacctmgr create account name=projet3 faishare=25 
```

# Création des utilisateurs

Créeons un utilisateur pour le projet 0 par exemple.

```bash
sacctmgr create account name=userXugpYprojet0 parent=project0 account=projet0 qos=normal
```

Ainsi qu'un utilisateur pour le projet 1, il doit donc pouvoir debugger rapidement, en plus de pouvoir lancer des jobs.

```bash
sacctmgr create account name=userXugpYprojet1 parent=project1 account=projet1 qos=debug,normal
```



# Vérification de la politique mise en place

Pour vérifier la politique mise en place, il suffit de faire :

```bash
sacctmgr show qos
```
Pour voir si les QOS ont bien été créées.
Ainsi que : 

```bash
sinfo
```
Pour voir les partitions et les noeuds associés.

