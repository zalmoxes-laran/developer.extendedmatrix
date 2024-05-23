#!/bin/bash

# Naviga nella directory del progetto Pelican
cd C:\Users\Nicola Delbarba\TEST

# Esegui lo script Python per recuperare i dati
python get_github_data.py

# Rigenera il sito Pelican
pelican content -o output -s pelicanconf.py

# (Opzionale) Pubblica il sito
# Esempio: rsync -avz output/ user@server:/percorso/della/cartella/server