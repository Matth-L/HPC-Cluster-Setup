2) Préciser la configuration slurm qui :
• Permettra aux utilisateurs du cluster de soumettre leurs jobs sur les différents types de nœuds
de calcul
• Optimisera l’ordonnancement des jobs et le choix des nœuds lors de leur allocation.
• Mettra en place une comptabilité des ressources consommées


Permettre aux utilisateurs du cluster de soumettre leurs jobs sur les différents types de nœuds de calcul :
truc du style :

PartitionName=AC Nodes=XX Default=YES MaxTime=INFINITE State=UP
PartitionName=AL Nodes=XX Default=YES MaxTime=INFINITE State=UP
PartitionName=AX Nodes=XX Default=YES MaxTime=INFINITE State=UP

On choisit pour l'ordonnacement des jobs : 
SchedulerType = backfill  (pour une "optimisation de l'ordonnancement")

choix des noeuds lors de leur allocation :
???

Comptabilité des ressources consommées :
Utilisation de mariadb


3) Restreindre l’allocation des ressources en fonction de 4 projets projet[0-3] de la façon suivante :
Chaque regroupement de communauté d’utilisateurs, est rattaché à un « projet » ie
projet0 : utilisateurs de ugp[0-2], … ,projet3 : utilisateurs de ugp[8-9].
• Limiter le nombre de jobs et de ressources utilisées par défaut par utilisateur ,
• Offrir la possibilité aux utilisateurs des projets 1 et 2 de tourner rapidement des jobs pour
debugger mais en restreignant encore plus le nombre de ces jobs ainsi que leur durée,
• Ne pas donner l’accès aux nœuds de la partition AmdGpu des utilisateurs du projet0,
• Attribuer respectivement aux 4 projets 15 %, 20 %,40 %, 25 % d’utilisation de la machine.
Donner les commandes nécessaires à la création de cette politique en y associant au minimum un
utilisateur par projet. Le nom des utilisateurs contiendra son numéro de ugp et son projet.:
exemple userXugpYprojetZ.
Donner les commandes permettant de vérifier la politique mise en place.

ça c'est QOS et sacctmgr je pense 


