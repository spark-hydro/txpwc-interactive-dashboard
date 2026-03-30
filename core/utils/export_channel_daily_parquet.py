from pathlib import Path
from core.io.txpwc_reader import read_channel_sdmorph_day


def main():
    model_dir = Path(r"C:\\Users\\seonggpa\\Documents\\projects\\watersheds\\Pecos\\Analysis\\america-pecos\\Scenarios\\Default\\TxtInOut")
    out_path = Path("resources/txpwc/basins/Pecos/channel_daily.parquet")

    df = read_channel_sdmorph_day(
        model_dir=model_dir,
        variables=["flo_out", "sed_out"],
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out_path, index=False)

    print(f"Saved: {out_path}")
    print(df.head())
    print(df.shape)


if __name__ == "__main__":
    main()