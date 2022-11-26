import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
from matplotlib.ticker import MultipleLocator, FuncFormatter


def dateparse(d):
    return datetime.strptime(d.strip('" '), "%Y-%m-%d")


plt.xkcd()

plt.rcParams["font.family"] = "Humor Sans"

df = pd.read_csv("stats.csv", parse_dates=["date"], date_parser=dateparse)
# Split the date out into parts
df["year"] = pd.DatetimeIndex(df["date"]).year
df["month"] = pd.DatetimeIndex(df["date"]).month
df["day"] = pd.DatetimeIndex(df["date"]).day
# print(df.head())

# Get the number of dates / entries in each year
gb = df.groupby("year")["wc"].sum().reset_index(name="word_count")
# Fill in the blanks
gb.loc[len(gb.index)] = [2015, 0]
gb.loc[len(gb.index)] = [2017, 0]
gb.loc[len(gb.index)] = [2018, 0]
gb.sort_values(by="year", ascending=True, inplace=True)

# print(gb)
gb["cumulative_words"] = gb["word_count"].cumsum()
# print(gb)


ax = sns.lineplot(
    x=gb.year,
    y=gb.cumulative_words,
    data=gb,
    # palette="tab10",
    linewidth=2,
    marker="o",
    color="#2d73b9",
)

ax.set(xlabel="Year", ylabel="Word Count", title="Cumulative Words Over Time")
sns.despine()
plt.setp(ax.get_xticklabels(), rotation=45)

ax.xaxis.set_major_locator(MultipleLocator(1))

ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x):,}"))


plt.savefig("plot_cumulative_words.svg", bbox_inches="tight", transparent=False)
