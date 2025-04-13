#!/usr/bin/env bash

TODAY=$(date +%Y-%m-%d)

./yaml_to_md.py tips.yaml | grep ${TODAY} >> README.md
