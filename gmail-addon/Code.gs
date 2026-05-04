const BACKEND_URL = "https://policy-overpay-depraved.ngrok-free.dev/analyze";

function onGmailMessageOpen(e) {
  return buildInitialCard();
}

function buildInitialCard() {
  return CardService.newCardBuilder()
    .addSection(
      CardService.newCardSection()
        .addWidget(CardService.newTextParagraph().setText("Analyze this email for phishing and malicious indicators."))
        .addWidget(
          CardService.newTextButton()
            .setText("Analyze Email")
            .setOnClickAction(CardService.newAction().setFunctionName("analyzeEmail"))
        )
    )
    .build();
}

function analyzeEmail(e) {
  GmailApp.setCurrentMessageAccessToken(e.gmail.accessToken);

  const messageId = e.gmail.messageId;
  const message = GmailApp.getMessageById(messageId);

  const payload = {
    subject: message.getSubject() || "",
    sender: message.getFrom() || "",
    body: message.getBody() || ""
  };

  const response = UrlFetchApp.fetch(BACKEND_URL, {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  });

  const result = JSON.parse(response.getContentText());

  return buildResultCard(result);
}

function buildResultCard(result) {
  const reasons = result.reasons.length
    ? result.reasons
    : ["No suspicious indicators detected."];

  let severityIcon = "🟢";
  if (result.score >= 60) {
    severityIcon = "🔴";
  } else if (result.score >= 30) {
    severityIcon = "🟡";
  }

  const section = CardService.newCardSection();

  // Title
  section.addWidget(
    CardService.newTextParagraph()
      .setText("<b>Malicious Email Analysis " + severityIcon + "</b>")
  );

  // Big Score
  section.addWidget(
    CardService.newTextParagraph()
      .setText("<b style='font-size:18px;'>Score: " + result.score + "/100</b>")
  );

  // Color logic
  let verdictColor = "green";
  if (result.score >= 60) verdictColor = "red";
  else if (result.score >= 30) verdictColor = "orange";

  // Verdict highlighted
  section.addWidget(
    CardService.newTextParagraph()
      .setText("<b style='color:" + verdictColor + ";'>Verdict: " + severityIcon + " " + result.verdict + "</b>")
  );

  section.addWidget(
    CardService.newTextParagraph()
      .setText("<b>Recommendation</b><br>" + result.recommendation)
  );

  section.addWidget(
    CardService.newTextParagraph()
      .setText("<b>Reasons</b>")
  );

  reasons.forEach(function(reason) {
    section.addWidget(
      CardService.newTextParagraph()
        .setText("• " + reason)
    );
  });

  return CardService.newCardBuilder()
    .addSection(section)
    .build();
}