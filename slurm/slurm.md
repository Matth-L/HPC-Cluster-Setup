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

```bash
PartitionName=AC Nodes=XX Default=YES MaxTime=INFINITE State=UP
PartitionName=AL Nodes=XX Default=YES MaxTime=INFINITE State=UP
PartitionName=AX Nodes=XX Default=YES MaxTime=INFINITE State=UP
```

(pas giga sur)

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