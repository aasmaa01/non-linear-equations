# Projet d'Analyse Numérique : Résolution d'Équations Non Linéaires

##  Vue d'ensemble du projet

Ce projet académique implémente et compare trois méthodes numériques classiques pour la résolution d'équations non linéaires de la forme **f(x) = 0**. Dans le cadre de ce travail, nous résolvons l'équation :


### Membres du groupe -groupe 4 Acad B
- **Soltani Asma** `222231640602`: Méthode de Newton-Raphson + Programme principal
- **Triaki Hiba** `242431461313` : Méthode des Approximations Successives
- **Smai Numidia** `232431541807` : Méthode de Dichotomie

---

## Description des trois méthodes

### 1. Méthode de Dichotomie (Bisection)

**Implémentée par :** Numidia

**Algorithme :**
1. On part d'un intervalle [a, b] où f change de signe
2. On calcule le milieu m = (a + b) / 2
3. Si f(m)·f(a) < 0, la racine est dans [a, m], sinon dans [m, b]
4. On répète jusqu'à ce que b - a < ε

**Convergence :**
- **Ordre de convergence :** 1 (linéaire)
- **Erreur à l'itération n :** |xₙ - α| ≤ (b₀ - a₀) / 2^(n+1)
- **Avantages :** Toujours convergente si f change de signe, robuste
- **Inconvénients :** Convergence lente, nécessite un encadrement initial

---

### 2. Méthode des Approximations Successives (Point Fixe)

**Implémentée par :** Triaki Hiba

```
x_{n+1} = φ(xₙ)
```

**Conditions de convergence :**
- φ doit être contractante : |φ'(x)| < 1 sur l'intervalle d'étude
- φ doit être stable : φ([a,b]) ⊆ [a,b]

**Convergence :**
- **Ordre de convergence :** 1 (linéaire) en général
- **Erreur :** |xₙ - α| ≤ k^n |x₀ - α| où k est la constante de contraction
- **Avantages :** Simple à implémenter, flexible dans le choix de φ
- **Inconvénients :** Convergence dépend fortement du choix de φ, peut diverger

---

### 3. Méthode de Newton-Raphson 

**Implémentée par :** Soltani Asma 

**Principe théorique :**

La méthode de Newton-Raphson est basée sur l'approximation linéaire de la fonction f par son développement de Taylor au premier ordre. Soit α la racine recherchée de f(x) = 0, et xₙ une approximation de α.

### **Formule fondamentale :**
```
x_{n+1} = xₙ - f(xₙ) / f'(xₙ)
```

**Interprétation géométrique :**
Géométriquement, x_{n+1} est l'abscisse du point d'intersection de la tangente à la courbe de f au point (xₙ, f(xₙ)) avec l'axe des abscisses.


## Théorie de la Convergence

### Théorème de Newton

Soit f ∈ C²[a,b] vérifiant:

1. f(a)·f(b) < 0
2. f'(x) ≠ 0, ∀x ∈ [a,b]
3. f' et f'' gardent un signe constant sur [a,b]
4. Si on note c l'élément où f' est minimal, alors |f(c)/f'(c)| ≤ b - a

Alors la suite de Newton définie ci-dessus converge vers l'unique racine α de f sur [a,b].

De plus nous avons:

```
|x_{n+1} - α| ≤ (M/2m)|xₙ - α|²
```

où M = sup|f''| et m = inf|f'| sur [a,b].

### Théorème de Newton-Raphson (Globale)

Soit [a,b] un intervalle non vide de ℝ, et une fonction f ∈ C²[a,b] changeant de signe sur [a,b] et telle que:
- f'(x) ≠ 0, ∀x ∈ [a,b]
- f''(x) ≠ 0, ∀x ∈ [a,b]

Alors pour toute initialisation x₀ ∈ [a,b] vérifiant f(x₀)·f''(x₀) ≥ 0, la suite de Newton:

```
x_{k+1} = xₖ - f(xₖ)/f'(xₖ)
```

converge vers l'unique racine de f sur [a,b].

### Ordre de Convergence

Soit une suite (xₖ) de réels convergeant vers une limite ζ. On dit que cette suite est convergente vers ζ avec un ordre r (r > 1) s'il existe un réel μ > 0 appelé constante asymptotique d'erreur, tel que:

```
lim   |x_{k+1} - ζ|     
k→∞  ______________ = μ
      |xₖ - ζ|^r
```

Dans le cas particulier où:
- r = 1: la convergence est dite linéaire
- r = 2: la convergence est dite quadratique
- r = 3: la convergence est dite cubique

La méthode de Newton est au moins d'ordre 2, elle est dite d'une convergence au moins quadratique.

### Comparaison avec les Autres Méthodes

1. Méthode de Dichotomie:
   - Ordre: 1 (linéaire)
   - Convergence relativement lente
   - Intéressante pour localiser la racine

2. Méthode de Newton:
   - Ordre: 2 (convergence quadratique)
   - Meilleure performance
   - Nécessite une bonne initialisation de x₀
   - Nécessite le calcul des dérivées

3. Méthode du Point Fixe:
   - Ordre: au moins 1
   - Offre le plus de possibilités avec un bon choix de la fonction φ
   - La méthode de Newton en est un cas particulier

---


## Installation

### Prérequis

- Python 3.7 ou supérieur
- pip

### Installation des dépendances

```bash
pip install -r requirements.txt
```

Ou manuellement:

```bash
pip install numpy matplotlib
```

---

## Utilisation

### Interface en Ligne de Commande

```bash
python main.py

# Spécifier une fonction
python main.py --function poly5

# Sauvegarder les graphiques
python main.py --function sqrt2 --save-plots
```

### Mode Interactif

```bash
python main.py --interactive
```

### Lister les Fonctions Disponibles

```bash
python main.py --list
```

