#!/usr/bin/env python3

import argparse
import json
import os
import random
import sys
from pathlib import Path

import yaml

DEFAULT_TIPS = Path(__file__).resolve().parent / "tips.yaml"
STATE_FILE = Path(os.environ.get("XDG_STATE_HOME") or Path.home() / ".local" / "state") / "daily_tips" / "quiz.json"
MENU = "[m]ore info, [n]ext tip, [q]uit: "

# Quiz boxes: a known tip moves up one box, a missed tip drops to box 0.
# Each box down doubles the chance of being picked, so a missed tip is
# four times as likely to come up as one you have never been quizzed on.
NEW_BOX = 2
MAX_BOX = 5

def load_tips(filepath):
    with open(filepath, 'r') as file:
        data = yaml.safe_load(file)
    if not isinstance(data, list) or not data:
        raise ValueError("YAML root must be a non-empty list of tip entries.")
    return data

def load_state(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        raise ValueError(f"cannot read quiz progress in {filepath}: {e}")

def save_state(state, filepath):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    tmp = filepath.with_suffix(".tmp")
    with open(tmp, 'w') as file:
        json.dump(state, file, indent=2, sort_keys=True)
    os.replace(tmp, filepath)

def tip_id(entry):
    return str(entry.get("date"))

def shuffled(tips):
    # Cycle through every tip once before any repeats
    while True:
        order = tips[:]
        random.shuffle(order)
        yield from order

def pick_card(tips, state, shown):
    pool = [entry for entry in tips if tip_id(entry) not in shown]
    if not pool:
        return None
    weights = [2 ** (NEW_BOX - state.get(tip_id(entry), {}).get("box", NEW_BOX)) for entry in pool]
    return random.choices(pool, weights)[0]

def ask(prompt):
    try:
        return input(prompt).strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return "q"

def show_tip(entry):
    print(f"\n{entry.get('date', '')}  {entry.get('tip', '')}")

def show_more(entry):
    print(f"\n{entry.get('explanation', 'No explanation.')}")
    tags = entry.get("tags") or []
    if tags:
        print(f"Tags: {', '.join(tags)}")

def browse(tips):
    queue = shuffled(tips)
    entry = next(queue)
    show_tip(entry)

    while True:
        choice = ask(f"\n{MENU}")

        if choice in ("m", "more"):
            show_more(entry)
        elif choice in ("n", "next"):
            entry = next(queue)
            show_tip(entry)
        elif choice in ("q", "quit"):
            break
        else:
            print("Please enter m, n or q.")

def quiz(tips, state, state_path):
    shown = set()
    known = answered = 0

    while True:
        entry = pick_card(tips, state, shown)
        if entry is None:
            print("\nYou have been quizzed on every tip this session.")
            break
        shown.add(tip_id(entry))
        show_tip(entry)

        if ask("\nRecall the explanation, then press Enter to check (q to quit): ") in ("q", "quit"):
            break
        show_more(entry)

        answer = ask("\nDid you know it? [y]es, [n]o, [q]uit: ")
        while answer not in ("y", "yes", "n", "no", "q", "quit"):
            answer = ask("Please enter y, n or q: ")
        if answer in ("q", "quit"):
            break

        card = state.setdefault(tip_id(entry), {"box": NEW_BOX, "right": 0, "wrong": 0})
        if answer in ("y", "yes"):
            card["box"] = min(card["box"] + 1, MAX_BOX)
            card["right"] += 1
            known += 1
        else:
            card["box"] = 0
            card["wrong"] += 1
        answered += 1
        save_state(state, state_path)

    if answered:
        print(f"\nYou knew {known} of {answered}. Progress saved to {state_path}")

def main():
    parser = argparse.ArgumentParser(description="Show random tips from a tips YAML file.")
    parser.add_argument("yaml_path", nargs="?", default=DEFAULT_TIPS, help="tips file (default: tips.yaml next to this script)")
    parser.add_argument("--quiz", action="store_true", help="quiz yourself on the explanations; missed tips come up more often")
    args = parser.parse_args()

    try:
        tips = load_tips(args.yaml_path)
        state = load_state(STATE_FILE) if args.quiz else None
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    if args.quiz:
        quiz(tips, state, STATE_FILE)
    else:
        browse(tips)

if __name__ == "__main__":
    main()
