#!/usr/bin/env python3

import random
import sys
from pathlib import Path

import yaml

DEFAULT_TIPS = Path(__file__).resolve().parent / "tips.yaml"
MENU = "[m]ore info, [n]ext tip, [q]uit: "

def load_tips(filepath):
    with open(filepath, 'r') as file:
        data = yaml.safe_load(file)
    if not isinstance(data, list) or not data:
        raise ValueError("YAML root must be a non-empty list of tip entries.")
    return data

def shuffled(tips):
    # Cycle through every tip once before any repeats
    while True:
        order = tips[:]
        random.shuffle(order)
        yield from order

def show_tip(entry):
    print(f"\n{entry.get('date', '')}  {entry.get('tip', '')}")

def show_more(entry):
    print(f"\n{entry.get('explanation', 'No explanation.')}")
    tags = entry.get("tags") or []
    if tags:
        print(f"Tags: {', '.join(tags)}")

def main(yaml_path):
    try:
        tips = load_tips(yaml_path)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    queue = shuffled(tips)
    entry = next(queue)
    show_tip(entry)

    while True:
        try:
            choice = input(f"\n{MENU}").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if choice in ("m", "more"):
            show_more(entry)
        elif choice in ("n", "next"):
            entry = next(queue)
            show_tip(entry)
        elif choice in ("q", "quit"):
            break
        else:
            print("Please enter m, n or q.")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_TIPS)
