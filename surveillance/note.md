Le contrat de disponibilité spécifie 5 critères de disponibilité.
1) Au moins un nœud de login doit être opérationnel pour chaque communauté,
2) Un débit minimal de 32 GB/s vers le système de stockage Lustre doit etre assuré,
3) 90% des nœuds de la partition AC doivent être disponibles,
4) 80% des nœuds de la partition AL,
5) 60 % des nœuds de la partition AX.
La sociéte AzkarHPC utilise le logiciel Shinken comme logiciel de surveillance et a écrit des
sondes (scripts) pour vérifier les critères de disponibilités :
• la sonde verif-noeud vérifie qu'une liste de nœuds est up
• la sonde verif-lustre-routeur vérifie que le service Lustre est opérationnel sur une liste de
nœuds
• la sonde verif-nodeset-ssh vérifie que le service ssh est opérationnel sur une liste de nœuds
Spécifier comment vous pourriez utiliser ces sondes pour vérifier les critères de disponibilités
(paramètres d'appel de ces sondes)
Proposer l'implémentation d'une sonde qui surveillera les seuils de disponibilité pour une partition
slurm.
Donner 3 points spécifiques à surveiller sur les nœuds de login pour qu'ils puissent assurer un
service interactif confortable pour les utilisateurs.
Au niveau du centre de calcul, quels sont les services critiques à surveiller ?
Pour faire une analyse plus fine des performances du cluster, que faut-il mettre en place ?

/!\ sondes = check = script de surveillance

Spécifier comment vous pourriez utiliser ces sondes pour vérifier les critères de disponibilités
(paramètres d'appel de ces sondes)
 
# Spécifier comment vous pourriez utiliser ces sondes pour vérifier les critères de disponibilités (paramètres d'appel de ces sondes)

On suppose que ces sondes sont des sondes classiques avec un message court sur stdout.
Il y a très peu d'informations sur les sondes, on suppose qu'elles sont bien faites et respecte les conventions vue en cours.
De plus, on suppose également que : 

- verif-noeud, donne le pourcentage sur une liste de noeud up
par exemple, si on fait `verif-noeud -H a,b,c,d` et que seul le noeud d est up, il rendra 25%
- verif-lustre-routeur, donne le débit
- verif-nodeset-ssh, donne les pourcentages, comme verif-nodeset-ssh.
C'est à dire :

```
– V version (--version)
– -h help (--help)
– -t timeout (--timeout)
– -w warning threshold (--warning)
– -c critical threshold (--critical)
– -H hostname (--hostname)
– -v verbose (--verbose)
```

TODO voir /etc/shinken/packs/linux-ssh/commands.cfg du TP (pour voir comment sont définis les checks)

```bash

# 1) Au moins un nœud de login doit être opérationnel pour chaque communauté
verif-nodeset-ssh -H [liste-noeud-login] -w 1 -c 0

# 2) Un débit minimal de 32 GB/s vers le système de stockage Lustre doit etre assuré,
verif-lustre-routeur -H [liste-noeud-lustre] -w 35 -c 31

# 3) 90% des noeuds de la partition AC doivent être disponibles
verif-noeud -H [liste-noeud-AC] -w 95 -c 89

# 4) 80% des nœuds de la partition AL,
verif-noeud -H [liste-noeud-AL] -w 85 -c 79

# 5) 60 % des nœuds de la partition AX.
verif-noeud -H [liste-noeud-AX] -w 65-c 59

```

Je trouve les pourcentages de chaque partie beaucoup trop élévé. Je ne comprend pas l'utilité de ces seuils.

https://wiki.monitoring-fr.org/shinken/shinken-advanced-architecture.html

# Proposer l'implémentation d'une sonde qui surveillera les seuils de disponibilité pour une partition slurm.

https://github.com/naparuba/check-linux-by-ssh

Nous pouvons voir que lors du tp, il était demandé d'écrire une sonde en bash. Cependant, nous pouvons voir que lors de celui-ci
nous avons également installer des plugins. 
Dont linux-ssh, qui lui a des checks écrit en python. 
Nous ferons donc l'hypothèse que nous pouvons utiliser des plugins python. 
C'est toujours du python 2... Go faire du sh 

voir `check_slurm.py`