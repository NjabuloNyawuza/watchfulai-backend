# WatchfulAI — Backend

A community safety early-alert system that ingests reports from WhatsApp and IoT motion sensors, correlates them geographically, and sends automated WhatsApp alerts when a cluster of incidents is detected in the same area.

Built for **Discovery GradHack 2026** (Theme: AI for Safer Communities). Deployed live on Render.

## How it works

1. **Ingestion** — Reports come in two ways:
   - **WhatsApp**, via a Twilio webhook (`/whatsapp/incoming`)
   - **Motion sensors** (e.g. a Raspberry Pi), via a REST endpoint (`/sensor/alert`)
2. **Classification** — Each WhatsApp report is scored as `EMERGENCY`, `SUSPICIOUS`, or `NOISE` using a keyword-matching classifier.
3. **Storage** — All reports are stored in Supabase, with WhatsApp sender numbers hashed (SHA-256) rather than stored in plain text.
4. **Correlation** — A clustering service checks recent `SUSPICIOUS`/`EMERGENCY` reports and groups any that fall within 200m of each other within a 2-hour window, using the Haversine formula for distance.
5. **Alerting** — When a cluster meets the threshold, an automated WhatsApp alert is sent via Twilio, summarising the reports, location, and threat level.

## API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Health check |
| `/whatsapp/incoming` | POST | Twilio webhook for incoming WhatsApp reports |
| `/sensor/alert` | POST | Receives motion alerts from sensors |
| `/reports` | GET | Returns the 200 most recent reports |

## Tech Stack

- **Framework:** FastAPI (Python)
- **Database:** Supabase
- **Messaging:** Twilio (WhatsApp Business API)
- **Deployment:** Render
- **Classification:** Keyword-based rules (see `services/classifier.py`) — a straightforward first pass; a future iteration could swap this for a trained NLP model

## Setup

1. Clone the repo
2. Create a `.env` file (see `.env.example` if present, or the variables below) — `.env` is already gitignored
3. Set the following environment variables:
   ```
   SUPABASE_URL=
   SUPABASE_KEY=
   TWILIO_ACCOUNT_SID=
   TWILIO_AUTH_TOKEN=
   TWILIO_WHATSAPP_FROM=
   ALERT_RECIPIENT=
   RENDER_URL=
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run locally:
   ```bash
   uvicorn main:app --reload
   ```

## Project Structure

```
routes/       — API route handlers (webhook, sensor, reports)
services/     — Classification, correlation, and alerting logic
database.py   — Supabase client setup
config.py     — Environment variable loading
data/         — Sample/seed data for testing
```
