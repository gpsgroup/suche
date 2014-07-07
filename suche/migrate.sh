#!/bin/bash
# script for migration of the database
python3 manage.py makemigrations
python3 manage.py migrate
