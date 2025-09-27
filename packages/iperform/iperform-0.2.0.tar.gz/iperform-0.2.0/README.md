
# iperform - Performance Intelligence for Business & Data Teams

![iperform logo](images/iperform_avatar.png)

![PyPI](https://img.shields.io/pypi/v/iperform.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/iperform)
![Python Version](https://img.shields.io/pypi/pyversions/iperform)
![License](https://img.shields.io/pypi/l/iperform)
![Bilingual: FR/EN](https://img.shields.io/badge/langues-FR%20|%20EN-blue)

---

## ✍🏽 Autor

ILUNGA BUABUA Patrick

[🇬🇧 Go to English](#-english) | [🇫🇷 Aller au Français](#-français)

<br><br>

## 🇬🇧 English

*Monitor, Decide, act - with precise KPIs, smart alerts, and reliable forecasts. In a few lines code.*

## 🚀 Overview

`iperform` is a Python package designed to turn your raw business data (Key Parameters - KPs) into actionable performance metrics (Key Performance Indicators - KPIs).  

Built for business, marketing, finance, and data teams who need to :

- 📊 Monitor operational performance (WTD, MTD, YTD, ...),
- 📈 Detect critical variations and trigger alerts,
- 🔮 Forcast future trends using statistical models or business rules,
- 🧹 Clean and validation data (missing, outliers, anomalies, ...),  
- 🖼️ Visualize KPIs and KPs clearly and impactfully.

💡 Advanced features as AI-powered forecasting (SARIMAX, LSTM, ...) or budgeting tools are in the SaaS/Premium edition **iperform[saas]**.

## ✨ Core functionality

`iperform` provides a comprehensive set of functions to extract time series values and dynamic performance indicator for any given reference date - enabling real-time operational reporting and decision-making.

Key functions include :  

- `mtd()` - Month-To-Date : Cumulative sum from the first day of the month up to reference date.
- `ytd()` - Year-To-Date : Cumulative sum from January 1st up to reference date.
- `get_summary_day()` - Returns 8+ dynamic KPIs for given day : curent value (D-Day), D-1, D-7, MTD, ∆ MTD, ... etc. 
  -> Also available : `get_summary_month()`, `get_summary_quarter()` for higher-level reporting
- `get_columns_day()` - Generate dynamic column headers for daily dashbords based on the reference date.
- `grand_trend_day()` - Creates interactive visualizations to explore trends and anomalies.
- `forecast_m()` - Predicts the full-month total based on current MTD performance, using statistical extrapolation or business rules.

All functions are designed for plug-and-play analytics - turning raw time-series data into actionable business insights with minimal code.


## 📦 Installation

Install the iperform package via PyPI :

```bash
pip install iperform
```

## 🧩 Examples

```python

import numpy as np
import pandas as pd
import iperform as ip

# Data
np.random.seed(1234)
date = pd.date_range("2023-01-01", periods=522, freq="D")
revenu = np.random.normal(50, 6.3, 522)
df = pd.DataFrame({"date": date, "revenu": revenu, "zone": "all_zone", "factor": "Orange"})

```

`mtd()` - Month-To-Date

Calculates the sum (or cumulative value) from the 1st of the month to the specified date.

```python

result = ip.mtd(data=df, date="2023-01-15", value="revenu", zone="all_zone", cumul=False, decimal=2)
print(f"Revenu MTD on January 15 : {result} USD")
# Example of output - MTD on January 15 : 745.61 USD

```

`forecast_m()` - Monthly Forecasts

Estimates the monthly total by extrapolating the observed daily average.

```python

projection = ip.forecast_m(data=df, date="2023-01-15", value="revenu", zone="all_zone", decimal=2)
print(f"Monthly forecast : {projection} USD")
# Example of output - Monthly forecast : 1540.93 USD

```

`get_summary_day()` - Daily summary (8 indicators)

Returns a list of 8 key indicators for a given date: daily value, previous day (D-1), previous week (D-7), MTD, growth rates, etc.

```python

summary = ip.get_summary_day(df=df, date="2023-03-21", zone="all_zone", factor="Orange", value="revenu")
labels = ["D-7", "D-1", "D-Day", "∆ DoD", "∆ DoD-7", "MTD-1", "MTD", "∆ MTD"]
for label, val in zip(labels, summary):
    print(f"{label}: {val}")
# Example of output -
# D-7: 54.437
# D-1: 53.981
# D-Day: 50.249
# ∆ DoD: -0.069
# ∆ DoD-7: -0.077
# MTD-1: 1070.639
# MTD: 1067.452
# ∆ MTD: -0.003

```

`get_summary_month()` - Monthly summary (8 indicators)

Returns a list of 8 key indicators for a given month: current month, previous month, same month last year (Y-1), YTD, and growth rates (MoM, YoY, etc.).

```python

summary_month = ip.get_summary_month(df=df, date="2024-04-30", factor="Orange",  value="revenu", decimal=2)
labels_month = ["M-12", "M-1", "M", "∆ SPLM", "∆ SPLY", "YTD-1", "YTD", "∆ YTD"]
for label, val in zip(labels_month, summary_month):
    print(f"{label}: {val}")
# Example of output -
# M-12: 1487.24
# M-1: 1514.23
# M: 1474.21
# ∆ SPLM: 0.01
# ∆ SPLY: -0.01
# YTD-1: 6025.71
# YTD: 5942.99
# ∆ YTD: -0.01

```

`get_columns_day()` - Generation of column titles (Daily dashboard)

Generates column names for a daily dashboard, based on a reference date.

```python

# Generate the titles for January 15, 2023
columns = get_column_day(date_ref="2023-01-15")
print("Column headers :")
print(columns)
# Example of output -
# Column headers :
# ['KPIs', '8-janv.', '14-janv.', '15-janv.', '∆ DoD', '∆ SDLW', 'MTD-1', 'MTD', '∆ MTD']

```

`get_columns_day()` + `get_summay_day()` - Generation of Daily dashboard

Create a dashboard with dynamic column name.

```python

date_ref = "2023-03-21"
columns = ip.get_column_day(date_ref)[1:9]
summary_day = ip.get_summary_day(df=df, date=date_ref, zone="all_zone", factor="Orange", value="revenu", decimal=3)
df_summary = pd.DataFrame([summary_day], columns=columns)
print(df_summary)
# Example of output -
# 14-mars  20-mars  21-mars  ∆ DoD  ∆ SDLW     MTD-1       MTD  ∆ MTD
#  54.437   53.981   50.249 -0.069  -0.077  1070.639  1067.452 -0.003

```

`delta()` - Relative change

Computes the percentage change of value x relative to value y.

```python

# Absolute difference (even if y=0)
print(ip.delta(x=100, y=0, abs=True))
# Example of output - 100.0

# Normalization: compare February (28d) vs January (31d), reduced to 30d
print(ip.delta(x=280, y=310, abs=False, nx=28, ny=31, nn=30))
# Example of output - 0.0

```

## 📄 Documentation

See [documentation]() and [notebooks]()
Report a bug or request a feature : [GitHub Issues]() 


## Contribute

All contributions are welcome !
Whether it's to fix a bug, add a new feature, or improve the documentation. 

Consulte le fichier [CONTRIBUTING.md]()  pour commencer.


## Contact 

- Github : https://github.com/ipatriqIP/iperform
- Auteur : buabua@internet.ru
- Licence : MIT 


<br><br>

## 🇫🇷 Français

*Piloter, décider, agir - avec des KPIs précis, des alertes intélligentes, et des prévisions fiables. En quelques lignes de code.*

## 🚀 Présentation

`iperform` est un package Python conçu pour transformer vos données brutes (Key Parameters - KPs) en indicateurs actionnables (Key Performance Indicators - KPIs).

Il s'adresse aux équipes business, marketing, finance et data qui doivent :  

- 📊 Piloter la performance opérationnelle (WTD, MTD, YTD, ...),  
- 📈 Détecter les variations critiques et les alertes,  
- 🔮 Prédire les tendances futures avec des modèles statistiques ou des règles métier,
- 🧹 Nettoyer et fiabiliser les données (valeurs manquates, aberrantes, ...), 
- 🖼️ Visualiser les KPIs et KPs de façon claire et impactante.

💡 Les fonctionnalités avancées telles que la modélisation IA (SARIMAX, LSTM, ...) ou des outils d'élaboration du budget sont dans l'édition SaaS/Premium **iperform[saas]**.

## ✨ Fonctionnalité de base

`iperform` propose un ensemble complet de fonctions pour extraire les valeurs d'une série temporelle et calculer des indicateurs de performance dynamiques pour toute date de référence donnée - permettant un reporting opérationnel en temps réel et une prise de décision éclairée.

Fonctions clés :

- `mtd()` - Month-To-Date (MTD) : Somme cumulative depuis le premier jour du mois jusqu'à la date de référence.   
- `ytd()` - Year-To-Date : (YTD) : Somme cumulative depuis le 1er janvier jusqu'à date de référence.
- `get_summary_day()` - Retourne 8+ indicateurs dynamiques pour une journée donnée : valeur du Jour-J (J-7, J-1, MTD, ...).
  -> Aussi disponible : `get_summary_month()`, `get_summary_quarter()`... pour des vues mensuelles ou trimestrielles.
- `get_columns_day()` : Génère les noms des colonnes pour un tableau de bord quotidien, basés sur la date de référence.
- `graph_trend_day()` : Crée des visualisations interactives pour explorer les tendances et détecter les anomalies.  
- `forecast_m()` : Estime le total du mois en cours à partir de la performance MTD, via l'extrapolation statistique ou règles métier.

Toutes les fonctions  sont conçues pour une analyse plug-and-play - transformant vos données brutes en insights actionables, en quelques lignes de code.


## 📦 Installation

Installation du package iperform via PyPI :

```bash
pip install iperform
```

## 🧩 Examples

```python

import numpy as np
import pandas as pd
import iperform as ip

# Data
np.random.seed(1234)
date = pd.date_range("2023-01-01", periods=522, freq="D")
revenu = np.random.normal(50, 6.3, 522)
df = pd.DataFrame({"date": date, "revenu": revenu, "zone": "all_zone", "factor": "Orange"})

```

`mtd()` - Month-To-Date

Calcule la somme cumulative depuis le 1er jour du mois en cours jusqu'à la date de référence.

```python

result = ip.mtd(data=df, date="2023-01-15", value="revenu", zone="all_zone", cumul=False, decimal=2)
print(f"Revenu MTD au 15 janvier : {result} USD")
# Exemple de sortie - MTD au 15 Janvier : 745.61 USD

```

`forecast_m()` - Projection mensuelle

Estime le total mensuel à partir de la performance MTD.

```python

projection = ip.forecast_m(data=df, date="2023-01-15", value="revenu", zone="all_zone", decimal=2)
print(f"Projection mensuelle : {projection} USD")
# Exemple de sortie - Projection mensuelle : 1540.93 USD

```

`get_summary_day()` - Résumé journalier (8 indicateurs)

Retourne une liste de 8 indicateurs pour une date donnée : valeur du jour, jour J-1, même jour de la semaine passée (D-7), MTD, variations, etc.

```python

summary = ip.get_summary_day(df=df, date="2023-03-21", zone="all_zone", factor="Orange", value="revenu")
labels = ["D-7", "D-1", "D-Day", "∆ DoD", "∆ DoD-7", "MTD-1", "MTD", "∆ MTD"]
for label, val in zip(labels, summary):
    print(f"{label}: {val}")
# Exemple de sortie  -
# D-7: 54.437
# D-1: 53.981
# D-Day: 50.249
# ∆ DoD: -0.069
# ∆ DoD-7: -0.077
# MTD-1: 1070.639
# MTD: 1067.452
# ∆ MTD: -0.003

```

`get_summary_month()` - Résumé mensuel (8 indicateurs)

Returne une liste de 8 indicateurs pour un mois donné : mois en cours, mois dernier, même mois de l'année passé, YTD, variations (MoM, YoY, etc.).

```python

summary_month = ip.get_summary_month(df=df, date="2024-04-30", factor="Orange",  value="revenu", decimal=2)
labels_month = ["M-12", "M-1", "M", "∆ SPLM", "∆ SPLY", "YTD-1", "YTD", "∆ YTD"]
for label, val in zip(labels_month, summary_month):
    print(f"{label}: {val}")
# Exemple de sortie -
# M-12: 1487.24
# M-1: 1514.23
# M: 1474.21
# ∆ SPLM: 0.01
# ∆ SPLY: -0.01
# YTD-1: 6025.71
# YTD: 5942.99
# ∆ YTD: -0.01

```

`get_columns_day()` - Génération des entêtes du dashbord journalier

Génère les noms des colonnes pour un dashbord journalier, basée sur la date de référence.

```python

# Generate the titles for January 15, 2023
columns = get_column_day(date_ref="2023-01-15")
print("Colonnes du dashbord :")
print(columns)
# Exemple de sortie -
# Colonnes du dashbord :
# ['KPIs', '8-janv.', '14-janv.', '15-janv.', '∆ DoD', '∆ SDLW', 'MTD-1', 'MTD', '∆ MTD']

```

`get_columns_day()` + `get_summay_day()` - Génération d'un dashbord journalier

Crée un dashbord avec les noms de colonnes dynamiques.

```python

date_ref = "2023-03-21"
columns = ip.get_column_day(date_ref)[1:9]
summary_day = ip.get_summary_day(df=df, date=date_ref, zone="all_zone", factor="Orange", value="revenu", decimal=3)
df_summary = pd.DataFrame([summary_day], columns=columns)
print(df_summary)
# Exemple de sortie -
# 14-mars  20-mars  21-mars  ∆ DoD  ∆ SDLW     MTD-1       MTD  ∆ MTD
#  54.437   53.981   50.249 -0.069  -0.077  1070.639  1067.452 -0.003

```

`delta()` - Variation relative

Calcule la variation entre de la valeur x par rapport à y.

```python

# Absolute difference (even if y=0)
print(ip.delta(x=100, y=0, abs=True))
# Example of output - 100.0

# Normalization: compare February (28d) vs January (31d), reduced to 30d
print(ip.delta(x=280, y=310, abs=False, nx=28, ny=31, nn=30))
# Example of output - 0.0

```

## 📄 Documentation

Voir la [documentation]() et [notebooks]()
Signale un bug ou demande une fonctionnalité : [GitHub Issues]() 

## Contribuer 

Toute contribution est la bienvenue !
Que ce soit pour corriger une erreur, ajouter une fonction, ou améliorer la documentation. 

Consulte le fichier [CONTRIBUTING.md]()  pour commencer.

## Contact 

- Github : https://github.com/ipatriqIP/iperform
- Auteur : buabua@internet.ru
- Licence : MIT 