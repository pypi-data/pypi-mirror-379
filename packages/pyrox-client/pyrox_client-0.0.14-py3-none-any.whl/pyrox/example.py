import pyrox.core as core
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def get_entry_from_race(race_df, athlete):
    subset = race_df[race_df["name"].str.contains(athlete, case=False)]
    return subset


client = core.PyroxClient()

rot = client.get_race(season=6, location="rotterdam", use_cache=False)
bcn = client.get_race(season=7, location="barcelona", use_cache=False)
athlete = "matei, vlad"

sns.set_style("whitegrid")
# --- columns (keep your spellings)
run_cols = [f"run{i}_time" for i in range(1, 9)]
station_cols_order = ["SkiErg","Sled Push","Sled Pull","BBJ","Row","Farmers","Lunges","Wall Balls"]
station_colmap = {
    "SkiErg": "skiErg_time",
    "Sled Push": "sledPush_time",
    "Sled Pull": "sledPull_time",
    "BBJ": "burpeeBroadJump_time",
    "Row": "rowErg_time",
    "Farmers": "farmersCarry_time",
    "Lunges": "sandbagLungees_time",  # if you fixed the typo, switch to 'sandbagLunges_time'
    "Wall Balls": "wallBalls_time",
}


def male_open(df: pd.DataFrame) -> pd.DataFrame:
    g = df["gender"].astype(str).str.lower().str.startswith("m")
    d = df["division"].astype(str).str.lower().str.contains("open")
    return df[g & d]

# --- per-race Male Open averages

rot_run_avg = rot[run_cols].mean()
bcn_run_avg  = bcn[run_cols].mean()

rot_sta_avg = pd.Series([rot[station_colmap[s]].mean() for s in station_cols_order], index=station_cols_order)
bcn_sta_avg  = pd.Series([bcn[station_colmap[s]].mean() for s in station_cols_order], index=station_cols_order)

# --- Your comparison frames (using your existing rot / bcn rows)
runs_cmp = pd.DataFrame({
    "segment": range(1, 9),
    "Rotterdam": [rot[c] for c in run_cols],
    "Barcelona": [bcn[c] for c in run_cols],
}).set_index("segment")

stations_cmp = pd.DataFrame({
    "station": station_cols_order,
    "Rotterdam": [rot.get(station_colmap[s], np.nan) for s in station_cols_order],
    "Barcelona": [bcn.get(station_colmap[s], np.nan) for s in station_cols_order],
}).set_index("station")

# --- Plot: runs (add per-race averages)
plt.figure()
plt.plot(runs_cmp.index, runs_cmp["Rotterdam"], marker="o", label="Rotterdam (you)")
plt.plot(runs_cmp.index, runs_cmp["Barcelona"], marker="o", label="Barcelona (you)")
plt.plot(runs_cmp.index, rot_run_avg.values, marker="o", linestyle="--", label="Rotterdam Avg (Male Open)")
plt.plot(runs_cmp.index, bcn_run_avg.values, marker="o", linestyle="--", label="Barcelona Avg (Male Open)")
plt.xticks(runs_cmp.index)
plt.xlabel("Run #")
plt.ylabel("Minutes")
plt.title("Run Splits — You vs Race Averages")
plt.legend()
plt.tight_layout()
plt.show()

# --- Plot: stations (add per-race averages)
plt.figure()
plt.plot(stations_cmp.index, stations_cmp["Rotterdam"], marker="o", label="Rotterdam (you)")
plt.plot(stations_cmp.index, stations_cmp["Barcelona"], marker="o", label="Barcelona (you)")
plt.plot(stations_cmp.index, rot_sta_avg.loc[stations_cmp.index].values, marker="o", linestyle="--", label="Rotterdam Avg (Male Open)")
plt.plot(stations_cmp.index, bcn_sta_avg.loc[stations_cmp.index].values, marker="o", linestyle="--", label="Barcelona Avg (Male Open)")
plt.xticks(stations_cmp.index)
plt.xlabel("Station")
plt.ylabel("Minutes")
plt.title("Station Splits — You vs Race Averages")
plt.legend()
plt.tight_layout()
plt.show()
