# Reiskosten Declaratie

Een lokale webapplicatie voor het bijhouden en declareren van woon-werk en zakelijke reiskosten.

## Functies

- Reizen invoeren met datum, traject (van/naar), type en kilometers
- Automatische berekening van vergoedbare kilometers per kalenderdag
- Maandoverzicht met navigatie per maand
- Totaalbedragen per categorie en per maand
- Export naar CSV (apart voor woon-werk en zakelijk)

## Vergoedingsregels

- **Woon-werk**: maximaal 86 km vergoed per kalenderdag (heen en terug samen)
- **Zakelijk**: als het totaal op een kalenderdag 86 km of minder is, telt het als woon-werk; alles boven de 86 km is zakelijk
- Tarieven zijn instelbaar (standaard: €0,23/km woon-werk, €0,28/km zakelijk)

## Installatie

Vereiste: **Python 3** (standaard aanwezig op macOS en de meeste Linux-distributies, op Windows te installeren via [python.org](https://python.org)).

1. Download of clone de repository
2. Maak het startscript uitvoerbaar (macOS/Linux):
   ```bash
   chmod +x start.command   # macOS
   chmod +x start.sh        # Linux
   ```

## Opstarten

| Platform | Actie |
|----------|-------|
| macOS | Dubbelklik op `start.command` |
| Linux | `./start.sh` in terminal |
| Windows | Dubbelklik op `start.bat` |

De browser opent automatisch. De Terminal blijft open zolang de app draait — sluit Terminal om de app te stoppen.

## Gegevensopslag

Alle data wordt opgeslagen in `reiskosten_data.json` in dezelfde map als de applicatie. Dit bestand blijft bewaard ongeacht browsercaches of browsergeschiedenis.

> `reiskosten_data.json` staat in `.gitignore` en wordt niet meegenomen in versiebeheer.

## Bestanden

| Bestand | Omschrijving |
|---------|--------------|
| `reiskosten.html` | De applicatie (frontend) |
| `server.py` | Lokale webserver met lees/schrijf API |
| `start.command` | Startscript voor macOS |
| `start.sh` | Startscript voor Linux |
| `start.bat` | Startscript voor Windows |
| `reiskosten_data.json` | Databestand (automatisch aangemaakt) |
