# Demo Guide

## Goal

Demonstrate how the system detects malicious emails directly inside Gmail.



## Step 1 – Safe Email

Open a normal email, for example:

Subject: Meeting tomorrow  
Body: "Hi, let's meet tomorrow at 10"

Click **Analyze Email**

Expected result:
- Score: 0–20
- Verdict: Safe



## Step 2 – Suspicious Email

Use an email containing phishing patterns:

Subject: Urgent Security Alert  
Body:
"Your account is compromised. Click here to verify your password immediately."

Click **Analyze Email**

Expected result:
- Score: 70–100
- Verdict: Likely malicious
- Reasons include suspicious words and links



## Step 3 – Explain the Output

Highlight:
- Score represents risk level
- Verdict is based on thresholds
- Reasons explain WHY the email is flagged
- Recommendation tells the user what to do



## Step 4 – Explain Architecture (briefly)

- Gmail Add-on extracts email
- Sends to FastAPI backend
- Backend analyzes using rules
- Result returned and displayed



## Step 5 – Talk About Improvements

Possible future improvements:
- Machine learning model
- URL reputation APIs
- Sender reputation scoring
- Deployment to cloud instead of ngrok