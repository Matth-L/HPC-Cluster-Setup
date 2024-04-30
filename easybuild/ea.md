# Réponse 

## Développement Intel complet

Il n'est pas précisé qu'est ce qui est entendu par le mot "complet". 
Nous supposons donc qu'un environnement X complet comprend tout ce qui 
peut être nécessaire, de proche ou de loin, pour faire du développement afin
que l'utilisateur n'est jamais à devoir installer un paquet.

Premièrement , il est nécessaire d'installer la toolchain GCCcore, comme indiqué dans 
le diagramme de Toolchain d'easybuild (https://docs.easybuild.io/common-toolchains/#common_toolchains_what).

Ensuite, nous installerons la toolchain intel, celle-ci comportera : 

- leur compilateur C/C++/Fortant
- leur libraire MPI d'Intel
- leur librairie "Math Kernel"
- binutils et gcc, qui seront la base de leurs compilateurs.

A cette toolchain, nous rajouterons également, différentes toolchain utile pour le 
développement. Il n'est pas précisé si ceux-ci sont comprises dans les dernières versions 
de la toolchain. Ne trouvant pas cette informations, nous décidons donc de les rajouter.

Nous ajouterons : 

- IntelPython, permettant d'améliorer les performances d'un code Python par le biais d'Anaconda.
- IntelDALL, qui ajoute une optimisation lors de l'analyse de données, cela n'est pas directement
lié à l'environnement de développement mais de nombreux code en auront besoin.
- IntelCuda, afin d'ajouter CUDA aux compilateurs fourni de base.

## Développement GNU de base

Pour un environnement de développement GNU de base, il sera nécessaire d'installer la toolchain 
GNU, celle-ci comprend uniquement des compilateur GCC et binutils. Il est demandé un développement 
GNU de base, cela semble donc suffisant.

## Développement pour codes accélérés par GPU/NVIDIA

Pour la partie code accélérés, nous installerons, la toolchain CUDA, contenant la CUDA-toolkit, 
permettant aux utilisateur d'avoir accès aux instructions nécessaire aux développements GPU.
De plus, nous installerons également la toolchain CUDACompat, cela permettra aux utilisateurs 
ayant le besoin d'utiliser des versions de CUDA, plus ou moins récentes, de pouvoir le faire 
plus facilement, comme indique le site de NVIDIA (https://docs.nvidia.com/deploy/cuda-compatibility/index.html).


## MATLAB et MATLAB-ENGINE

Enfin , afin d'avoir accès au version récente de MATLAB ainsi que de MATLAB-ENGINE nous installerons les toolchains,
MATLAB, qui comporte l'environnement interactif demandé, ainsi que l'API Python nommé MATLAB-ENGINE.
Nous pouvons voir que MATLAB-ENGINE nécessite une toolchain différentes (GCCcore/11.2.0), cela risque de 
nous forcer à choisir cette version pour des problèmes de compatibilité. 

*PAS GIGA SUR DE CETTE PARTIE*

# Dans quels types de systèmes de fichiers pouvez-vous installer ces produits ? Préciser les avantages et inconvénients.

Cela sera directement dans les noeuds de login, ceux-ci possèdent des disques durs, ils seront accessible en lecture seule. Afin que les utilisateurs aient facilement 
accès à leurs environnement. Le système de fichier est donc ext4. 
L'avantage de cette solution est la localité des environnements, permettant donc un accès plus rapide et le fait de ne pas surcharger le réseau. 
L'inconvénient est la mise à jour qu'il faudra faire sur chaque machine. 

Pour cela nous proposons de mettre des "mirrors" sur certains noeuds de services contenant les paquets à mettre à jour. Il suffira alors d'utiliser un crontab
demandant à puppet de faire des mises à jour régulièrement. De plus, cela permettra aux administrateurs d'approuver les versions et de facilement décliner une mise à jour.

### Remarque

Nous pouvons remarquer que la majorité de ces toolchains sont estampillés sous le nom de 
la toolchain system dans la documentation easybuild.

