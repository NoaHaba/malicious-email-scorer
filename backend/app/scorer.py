import re

from app.models import EmailRequest, AnalysisResponse


SUSPICIOUS_WORDS = ["urgent", "password", "verify", "click", "account", "bank"]


def extract_links(text: str) -> list[str]:
    links = re.findall(r"https?://[^\s\"'<>]+", text)
    return list(dict.fromkeys(links))


def analyze(email: EmailRequest) -> AnalysisResponse:
    score = 0
    reasons = []

    body_lower = email.body.lower()
    subject_lower = email.subject.lower()
    sender_lower = email.sender.lower()

    for word in SUSPICIOUS_WORDS:
        if word in body_lower or word in subject_lower:
            score += 15
            reasons.append(f"Contains suspicious word: '{word}'")

    if "@" not in email.sender:
        score += 30
        reasons.append("Invalid sender format")

    if "@" in email.sender:
        domain = sender_lower.split("@")[-1].replace(">", "").strip()
        if any(x in domain for x in ["secure", "verify", "login"]):
            score += 20
            reasons.append(f"Suspicious sender domain: {domain}")

    links = extract_links(email.body)

    if links:
        score += 15
        reasons.append("Contains external links")

        for link in links:
            link_lower = link.lower()
            if any(x in link_lower for x in ["secure", "verify", "login"]):
                score += 10
                reasons.append(f"Suspicious link: {link}")

    score = min(score, 100)

    if score < 30:
        verdict = "Safe"
        recommendation = "No immediate risk detected. User may proceed normally."
    elif score < 60:
        verdict = "Suspicious"
        recommendation = "Review carefully before clicking links or replying."
    else:
        verdict = "Likely malicious"
        recommendation = "Do not click links, download attachments, or provide credentials."

    return AnalysisResponse(
        score=score,
        verdict=verdict,
        recommendation=recommendation,
        reasons=reasons,
    )