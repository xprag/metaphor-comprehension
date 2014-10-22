#!/bin/bash
# This script create a SQLite database containing the psychopy output results

rm arguments.db
python create_db.py
python set_db.py
python get_db.py
rm *.pyc

