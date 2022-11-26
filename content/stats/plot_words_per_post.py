import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from datetime import datetime

from matplotlib.ticker import MultipleLocator, FuncFormatter


def dateparse(d):
    return datetime.strptime(d.strip('" '), "%Y-%m-%d")


plt.xkcd()

plt.rcParams["font.family"] = "Humor Sans"

df = pd.read_csv("stats.csv", parse_dates=["date"], date_parser=dateparse)
# print(df.head())
ax = sns.lineplot(
    x=df.date,
    y=df.wc,
    data=df,
    # palette="tab10",
    linewidth=2,
    marker="o",
    color="#2d73b9",
)

# # Set general font size
# plt.rcParams["font.size"] = "10"

# # Set tick font size
# for label in ax.get_xticklabels() + ax.get_yticklabels():
#     label.set_fontsize(10)

ax.set(xlabel="Date", ylabel="Word Count", title="Words per Post")
sns.despine()
plt.setp(ax.get_xticklabels(), rotation=45)

# Define the date format
date_fmt = DateFormatter("%Y")
ax.xaxis.set_major_formatter(date_fmt)
# Ensure a major tick for each week using (interval=1)
# ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
# ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=1))

ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{int(x):,}"))

# add text annotation
# plt.text(
#     17000,
#     1300,
#     "Can you guess \nwhen we had kids?",
#     horizontalalignment="center",
#     size="medium",
#     color="black",
#     # weight="semibold",
# )

plt.savefig("plot_words_per_post.svg", bbox_inches="tight", transparent=False)
