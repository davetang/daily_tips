#!/usr/bin/env python3

import yaml
import sys
from pathlib import Path

def load_yaml(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

def escape_pipes(text):
    return text.replace("|", r"\|")

def to_markdown_table(data):
    # Validate input
    if not isinstance(data, list):
        raise ValueError("YAML root must be a list of entries.")

    # Header
    headers = ["Date", "Tip", "Explanation", "Tags"]
    header_row = f"| {' | '.join(headers)} |"
    separator = f"| {' | '.join(['---'] * len(headers))} |"
    rows = [header_row, separator]

    # Rows
    for entry in data:
        date = escape_pipes(str(entry.get("date", "")))
        tip = escape_pipes(str(entry.get("tip", "")).replace("\n", " ").strip())
        explanation = escape_pipes(str(entry.get("explanation", "")).replace("\n", " ").strip())
        tags = escape_pipes(", ".join(entry.get("tags", [])))

        row = f"| {date} | {tip} | {explanation} | {tags} |"
        rows.append(row)

    return "\n".join(rows)

def main(yaml_path, output_path=None):
    try:
        data = load_yaml(yaml_path)

        if not isinstance(data, list):
            print("Error: YAML file should contain a list of tip entries.")
            sys.exit(1)

        markdown = to_markdown_table(data)

        if output_path:
            with open(output_path, 'w') as out_file:
                out_file.write(markdown)
            print(f"Markdown table written to {output_path}")
        else:
            print(markdown)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python yaml_to_md_table.py <path_to_yaml> [output_md_file]")
    else:
        yaml_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        main(yaml_path, output_path)
