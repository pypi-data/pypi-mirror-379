""" functions for processing cls.log files """
import json
import re
import sys
from typing import List, Dict
import pandas as pd
import zipfile
from tempfile import TemporaryDirectory
from pathlib import Path

from .utils import (
    CLS_COLUMNS, CLS_ERROR_BLOCK_PATTERN, CLS_ERROR_TYPE_PATTERN, CLS_OUTPUT_REPORT, 
    norm_path, safe_extract, generate_report_filename
)

def process_cls_file(cls_file: Path) -> List[Dict[str, str]]:
    """process cls.log file, extract error messages and types"""
    errors = []
    text = cls_file.read_text(encoding="utf-8", errors="ignore")
    for blk in CLS_ERROR_BLOCK_PATTERN.findall(text):
        msg_lines, etype = [], "UNKNOWN"
        for line in map(str.strip, blk.splitlines()):
            if line.startswith(("╭", "╰")) or ("Error on Agent" in line):
                continue
            if line.startswith("│"):
                body = line.lstrip("│").rstrip("│").strip()
                if body:
                    msg_lines.append(body)
                    if etype == "UNKNOWN":
                        m = CLS_ERROR_TYPE_PATTERN.search(body)
                        if m:
                            etype = m.group(1)
        if msg_lines:
            errors.append({"type": etype, "msg": "\n".join(msg_lines)})
    return errors


def write_cls_error_report(errors: list, type_counter: dict, out_xlsx: Path) -> None:
    """Write cls.log errors to an excel file."""
    df_detail = pd.DataFrame(errors, columns=CLS_COLUMNS)
    df_type = pd.DataFrame(list(type_counter.items()), columns=["Error Type", "Count"])
    # add a row for all error types count
    all_count = df_type['Count'].sum()
    df_type = pd.concat([df_type, pd.DataFrame([["ALL", all_count]], columns=["Error Type", "Count"])], ignore_index=True)
    with pd.ExcelWriter(out_xlsx, engine='openpyxl') as writer:
        df_detail.to_excel(writer, sheet_name='Detail', index=False)
        df_type.to_excel(writer, sheet_name='TypeCount', index=False)


def generate_cls_error_report(zip_path: Path, need_write: bool = False) -> dict:
    """unzip outer zip, recursively process all inner zips, output cls.log error result"""
    zip_path = norm_path(zip_path)
    if not zip_path.exists():
        raise ZipNotFoundError(f"Zip file not found: {zip_path}")
    rows, counter = [], {}
    skipped_inner_zip = 0
    skipped_cls_log = 0
    with TemporaryDirectory(prefix="msbench_") as tmp:
        tmp_dir = Path(tmp)
        with zipfile.ZipFile(zip_path) as z:
            safe_extract(z, tmp_dir)

        for inner in tmp_dir.rglob("*.zip"):
            try:
                with zipfile.ZipFile(inner) as z:
                    safe_extract(z, tmp_dir/inner.stem, ignore_error=False)
            except Exception as e:
                skipped_inner_zip += 1
                continue

            # only process cls.log files in the output directory
            output_dir = tmp_dir/inner.stem/"output"
            if output_dir.exists() and output_dir.is_dir():
                for cls in output_dir.rglob("cls.log"):
                    try:
                        for item in process_cls_file(cls):
                            rows.append([inner.name, item["msg"], item["type"]])
                            counter[item["type"]] = counter.get(item["type"], 0) + 1
                    except Exception as e:
                        skipped_cls_log += 1
                        continue

    # Generate unique output filename based on zip file name
    if need_write:
        report_filename = generate_report_filename(zip_path, "cls")
        out_xlsx = zip_path.parent / report_filename
        write_cls_error_report(rows, counter, out_xlsx)
    else:
        out_xlsx = None

    return {
        "report_path": str(out_xlsx) if need_write else "",
        "total_errors": sum(counter.values()),
        "by_type": counter,
        "skipped_inner_zip": skipped_inner_zip,
        "skipped_cls_log": skipped_cls_log,
        "errors": rows
    }