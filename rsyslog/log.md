Le lien pour edit le canva : https://www.canva.com/design/DAGEJ69bZyc/BFuKducBjQHTnk9WHpM0zg/edit

# 4.8

Le fichier de log vient du cluster et a été modifié.

Je n'ai pas pensé à l'architecture encore, ni au code conf des calculs.

Le fichier de configuration des serveurs devrait être ok je pense.

Pour la centralisation des consoles, dans le cours il parle de conman, 
j'ai donc essayé de l'utiliser.

Il reste à faire la partie rédaction et choix du graphique.

## je pense qu'il ne manque plus que l'architecture et cette partie est good
# début de réponse structuré ( sans architecture )

Lors de cette partie, il nous est demandé de mettre en place un serveur de log centralisé.
Il est demandé que les fichiers de journaux soit organisés en utilisant une arborescence permettant de distinguer facilement les machines qui ont généré les logs. Les logs seront donc stockés de cette manière. De plus, différents logs seront crées en fonction de leurs urgences. Ils ont séparé selon leurs différentes classes (0 à 7). Les logs de classe 0 sont les plus urgents et les logs de classe 7 sont les moins urgents. Ainsi, un administrateur pourra facilement les répérer.


Les noeuds de services sont ceux qui génèrent les logs. Leurs configurations est dans le fichier rsyslog_service.conf.
Un template est également utilisé sur les logs afin que ceux-ci soient analysés par un logiciel de visualisation de logs tel qu'open search , ou la version payante , Elasticsearch.

Le logiciel interactif permettant l'accès au console est conman. Il permet de visualiser les logs de plusieurs machines en même temps.

Pour la politique de gestion des journaux du cluster : 

- Les codes d'erreurs allant de 0 à 2 sont des erreurs critiques. Ils seront "rotate" et compressés tous les mois, et supprimés au bout de 2 mois. Les problèmes critiques doivent être résolus rapidement. Cependant, nous pensons qu'il est important d'avoir accès à ceux-ci rapidement en cas de problème similaire, ou redondant sur une période de temps relativement longue. c'est pourquoi nous les stockerons stockés 1 an. Ce sont censés être les messages les moins nombreux, et les plus importants.
- Les codes d'erreur de niveau 3 sont non-urgent, mais doivent être traités rapidement. Ils seront "rotate" et compressés tous les mois, et supprimés au bout de 6 mois.
- Les autres sont non important et risque également d'être les plus lourds, ils ne seront stockés qu'un mois. 

(cf. logrotate.conf)



# Relire la proposition technique de AzkarHPC et proposer un espace de stockage adéquat pour le répertoire /var/cluster/ .

NFS 



# partie SOUPE

Pour des raisons de scalabilité, le serveur NFS est choisi pour stocker les logs en raison de sa capacité de stockage. D'après la configuration proposée par AzkarHPC, il y a un seul serveur NFS, ce qui en fait un SPOF, il est donc vivement encouragé de faire un serveur NFS redondant comme évoqué précédemment.

Le serveur NFS a pour rôle de stocker les logs. Il est tout à fait possible pour les noeuds de calcul d'envoyer directement les logs au NFS, mais il faudrait pour cela un démon rsyslog sur le serveur NFS qui gèrerait la politique de décision (savoir dans quel fichier va quel log). Afin d'éviter de faire des capacités de calcul (inconnues) du serveur NFS un SPOF, la politique de décision est confiée au noeuds de service. Aucun démon rsyslog ne tourne sur le NFS.

Les noeuds de service sont non seulement en charge de la politique de décision, mais aussi du logrotate (car la compression demande aussi des ressources CPU). Ainsi, les logs générés par tous les noeuds du réseau IB seront envoyés aux noeuds de service (via le réseau IB), qui se chargeront de décider où les stocker. Sur ces noeuds de service, un (ou plusieurs, je sais pas encore) répertoire de logs est monté en NFS, le noeud de service décide simplement où placer les logs dans ce répertoire, les logs sont alors envoyés des noeuds de service au NFS sur le réseau d'administration (d'où le choix d'envoyer les logs aux noeuds de service via le réseau IB, pour éviter de doubler le trafic sur le réseau d'administration).

Comme il y a 4 switches d'administration reliés directement au NFS, nous décidons, pour des raisons de débit sur le réseau d'administration, d'attribuer la gestion des logs à 4 noeuds de service, un sur chacun de ces switches.

Dans cette configuration, on peut cependant relever un problème : comme le logrotate compresse les logs à heure fixe, une grande quantité de logs est compressée à chacune de ces heures. Ce qui signifie qu'une grande quantité de logs est envoyée par le NFS aux noeuds de service, compressée sur ces noeuds de service puis renvoyée au NFS, ce qui pourrait saturer régulièrement le réseau d'administration.

Si les capacités de calcul du serveur NFS étaient connues et qu'elles s'avéraient suffisantes, il serait envisageable de lui attribuer la politique de décision et le logrotate, ainsi les noeuds de service n'auraient même plus besoin de servir d'intermédiaire, et les noeuds du réseau IB pourraient envoyer leurs logs directement au NFS via le réseau d'administration. Dans ce cas, les noeuds de service ne fourniraient qu'un accès en lecture au NFS. Ne connaissant pas la capacité de calcul du serveur NFS, cette solution n'est pas retenue. La solution retenue est celle évoquée dans les paragraphes ci-dessus, malgré le problème de réseau.

Les fichiers de configuration diffèreront sur les noeuds de calcul et les autre noeuds : tous les logs des autres noeuds seront enregistrés, seuls les logs évoquant un problème seront envoyés par les noeuds de calcul.
