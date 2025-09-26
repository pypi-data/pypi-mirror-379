# Installation d'UPAS CLI via les Packages Debian

Ce guide explique comment installer UPAS CLI en utilisant les packages Debian pré-construits disponibles dans les releases GitHub.

## Architectures Supportées

UPAS CLI fournit des packages Debian pour trois architectures principales :

### 🖥️ AMD64 (Intel/AMD 64-bit)

- **Fichier** : `upas-cli_X.Y.Z-1_amd64.deb`
- **Compatible** : PC de bureau, serveurs Intel/AMD, machines virtuelles
- **Commande** : `uname -m` affiche `x86_64`

### 🔧 ARMHF (ARM 32-bit Hard Float)

- **Fichier** : `upas-cli_X.Y.Z-1_armhf.deb`
- **Compatible** : Raspberry Pi (ancien), systèmes embarqués ARM 32-bit
- **Commande** : `uname -m` affiche `armv7l` ou similaire

### 📱 ARM64 (ARM 64-bit)

- **Fichier** : `upas-cli_X.Y.Z-1_arm64.deb`
- **Compatible** : Raspberry Pi 4+, Apple Silicon (sous Linux), serveurs ARM64
- **Commande** : `uname -m` affiche `aarch64`

## Installation Rapide

### 1. Détecter votre architecture

```bash
uname -m
```

### 2. Télécharger le package approprié

```bash
# Pour AMD64
wget https://github.com/BitsDiver/upas-cli/releases/latest/download/upas-cli_1.0.6-1_amd64.deb

# Pour ARM64 (Raspberry Pi 4+)
wget https://github.com/BitsDiver/SignalMiners/Reverse/upas-cli/releases/latest/download/upas-cli_1.0.6-1_arm64.deb

# Pour ARMHF (Raspberry Pi ancien)
wget https://github.com/BitsDiver/SignalMiners/Reverse/upas-cli/releases/latest/download/upas-cli_1.0.6-1_armhf.deb
```

### 3. Installer le package

```bash
sudo dpkg -i upas-cli_*.deb

# Si des dépendances manquent
sudo apt-get install -f
```

### 4. Vérifier l'installation

```bash
upas --version
upas --help
```

## Installation Détaillée

### Prérequis Système

- **OS** : Ubuntu 18.04+, Debian 10+, Raspberry Pi OS
- **Python** : Version 3.7 ou supérieure (généralement pré-installé)
- **Espace disque** : ~50 MB

### Vérification des prérequis

```bash
# Vérifier Python
python3 --version

# Vérifier l'espace disque
df -h /usr
```

### Installation pas à pas

1. **Mise à jour du système**

```bash
sudo apt-get update && sudo apt-get upgrade
```

2. **Téléchargement du package**

```bash
# Remplacer X.Y.Z par la version actuelle et ARCH par votre architecture
ARCH=$(dpkg --print-architecture)
VERSION="1.0.6"
wget "https://github.com/BitsDiver/upas-cli/releases/download/v${VERSION}/upas-cli_${VERSION}-1_${ARCH}.deb"
```

3. **Installation**

```bash
sudo dpkg -i upas-cli_*.deb
```

4. **Résolution des dépendances (si nécessaire)**

```bash
sudo apt-get install -f
```

## Structure d'Installation

Après installation, UPAS CLI est disponible à ces emplacements :

### Exécutable

- `/usr/bin/upas` - Commande principale

### Documentation

- `/usr/share/doc/upas-cli/README.md` - Documentation principale
- `/usr/share/doc/upas-cli/WIKI.md` - Guide complet
- `/usr/share/doc/upas-cli/SPECIFICATIONS.md` - Spécifications techniques

### Exemples et Protocoles

- `/usr/share/upas-cli/examples/` - Fichiers d'exemple
- `/usr/share/upas-cli/protocols/` - Définitions de protocoles

### Configuration

- `/etc/upas/` - Répertoire de configuration système

## Utilisation de Base

### Commandes essentielles

```bash
# Affichage de l'aide
upas --help

# Version installée
upas --version

# Lister les protocoles disponibles
ls /usr/share/upas-cli/protocols/

# Exécuter un exemple
upas run /usr/share/upas-cli/examples/simple_test_protocol.json
```

### Exemples Disponibles

```bash
# Protocoles de découverte
upas run /usr/share/upas-cli/protocols/behaviors/discovery/arp_discovery.json

# Protocoles IoT
upas run /usr/share/upas-cli/examples/iot_discovery.json

# Protocoles industriels
upas run /usr/share/upas-cli/examples/modbus_simulation.json
```

## Dépannage

### Erreurs Communes

**"Package has bad or weak signature"**

```bash
# Ignorer temporairement la vérification de signature
sudo dpkg -i --force-bad-version upas-cli_*.deb
```

**"Python3 not found"**

```bash
# Installer Python 3
sudo apt-get install python3 python3-pip
```

**"Permission denied" lors de l'exécution**

```bash
# Vérifier les permissions
ls -la /usr/bin/upas

# Réinstaller si nécessaire
sudo dpkg --purge upas-cli
sudo dpkg -i upas-cli_*.deb
```

### Diagnostic

```bash
# Vérifier le statut du package
dpkg -s upas-cli

# Lister tous les fichiers installés
dpkg -L upas-cli

# Vérifier les dépendances
apt-cache depends upas-cli
```

## Désinstallation

### Suppression complète

```bash
# Désinstaller le package
sudo dpkg --purge upas-cli

# Nettoyer les dépendances orphelines
sudo apt-get autoremove

# Supprimer la configuration (optionnel)
sudo rm -rf /etc/upas/
```

### Suppression simple

```bash
sudo apt-get remove upas-cli
```

## Mise à Jour

### Vers une nouvelle version

```bash
# Télécharger la nouvelle version
wget https://github.com/BitsDiver/upas-cli/releases/latest/download/upas-cli_X.Y.Z-1_amd64.deb

# Installer par-dessus l'ancienne version
sudo dpkg -i upas-cli_*.deb
```

### Vérification de version

```bash
# Version actuelle
upas --version

# Dernière version disponible
curl -s https://api.github.com/repos/BitsDiver/upas-cli/releases/latest | grep tag_name
```

## Support Multi-Architecture

### Raspberry Pi

```bash
# Pi 4, 400, CM4 (64-bit OS)
wget https://github.com/BitsDiver/upas-cli/releases/latest/download/upas-cli_1.0.6-1_arm64.deb

# Pi 3, Zero 2 (32-bit OS)
wget https://github.com/BitsDiver/upas-cli/releases/latest/download/upas-cli_1.0.6-1_armhf.deb

# Pi Zero, Pi 1 (32-bit OS)
wget https://github.com/BitsDiver/upas-cli/releases/latest/download/upas-cli_1.0.6-1_armhf.deb
```

### Docker

```bash
# Conteneur multi-architecture
docker run --rm -v $(pwd):/workspace bitsdiver/upas-cli:latest upas --help
```

## Alternatives d'Installation

### Via pip (si les packages Debian ne conviennent pas)

```bash
pip install upas-cli
```

### Via le code source

```bash
git clone https://github.com/BitsDiver/upas-cli.git
cd upas-cli
pip install -e .
```

---

**Support** : Pour toute question, ouvrir une issue sur [GitHub](https://github.com/BitsDiver/upas-cli/issues)

**Documentation complète** : Consultez `/usr/share/doc/upas-cli/` après installation
