
"""
src/viz.py

Visualiseringsmodul för e-commerce.py -> report.ipynb.
Alla funktioner returnerar ett matplotlib.figure.Figure-objekt och stänger
figuren internt (plt.close(fig)) för att förhindra dubbla utskrifter i Jupyter.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Sherif Figuror gällande fråga (3):
# --- 1. Veckodagar (Stapeldiagram Mån->Sön) ---
def plot_weekday_overview(weekday_summary: pd.DataFrame) -> plt.figure:
    """Diagram 1-3: Tre staplade stapeldiagram per veckodag: antal ordrar, total intäkt och AOV.
    Indata: resultatet från weekday_revenue_summary() (kolumner sum, mean, count)."""
    
    fig, axes = plt.subplots(3, 1, figsize=(7, 10))

    axes[0].bar(weekday_summary.index, weekday_summary["count"])
    axes[0].set_title("Totala antalet beställningar per veckodag")
    axes[0].set_xlabel("Veckodag")
    axes[0].set_ylabel("Antal ordrar")
        
    axes[1].bar(weekday_summary.index, weekday_summary["sum"])
    axes[1].set_title("Total intäkt per veckodag")
    axes[1].set_xlabel("Veckodag")
    axes[1].set_ylabel("Total Intäkt (SEK)")
    
    axes[2].bar(weekday_summary.index, weekday_summary["mean"])
    axes[2].set_title("Genomsnittligt ordervärde (AOV) per veckodag")
    axes[2].set_xlabel("Veckodag")
    axes[2].set_ylabel("AOV (SEK)")
    
    for ax in axes:                     # same settings on all three
        ax.grid(True, axis="y")
        ax.set_axisbelow(True)
        ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

    fig.tight_layout()
    plt.close(fig)
    return fig


# --- 2. Veckotrend (Linjediagram) ---
def plot_weekly_rev(weekly_rev_summ: pd.DataFrame) -> plt.figure:
    """Diagram 4: Veckovis omsättning."""
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(weekly_rev_summ.index.astype(str), weekly_rev_summ.values, marker="s", linewidth=2)
    ax.set_title("Veckoomsättning")
    ax.set_xlabel("Vecka")
    ax.set_ylabel("Intäkt (SEK)")
    ax.grid(True)
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))
    ax.tick_params(axis="x", rotation=45)
    plt.tight_layout()

    plt.close(fig)
    return fig


# --- 3. Månadssammanfattning (3 subplots med delad x-axel) ---
def plot_monthly_overview(monthly_change: pd.DataFrame) -> plt.figure:
    """Diagram 5-7: Tre sammankopplade grafer (Antal order, Intäkt med MoM-förändring, AOV)."""
    
    fig, axes = plt.subplots(3, 1, figsize=(7, 10))

    # 1. Antal Order
    axes[0].plot(monthly_change.index.astype(str), monthly_change["count"])
    axes[0].set_title("Antal order per månad")
    axes[0].set_xlabel("Månad")
    axes[0].set_ylabel("Antal ordrar")

    # 2. Omsättning per månad med % förändring ovanför staplarna.   
    bars = axes[1].bar(monthly_change.index.astype(str), monthly_change["sum"])
    labels = ["" if pd.isna(p) else f"{p:.1f} %" for p in monthly_change["pct_change"]]
    axes[1].bar_label(bars, labels=labels, padding=3)
    axes[1].set_title("Omsättning per månad med MOM % förändring")
    axes[1].set_xlabel("Månad")
    axes[1].set_ylabel("Total Intäkt (SEK)")

    # 3. AOV
    axes[2].plot(monthly_change.index.astype(str), monthly_change["mean"])
    axes[2].set_title("Genomsnittligt ordervärde (AOV) per månad")
    axes[2].set_xlabel("Månad")
    axes[2].set_ylabel("AOV (SEK)")
    
    for ax in axes:                     # same settings on all four
        ax.grid(True, axis="y")
        ax.set_axisbelow(True)
        ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

    fig.tight_layout()
    plt.close(fig)
    return fig


# --- 4. Kategoriprestanda över tid (Unstack line chart) ---
def plot_category_trends(category_perf_summ: pd.DataFrame, figsize: tuple[int, int] = (9, 5)) -> plt.figure:
    """Diagram 8: Utveckling per kategori över tid."""
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.set_title("Intäktsutveckling per kategori per månad")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Intäkt (SEK)")

    # Unstack för att få månader som rader och kategorier som kolumner
    unstacked = category_perf_summ["total_revenue"].unstack(level=-1)

    # Rita linjer med automatisk färgkodning per kategori
    unstacked.plot(ax=ax, marker="o", linewidth=2)

    # Formaterar Y-axeln med kommatecken som tusentalsavgränsare (t.ex. 300,000)
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

    fig.tight_layout()
    plt.close(fig)
    return fig


# --- 5. Stadprestanda över tid (Unstack line chart) ---
def plot_city_trends(city_performance: pd.DataFrame, figsize: tuple[int, int] = (9, 5)) -> plt.figure:
    """Diagram 9: Utveckling per Stad över tid."""
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.set_title("Intäktsutveckling per stad per månad")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Intäkt (SEK)")

    # Unstack för att få månader som rader och Stad som kolumner
    unstacked = city_performance["total_revenue"].unstack(level=-1)

    # Rita linjer med automatisk färgkodning per stad
    unstacked.plot(ax=ax, marker="o", linewidth=2)

    # Formaterar Y-axeln med kommatecken som tusentalsavgränsare (t.ex. 300,000)
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

    fig.tight_layout()
    plt.close(fig)
    return fig

## slutet på Sherifs figurer för fråga (3).

# Edvins Figuror:
def bar(ax, x, y, title, xlabel, ylabel, grid: bool = True):
    x = x
    y = y
    ax.bar(x,y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y")
    return ax

## slutet på Edvins figurer

# Henrik Figuror:
def pie_chart_top3(top3: pd.DataFrame) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.pie(
        top3["revenue"],
        labels=top3["category"],
        autopct="%1.1f%%"
    )

    ax.set_title("Top 3 Categories by Revenue")
    plt.close(fig)
    return fig
## slutet på Henrik figurer
