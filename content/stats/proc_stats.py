import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

published_count = 0
draft_count = 0
total_count = 0

total_wc = 0
draft_wc = 0
published_wc = 0

total_avg_wc = 0
published_avg_wc = 0
draft_avg_wc = 0

posts_per_year = defaultdict(int)

earliest_dt = datetime.now()
latest_dt = datetime.min

longest = {"wc": 0, "slug": None, "title": None, "url": None, "dt": None}
earliest = {"wc": 0, "slug": None, "title": None, "url": None, "dt": None}
latest = {"wc": 0, "slug": None, "title": None, "url": None, "dt": None}


def mk_link(row, dt):
    return f"blog/{dt.year}/{dt.month:02}/{dt.day:02}/{Path(row['filename']).stem}/"


def mk_title(slug):
    return slug.replace("-", " ").title().strip()


def mk_post(post, row):
    dt = datetime.strptime(row["date"], "%Y-%m-%d")

    post["wc"] = int(row["wc"])
    post["post"] = row["filename"]
    post["slug"] = row["slug"]
    post["title"] = mk_title(row["slug"])
    post["url"] = mk_link(row, dt)
    post["dt"] = dt

    return post


def write_post(f, type, post):
    f.write(f":{type}_dt: {post['dt']:%Y-%m-%d}\n")
    f.write(f":{type}_url: {post['url']}\n")
    f.write(f":{type}_wc: {post['wc']:,}\n")
    f.write(f":{type}_title: {post['title']}\n")
    f.write(f":{type}_post: {post['post']}\n")
    f.write("\n")


with open("stats.csv") as stats:
    rows = csv.DictReader(stats, skipinitialspace=True)
    for row in rows:
        wc = int(row["wc"])
        dt = datetime.strptime(row["date"], "%Y-%m-%d")

        total_wc += wc
        total_count += 1

        if row["status"] == "published":
            posts_per_year[dt.year] += 1
            published_wc += wc
            published_count += 1

            if wc > longest["wc"]:
                longest = mk_post(longest, row)

            if dt < earliest_dt:
                earliest_dt = dt
                earliest = mk_post(earliest, row)
            if dt > latest_dt:
                latest_dt = dt
                latest = mk_post(latest, row)
        else:
            # Drafts, etc...
            draft_count += 1
            draft_wc += wc

total_avg_wc = total_wc // total_count
draft_avg_wc = draft_wc // draft_count
published_avg_wc = published_wc // published_count

print("Writing stats.adoc...")
with open("stats.adoc", "w") as adoc:
    adoc.write(f":published_count: {published_count:,}\n")
    adoc.write(f":draft_count: {draft_count:,}\n")
    adoc.write(f":total_count: {total_count:,}\n")
    adoc.write("\n")

    adoc.write(f":draft_wc: {draft_wc:,}\n")
    adoc.write(f":published_wc: {published_wc:,}\n")
    adoc.write(f":total_wc: {total_wc:,}\n")
    adoc.write("\n")

    adoc.write(f":total_avg_wc: {total_avg_wc:,}\n")
    adoc.write(f":draft_avg_wc: {draft_avg_wc:,}\n")
    adoc.write(f":published_avg_wc: {published_avg_wc:,}\n")
    adoc.write("\n")

    write_post(adoc, "longest", longest)
    write_post(adoc, "earliest", earliest)
    write_post(adoc, "latest", latest)


print("Writing posts_per_year.csv...")
with open("posts_per_year.csv", "w") as csvfile:
    csvfile.write("year,post_count\n")
    for k, v in posts_per_year.items():
        csvfile.write(f"{k},{v}\n")
