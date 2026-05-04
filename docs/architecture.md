# Architecture

The system is composed of two main components:

## 1. Gmail Add-on (Frontend Layer)

The Gmail Add-on is implemented using Google Apps Script.

Responsibilities:
- Triggered when an email is opened
- Extracts email data (subject, sender, body)
- Sends the data to the backend API
- Displays the analysis result to the user



## 2. Backend API (FastAPI)

The backend is built with FastAPI and is exposed via ngrok.

Responsibilities:
- Receives email data via HTTP POST request
- Runs a rule-based analysis engine
- Computes a risk score (0–100)
- Returns verdict and explanations



## 3. Scoring Engine

A rule-based system that evaluates:

- Suspicious keywords (e.g. "password", "verify")
- Sender domain anomalies
- Presence of external links
- Suspicious URL patterns

Each rule contributes to a cumulative score.



## 4. Communication Flow

1. User opens an email in Gmail
2. Gmail Add-on is triggered
3. Email data is extracted
4. Request is sent to backend (via ngrok URL)
5. Backend analyzes the email
6. Response is returned to the Add-on
7. Result is displayed to the user



## 5. Design Decisions

- FastAPI: lightweight and fast for prototyping
- Rule-based scoring: simple, explainable, and deterministic
- ngrok: enables local development without deployment
- Gmail Add-on: integrates directly into user workflow



## 6. Limitations

- No machine learning (rule-based only)
- Basic heuristics (not production-grade detection)
- Relies on ngrok (not a deployed service)