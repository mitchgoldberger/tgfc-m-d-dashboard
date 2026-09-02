# TGFC - M&D Dashboard — Standalone Streamlit App

A self-contained dashboard for the TGFC Beef Trim purchase-order log
(M&D International → Northstar Imports). All data is embedded in `app.py`,
so the app runs on its own with no external connections or credentials.

## Features
- Sidebar filters: Item Description, Delivery Location, Order Date
- KPI tiles: load count, total pounds, split by trim type
- Full PO table + Pounds-by-delivery-date chart
- CSV download of the filtered view

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy live (Streamlit Community Cloud)
1. Push `app.py` and `requirements.txt` to a GitHub repo (files at the root).
2. Go to https://share.streamlit.io → **Create app** → **Deploy from GitHub**.
3. Select the repo + branch (`main`), main file `app.py` → **Deploy**.
4. You get a live `…streamlit.app` URL. Pushes to `main` auto-redeploy.

## Updating the data
Edit the `ROWS` list near the top of `app.py` (or replace it with a
`pd.read_csv(...)`), commit, and it redeploys automatically.
