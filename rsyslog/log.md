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