# Guide de Construction des Packages Debian UPAS CLI

Ce guide explique comment construire des packages Debian pour UPAS CLI sur plusieurs architectures (amd64, armhf, arm64).

## Vue d'ensemble

UPAS CLI utilise un système de construction automatisé qui génère des packages Debian pour trois architectures principales :

- **amd64** : Intel/AMD 64-bit (serveurs, PC de bureau)
- **armhf** : ARM 32-bit hard-float (Raspberry Pi, systèmes embarqués anciens)
- **arm64** : ARM 64-bit (Raspberry Pi 4+, Apple Silicon, serveurs ARM)

## Prérequis

### Système Ubuntu/Debian

```bash
# Outils de base
sudo apt-get update
sudo apt-get install -y build-essential debhelper dh-python python3-setuptools

# Pour la compilation croisée ARM
sudo apt-get install -y gcc-arm-linux-gnueabihf gcc-aarch64-linux-gnu
sudo apt-get install -y qemu-user-static

# Outils Python
pip install build setuptools wheel
```

## Méthodes de Construction

### 1. Via Makefile (Recommandé)

```bash
# Construction pour une architecture spécifique
make debian-amd64    # Package pour x86_64
make debian-armhf    # Package pour ARM 32-bit
make debian-arm64    # Package pour ARM 64-bit

# Construction pour toutes les architectures
make debian-all

# Nettoyage
make debian-clean
```

### 2. Via Script Direct

```bash
# Rendre le script exécutable
chmod +x scripts/build-debian.sh

# Construction
./scripts/build-debian.sh amd64    # Ou armhf, arm64, all
```

### 3. Via Générateur de Configuration

```bash
# Génération manuelle des fichiers de configuration
python3 scripts/generate-debian-config.py --arch amd64 --clean

# Construction manuelle
dpkg-buildpackage -us -uc
```

## Structure des Packages

Les packages Debian incluent :

### Binaires

- `/usr/bin/upas` - Exécutable principal
- `/usr/lib/python3/dist-packages/upas/` - Modules Python

### Documentation

- `/usr/share/doc/upas-cli/README.md`
- `/usr/share/doc/upas-cli/WIKI.md`
- `/usr/share/doc/upas-cli/SPECIFICATIONS.md`

### Exemples et Protocoles

- `/usr/share/upas-cli/examples/` - Fichiers d'exemple
- `/usr/share/upas-cli/protocols/` - Définitions de protocoles

### Configuration

- `/etc/upas/` - Répertoire de configuration (créé lors de l'installation)

## Architecture Cross-Compilation

### Compilation Croisée ARM

Le système utilise les compilateurs croisés GCC :

```bash
# Pour armhf (ARM 32-bit)
export CC=arm-linux-gnueabihf-gcc
export DEB_HOST_ARCH=armhf
export DEB_HOST_GNU_TYPE=arm-linux-gnueabihf

# Pour arm64 (ARM 64-bit)
export CC=aarch64-linux-gnu-gcc
export DEB_HOST_ARCH=arm64
export DEB_HOST_GNU_TYPE=aarch64-linux-gnu
```

### Émulation QEMU

Les packages utilisent `qemu-user-static` pour l'émulation lors des tests d'installation.

## Fichiers de Configuration Debian

### debian/control

Définit les métadonnées du package :

- Nom, version, description
- Dépendances Python (>= 3.7)
- Architecture cible

### debian/rules

Script de construction :

- Installation des modules Python
- Copie des protocoles et exemples
- Installation de la documentation

### debian/postinst

Script post-installation :

- Création de `/etc/upas/`
- Messages d'information utilisateur

## Test des Packages

### Installation Locale

```bash
# Installation du package
sudo dpkg -i ../upas-cli_1.0.7-1_amd64.deb

# Résolution des dépendances si nécessaire
sudo apt-get install -f

# Test des commandes
upas --version
upas --help
```

### Test Automatisé

```bash
make debian-test-install
```

## Intégration CI/CD

Le workflow GitHub Actions (`.github/workflows/publish.yml`) automatise :

1. **Construction PyPI** - Package Python standard
2. **Construction Debian** - Packages pour amd64, armhf, arm64
3. **Publication** - Release sur GitHub avec tous les artifacts

### Déclenchement

```bash
# Créer une release pour déclencher la publication
git tag 1.0.7
git push origin 1.0.7

# Créer une release GitHub depuis l'interface web
```

## Dépannage

### Erreurs Communes

**Compilateur croisé manquant :**

```bash
sudo apt-get install gcc-arm-linux-gnueabihf gcc-aarch64-linux-gnu
```

**Outils Debian manquants :**

```bash
sudo apt-get install build-essential debhelper dh-python
```

**Erreurs de dépendances Python :**

```bash
sudo apt-get install python3-setuptools python3-dev
```

### Logs de Construction

Les logs détaillés sont disponibles dans :

- Terminal pour construction locale
- GitHub Actions logs pour CI/CD

### Test Manuel

```bash
# Vérification de la structure du package
dpkg -c ../upas-cli_*.deb

# Informations du package
dpkg -I ../upas-cli_*.deb

# Test d'installation en mode simulation
sudo dpkg -i --dry-run ../upas-cli_*.deb
```

## Publication

### Packages Locaux

Les packages sont générés dans le répertoire parent :

```
../upas-cli_1.0.7-1_amd64.deb
../upas-cli_1.0.7-1_armhf.deb
../upas-cli_1.0.7-1_arm64.deb
```

### GitHub Releases

Les packages sont automatiquement attachés aux releases GitHub :

- `upas-cli_v1.0.7-1_amd64.deb`
- `upas-cli_v1.0.7-1_armhf.deb`
- `upas-cli_v1.0.7-1_arm64.deb`

## Distribution

### Référentiels APT (Futur)

Possibilité d'héberger un référentiel APT pour faciliter l'installation :

```bash
# Ajout du référentiel (exemple)
echo "deb https://apt.bitsdiver.com/ stable main" | sudo tee /etc/apt/sources.list.d/upas.list

# Installation via APT
sudo apt-get update
sudo apt-get install upas-cli
```

### Installation Directe

```bash
# Téléchargement et installation
wget https://github.com/BitsDiver/upas-cli/releases/latest/download/upas-cli_1.0.7-1_amd64.deb
sudo dpkg -i upas-cli_1.0.7-1_amd64.deb
```

## Maintenance

### Mise à Jour des Versions

1. Modifier `pyproject.toml` avec la nouvelle version
2. Créer une release Git
3. Les packages sont automatiquement générés par CI/CD

### Mise à Jour des Dépendances

- Modifier `debian/control` si nécessaire
- Tester sur toutes les architectures
- Valider la compatibilité

---

_Ce guide est maintenu par l'équipe BitsDiver pour UPAS CLI v1.0.7+_
