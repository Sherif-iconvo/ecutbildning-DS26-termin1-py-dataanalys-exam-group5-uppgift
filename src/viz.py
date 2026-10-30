def pie_chart_top3(ax, x, y, title, legend_title=None):
    ax.pie(y, autopct="%1.1f%%")
    ax.legend(x, title=legend_title, loc="center left", bbox_to_anchor=(1, 0.5))
    ax.set_title(title)
    return ax