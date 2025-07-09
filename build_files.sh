#!/bin/bash
# build_files.sh

# 1️⃣ Ensure pip is available and up‑to‑date
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip

# 2️⃣ Install project dependencies
pip install -r requirements.txt

# 3️⃣ Run any pending migrations (if using a database)
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

# 4️⃣ Collect static assets into the 'staticfiles' directory
python3 manage.py collectstatic --noinput --clear
