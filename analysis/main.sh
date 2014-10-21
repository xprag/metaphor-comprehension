#!/bin/bash
# This script create a SQLite database containing the psychopy output results

python create_db.py
python set_db.py
python get_db.py
rm *.pyc

