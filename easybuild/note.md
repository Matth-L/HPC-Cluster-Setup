Grâce aux réunions avec les futurs développeurs et utilisateurs de la machine, vous avez identifié
les besoins suivants :
• un environnement de développement Intel complet
• un environnement de développement GNU de base
• un environnement de développement pour des codes accélérés par GPU/NVIDIA .
• Une version récente de MATLAB et MATLAB-Engine

Vous anticipez d'autres demandes et décidez d'utiliser EasyBuild pour générer et offrir 
les environnements logiciels voulus. Précisez les toolchains que vous utiliserez et les produits que
vous offrirez avec leurs versions. Vous trouverez les informations adéquates sous :
https://docs.easybuild.io/en/latest/version-specific/Supported_software.html
Dans quels types de systèmes de fichiers pouvez-vous installer ces produits ? Préciser les
avantages et inconvénients.

## Réponse

(un problème au niveau de la date des versions, j'ai essayé de prendre les plus récentes)

Il marque pas les dépendances sur le site... assez chiant.

### Environnements de développement (Intel)

Pour environnement de dev Intel complet: Par complet on comprend tout ce qui peut être nécessaire de proche ou de loin pour faire du dev.

Sans réfléchir j'aurais dl tous les paquests qui iraient avec Intel.

Liste de tt les packets commençant par intel : 

Il faut installer GCCcore en premier d'après la toolchain diagram (je pense que sans, il s'isntalle juste tout seul mais bon) https://docs.easybuild.io/common-toolchains/#common_toolchains_what

Ce que j'aurais gardé : 

- `intel-compilers` car mène directement vers le site HPC intel et est mis à jour le plus récemment 

- `IntelDAAL` Intel® Data Analytics Acceleration Library (Intel® DAAL) is the library of Intel® architecture optimized building blocks covering all stages of data analytics: data acquisition from a data source, preprocessing, transformation, data mining, modeling, validation, and decision making.

- `IntelPython` Intel® Distribution for Python. Powered by Anaconda. Accelerating Python* performance on modern architectures from Intel.

---------------------------------------------------

- `intel` (version 2023b) Contient les compilatuers Intels, MPI, Math Kernel Library. Les compilateurs intels sont la toolchain intel-compilers càd : Intel C, C++ & Fortran compilers (classic and oneAPI).

 à l'air d'être le 2e le plus à jour, ce qui me dérange est que son compilateur a reçu une maj en 2024, mais ça date la plus récente est 2023.
 donc peut etre pas le plus à jour, mais le plus général.

semble posséder `intel-compilers`, qui lui a recu une maj en 2024 et qui possède C++, Fortran, OpenMP*, and MPI.

- `intelcuda` (version 2020b) Intel Cluster Toolkit Compiler Edition provides Intel C/C++ and Fortran compilers, Intel MPI & Intel MKL, with CUDA toolkit

(cuda jsp car y a un package cuda déjà)

tout à pas l'air a jour de fou, a voir pk. Risque d'avoir pas mal de doublon peut être , à voir comment gérer cela pour éliminer ce qui semble inutile.

### Environnements de développement (GNU)

Toolchain utilisés : 

- `GNU` Compiler-only toolchain with GCC and binutils. (version : 5.1.0-2.25	) 

## Environnements de développement pour des codes accélérés par GPU/NVIDIA

Toolchain utilisé :

- `cuda`
- `CUDAcompat` pour régler les problèmes de compatibilité si certains codes ne sont pas compatibles avec les versions récentes de CUDA.

## MATLAB et MATLAB-Engine

- `MATLAB`
- `MATLAB-Engine` (API python)


fin globalement la toolchain system install tout ce que j'ai dit plus haut

sauf matlabengine et proxy qui sont en GCCcore/11.2.0 et GCCcore/11.3.0

ça, ça force la version de gcc je pesne ou ça introduit des pb de compatbilité, à voir.