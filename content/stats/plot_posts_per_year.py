import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
from matplotlib.ticker import MultipleLocator


def dateparse(d):
    return datetime.strptime(d.strip('" '), "%Y-%m-%d")


plt.xkcd()

df = pd.read_csv("stats.csv", parse_dates=["date"], date_parser=dateparse)
# Split the date out into parts
df["year"] = pd.DatetimeIndex(df["date"]).year
df["month"] = pd.DatetimeIndex(df["date"]).month
df["day"] = pd.DatetimeIndex(df["date"]).day
# print(df.head())

# Get the number of dates / entries in each month
gb = df.groupby(by=["year", "status"])["date"].count().reset_index(name="pc")
# print(gb)
# print()

# Fill in the blanks
gb.loc[len(gb.index)] = [2012, "published", 0]
gb.loc[len(gb.index)] = [2015, "published", 0]
gb.loc[len(gb.index)] = [2017, "published", 0]
gb.loc[len(gb.index)] = [2017, "draft", 0]
gb.loc[len(gb.index)] = [2018, "published", 0]
gb.loc[len(gb.index)] = [2018, "draft", 0]
gb.loc[len(gb.index)] = [2019, "draft", 0]
gb.loc[len(gb.index)] = [2020, "draft", 0]
# print(gb)
# print()

#
# Add the yearly total
#

# Make another groupdby, with the yearly totals
gb1 = gb.groupby(by=["year"])["pc"].sum().reset_index(name="total")

# Merge the yearly totals into the original, as a new "total" type row
for index, row in gb1.iterrows():
    gb.loc[len(gb.index)] = [row["year"], "total", row["total"]]

# color palette as dictionary
mypal = {"published": "#2d73b9", "draft": "tab:gray", "total": "lightgray"}

ax = sns.lineplot(
    x=gb.year, y=gb.pc, data=gb, hue="status", palette=mypal, linewidth=2, marker="o"
)

ax.set(xlabel="Year", ylabel="Post Count", title="Posts per Year")
sns.despine()
plt.setp(ax.get_xticklabels(), rotation=45)

# Remove frame from legend
plt.legend(frameon=False)

ax.xaxis.set_major_locator(MultipleLocator(1))

plt.savefig("plot_posts_per_year.svg", bbox_inches="tight", transparent=False)
