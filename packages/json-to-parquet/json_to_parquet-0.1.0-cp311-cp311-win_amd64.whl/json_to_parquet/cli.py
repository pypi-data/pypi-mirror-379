import argparse
import sys

from . import convert_json_to_parquet


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description="Convert JSON/NDJSON to Parquet (streaming, nested).",
    )
    p.add_argument("input_path", help="Path to input JSON/NDJSON file")
    p.add_argument("output_path", help="Path to output Parquet file")

    p.add_argument(
        "--batch-size",
        type=int,
        default=10000,
        help="Arrow RecordBatch size (default: 10000)",
    )
    p.add_argument(
        "--compression",
        choices=["snappy", "gzip", "lz4", "zstd", "none"],
        default="snappy",
        help="Parquet compression (default: snappy)",
    )
    p.add_argument(
        "--json-path",
        default=None,
        help="Optional dot path to nested array/objects, e.g. 'results' or 'response.data.items'",
    )
    p.add_argument(
        "--schema-mode",
        choices=["sample", "full"],
        default="sample",
        help="Schema inference mode: sample (default) or full",
    )
    p.add_argument(
        "--schema-infer-rows",
        type=int,
        default=10000,
        help="Rows to scan when schema-mode=sample (default: 10000)",
    )

    group = p.add_mutually_exclusive_group()
    group.add_argument(
        "--schema-json",
        default=None,
        help="Inline JSON string defining schema (overrides inference)",
    )
    group.add_argument(
        "--schema-json-file",
        default=None,
        help="Path to a JSON file defining schema (overrides inference)",
    )

    return p.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)

    schema_json = args.schema_json
    if args.schema_json_file:
        with open(args.schema_json_file, "r", encoding="utf-8") as f:
            schema_json = f.read()

    try:
        convert_json_to_parquet(
            input_path=args.input_path,
            output_path=args.output_path,
            batch_size=args.batch_size,
            compression=args.compression,
            json_path=args.json_path,
            schema_mode=args.schema_mode,
            schema_infer_rows=args.schema_infer_rows,
            schema_json=schema_json,
        )
    except Exception as e:
        print(f"Conversion failed: {e}", file=sys.stderr)
        return 1
    return 0
