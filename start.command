#!/bin/bash
cd "$(dirname "$0")"

if lsof -Pi :8765 -sTCP:LISTEN -t >/dev/null 2>&1; then
    # Server draait al, open alleen de browser
    open http://localhost:8765/reiskosten.html
else
    # Open browser na korte vertraging, start daarna server op voorgrond
    (sleep 1 && open http://localhost:8765/reiskosten.html) &
    python3 server.py
fi
