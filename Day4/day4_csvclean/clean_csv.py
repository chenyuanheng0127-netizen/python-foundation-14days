#!/usr/bin/env python3
import argparse, json, logging
from pathlib import Path
import pandas as pd


def clean_dataframe(df, columns=None, dropna=False, dropna_cols=None,
                    dedup=False, dedup_cols=None):
    summary = {"rows_before": int(df.shape[0]),
               "cols_before": list(df.columns.astype(str)),
               "columns_kept": None,
               "dropna_applied": bool(dropna),
               "dropna_cols": dropna_cols if dropna_cols else None,
               "dedup_applied": bool(dedup),
               "dedup_cols": dedup_cols if dedup_cols else None,
               "rows_after_dropna": None,
               "rows_after_dedup": None,
               "rows_after": None,
               "rows_removed_na": 0,
               "rows_removed_dups": 0}
    if columns:
        missing = [c for c in columns if c not in df.columns]
        if missing: raise ValueError(f"Columns not found: {missing}")
        df = df[list(columns)].copy()
        summary["columns_kept"] = list(columns)
    else:
        summary["columns_kept"] = list(df.columns.astype(str))
    if dropna:
        before = len(df)
        if dropna_cols:
            bad = [c for c in dropna_cols if c not in df.columns]
            if bad: raise ValueError(f"--dropna-cols not found: {bad}")
            df = df.dropna(subset=list(dropna_cols))
        else:
            df = df.dropna(how="any")
        after = len(df)
        summary["rows_after_dropna"] = int(after)
        summary["rows_removed_na"] = int(before - after)
    if dedup:
        before = len(df)
        if dedup_cols:
            bad = [c for c in dedup_cols if c not in df.columns]
            if bad: raise ValueError(f"--dedup-cols not found: {bad}")
            df = df.drop_duplicates(subset=list(dedup_cols), keep="first")
        else:
            df = df.drop_duplicates(keep="first")
        after = len(df)
        summary["rows_after_dedup"] = int(after)
        summary["rows_removed_dups"] = int(before - after)
    summary["rows_after"] = int(len(df))
    return df, summary

def parse_args():
    p = argparse.ArgumentParser(description="CSV cleaner")
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--columns", nargs="+")
    p.add_argument("--dropna", action="store_true")
    p.add_argument("--dropna-cols", nargs="+")
    p.add_argument("--dedup", action="store_true")
    p.add_argument("--dedup-cols", nargs="+")
    p.add_argument("--to-json")
    p.add_argument("--sep", default=",")
    p.add_argument("--encoding", default="utf-8")
    p.add_argument("--verbose", action="store_true")
    return p.parse_args()

def main():
    args = parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(levelname)s | %(message)s")
    inp, outp = Path(args.input), Path(args.output)
    if not inp.exists():
        logging.error(f"Input not found: {inp}"); return 2
    df = pd.read_csv(inp, sep=args.sep, encoding=args.encoding)
    try:
        df_out, summary = clean_dataframe(
            df, columns=args.columns, dropna=args.dropna, dropna_cols=args.dropna_cols,
            dedup=args.dedup, dedup_cols=args.dedup_cols)
    except ValueError as e:
        logging.error(str(e)); return 3
    outp.parent.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(outp, index=False, sep=args.sep, encoding=args.encoding)
    if args.to_json:
        Path(args.to_json).parent.mkdir(parents=True, exist_ok=True)
        with open(args.to_json, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
    logging.info(f"Done. rows: {len(df_out)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
