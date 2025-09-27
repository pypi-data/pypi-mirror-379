"""
iperform - Tableau de bord analytique dynamique pour telecom & banque

Conçu pour être simple, complet et communautaire.
Toutes les fonctions principales sont accessibles via `ip.fonction()`.

Pour les fonctionnalités avancées (prévision SARIMAX, narration, alertes, élaboration budget),
voir `iperform_cloud` : https://www.ipgeodata.com
"""

import os

# --- Version du package ---
__version__ = "0.2.0"

# --- Fonctions principales (exposées au niveau racine) ---
from .core import (
    get_summary_day,
    get_summary_month,
    get_summary_quarter,
    get_column_day,
    get_column_month,
    get_column_quarter,
    dday,
    mtd, qtd, ytd, htd, wtd,
    full_w, full_m, full_q, full_h, full_y,
    forecast_m,
    delta
    )

# --- Plotting des KPIs ---
from .plotting import (
    graph_trend_day,
    plot_kpi,
    graph_season
    )

# --- Formatage des KPIs ---
from .formatting import format_kpi

# --- Utilitaires ---
from .utils import load_sample_data


# --- Premium module ---

_premium_modules = [
    'modeling',
    'preprocessing',
    'budgeting',
    'deployment'
    ]

# Dictionnary function
_premium_imports = {
    'modeling': ['forecast_m_advanced', 'cluster_customers', 'detect_anomalies'],
    'preprocessing': ['clean_telecom_data', 'impute_missing_values'],
    'budgeting': ['calculate_budget_variance', 'forecast_budget'],
    'deployment': ['send_email_report', 'export_to_excel']
    }

# Import modul
for module_name in _premium_modules:
    module_path = os.path.join(os.path.dirname(__file__), f'{module_name}.py')
    if os.path.exists(module_path):
        try:
            # Import dynamique
            module = __import__(f'.{module_name}', fromlist=_premium_imports[module_name], globals=globals(), locals=locals(), level=1)
            # Importer chaque fonction dans l'espace global
            for func_name in _premium_imports[module_name]:
                if hasattr(module, func_name):
                    globals()[func_name] = getattr(module, func_name)
        except Exception as e:
            print(f"⚠️ Erreur lors de l'import de {module_name}: {e}")
            continue


# --- Contrôle de `from iperform import *` ---
__all__ = ["get_summary_day", "get_summary_month", "get_summary_quarter",
           "get_column_day", "get_column_month", "get_column_quarter",
           "graph_trend_day", "plot_kpi", "graph_season",
           "dday",
           "mtd", "qtd", "ytd", "htd", "wtd",
           "full_w", "full_m", "full_q", "full_h", "full_y",
           "forecast_m",
           "delta",
           "format_kpi",
           "load_sample_data",
           "__version__"
           ]