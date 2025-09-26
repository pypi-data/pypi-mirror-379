# 📈 finance-ml

Un mini-projet d'apprentissage automatique en Python, construit avec [Poetry](https://python-poetry.org/) et testé automatiquement avec [pytest](https://docs.pytest.org/) et [GitHub Actions](https://docs.github.com/en/actions).

## 🚀 Objectifs du projet
- Mettre en place une structure de projet Python propre.
- Implémenter pas à pas des algorithmes de machine learning appliqués à la finance.
- Apprendre à écrire des tests unitaires avec **pytest**.
- Automatiser l’intégration continue (CI) avec **GitHub Actions**.

## 📂 Structure du projet
finance-ml/
├── .github/workflows/ # Workflows GitHub Actions (tests automatiques)
├── src/my_package/ # Code source du package
│ ├── init.py
│ └── linear_models.py
├── tests/ # Tests unitaires
│ ├── init.py
│ └── test_linear_models.py
├── pyproject.toml # Configuration du projet (Poetry)
├── poetry.lock # Verrouillage des dépendances
└── README.md # Documentation du projet

## ⚙️ Installation

Cloner le projet :
```bash
git clone https://github.com/Antoine-Moniz/finance-ml.git
cd finance-ml

Installer les dépendances avec Poetry :
poetry install

Activer l’environnement virtuel :
poetry shell

Fonctionnalités
Implémentées

Régression linéaire (LinearRegression) :

Avec ou sans intercept

Méthode des moindres carrés

Prédictions sur de nouvelles données

Tests

Lancer les tests unitaires avec :

poetry run pytest

🔄 Intégration Continue (CI)

Chaque push ou pull request déclenche automatiquement les tests via GitHub Actions.
Voir l’onglet Actions
 pour consulter l’historique des exécutions.