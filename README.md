# Malicious Email Scorer

A Gmail Add-on that analyzes emails for phishing and malicious indicators using a rule-based backend.

---

## Overview

This project integrates directly into Gmail and allows users to analyze any opened email with a single click.

The system evaluates the email and returns:

* A risk score (0–100)
* A verdict (Safe / Suspicious / Likely malicious)
* Reasons explaining the classification
* A recommended action for the user

---

## Demo

1. Open any email in Gmail
2. Click **"Analyze Email"** in the add-on panel
3. View the analysis result directly inside Gmail

---

## Architecture

The system consists of two main components:

### Gmail Add-on (Google Apps Script)

* Extracts email data (subject, sender, body)
* Sends the data to the backend API
* Displays the analysis result inside Gmail

### Backend API (FastAPI)

* Receives email data via HTTP request
* Runs a rule-based scoring engine
* Returns score, verdict, and explanations

Communication between the add-on and the backend is done via HTTP using ngrok.

---

## Scoring Logic

The system assigns a score based on several heuristics:

* Suspicious keywords (e.g. "password", "verify", "urgent")
* Suspicious sender domains
* Presence of external links
* Suspicious URL patterns

### Verdict thresholds

* 0–29 → Safe
* 30–59 → Suspicious
* 60–100 → Likely malicious

---

## Example Output

Score: 75  
Verdict: Likely malicious  

Recommendation:  
Do not click links, download attachments, or provide credentials.

Reasons:
- Contains suspicious word: 'password'  
- Contains suspicious word: 'verify'  
- Contains external links  

---

## Tech Stack

* Python (FastAPI)
* Google Apps Script (Gmail Add-on)
* ngrok (local tunneling)
* Pydantic

---

## Project Structure

backend/
  app/
    main.py          # FastAPI entry point
    models.py        # Request/response schemas
    scorer.py        # Core scoring logic
  tests/
    test_scorer.py   # Unit tests for scoring engine
  requirements.txt   # Python dependencies

gmail-addon/
  Code.gs            # Gmail Add-on logic
  appsscript.json    # Add-on configuration

docs/
  architecture.md    # System design explanation
  demo.md            # Demo instructions

README.md            # Project overview and setup
.gitignore           # Files excluded from Git

---

## How to Run

### Backend

```
cd backend
python -m venv venv # Create virtual environment if not already created
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

### Expose API (ngrok)

```
ngrok http 8000
```

Copy the generated URL and update it in `Code.gs`:

```
const BACKEND_URL = "https://<your-ngrok-url>/analyze";
```

---

### Gmail Add-on

1. Open Google Apps Script
2. Paste the code from `gmail-addon/Code.gs`
3. Configure `appsscript.json`
4. Deploy → Test deployment
5. Open Gmail and test

---

## Design Decisions

* Rule-based scoring for simplicity and explainability
* FastAPI for rapid backend development
* Gmail Add-on for direct integration into the user workflow
* ngrok for local development without deployment

---

## Security Considerations

The system treats all email content as untrusted input and does not persist any user data.
All external requests are performed over HTTPS.

---

## Tests

Basic unit tests are included for the scoring engine.

To run the tests:

cd backend
venv\Scripts\activate
pip install -r requirements.txt
python -m pytest

The tests cover both safe and malicious email scenarios to validate the scoring logic.

---

## Limitations

* No machine learning model
* Basic heuristics only
* Not production-ready
* Requires ngrok for local execution

---

## Future Improvements

* Replace rule-based scoring with a machine learning model trained on labeled phishing and legitimate emails
* Integration with URL reputation APIs
* Sender reputation analysis
* Deployment to a cloud environment
* UI and UX improvements

---

## Author

Noa Haba
