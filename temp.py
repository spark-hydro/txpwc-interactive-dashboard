from pathlib import Path
from core.io.txpwc_reader import read_channel_sdmorph_day

model_dir = Path(r"C:\\Users\\seonggpa\\Documents\\projects\\watersheds\\Pecos\\Analysis\\america-pecos\\Scenarios\\Default\\TxtInOut")
df = read_channel_sdmorph_day(model_dir)

print(df.head())
print(df.tail())
print(df.columns.tolist())
print("Rows:", len(df))
print("Unique gis_id:", df["gis_id"].nunique())
print("Date range:", df["date"].min(), "to", df["date"].max())
print(df.groupby("gis_id").size().head())