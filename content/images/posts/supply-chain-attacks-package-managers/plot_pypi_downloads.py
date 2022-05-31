import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
from datetime import datetime

from matplotlib.ticker import MultipleLocator, FuncFormatter

plt.xkcd()

df = pd.read_csv("pypi_downloads.csv")
# print(df.head())

ax = sns.lineplot(
    # x=df.project,
    y=df.cumulative_downloads,
    x=df.index,
    data=df,
    # palette="tab10",
    linewidth=2,
    # marker="o",
    color="#2d73b9",
)

ax.set(
    xlabel="Packages",
    ylabel="Percentage of Downloads",
    title="Cumulative Percentage of PyPI Downloads, first 5K Packages",
)
sns.despine()

plt.axvline(x=805, color="lightgray", linestyle="--", label="The 805th package")
plt.axhline(y=80, color="lightgray", linestyle="--", label="80% of downloads")

plt.savefig("plot_pypi_downloads.svg", bbox_inches="tight", transparent=False)
