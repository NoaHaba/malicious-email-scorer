from app.scorer import analyze
from app.models import EmailRequest


def test_safe_email():
    email = EmailRequest(
        subject="Meeting tomorrow",
        sender="manager@company.com",
        body="Let's meet at 10"
    )
    result = analyze(email)
    assert result.score < 30
    assert result.verdict == "Safe"


def test_malicious_email():
    email = EmailRequest(
        subject="Urgent security alert",
        sender="support@secure-login.com",
        body="Click here to verify your password"
    )
    result = analyze(email)
    assert result.score >= 60
    assert result.verdict == "Likely malicious"