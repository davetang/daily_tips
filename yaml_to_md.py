#!/usr/bin/env python3

import yaml
import sys
from pathlib import Path

def load_yaml(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

def to_markdown_table(data):
    # Header
    headers = ["Date", "Tip", "Explanation", "Tags"]
    header_row = f"| {' | '.join(headers)} |"
    separator = f"| {' | '.join(['---'] * len(headers))} |"
    rows = [header_row, separator]

    # Rows
    for entry in data:
        date = entry.get("date", "")
        tip = entry.get("tip", "").replace("\n", " ").strip()
        explanation = entry.get("explanation", "").replace("\n", " ").strip()
        tags = ", ".join(entry.get("tags", []))

        row = f"| {date} | {tip} | {explanation} | {tags} |"
        rows.append(row)

    return "\n".join(rows)

def main(yaml_path, output_path=None):
    data = load_yaml(yaml_path)
    markdown = to_markdown_table(data)

    if output_path:
        with open(output_path, 'w') as out_file:
            out_file.write(markdown)
        print(f"Markdown table written to {output_path}")
    else:
        print(markdown)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python yaml_to_md_table.py <path_to_yaml> [output_md_file]")
    else:
        yaml_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        main(yaml_path, output_path)
