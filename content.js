// Constants
const SCAN_INTERVAL = 2000; // Check for new emails every 2 seconds

// Helper function to extract email content
function extractEmailContent(emailElement) {
  const subject = emailElement.querySelector('.subject')?.textContent || '';
  const body = emailElement.querySelector('.email-body')?.textContent || '';
  const sender = emailElement.querySelector('.sender')?.textContent || '';
  
  return {
    subject,
    body,
    sender
  };
}

// Function to add warning banner to suspicious emails
function addWarningBanner(emailElement, analysis) {
  const banner = document.createElement('div');
  banner.className = 'phishshield-warning';
  banner.innerHTML = `
    <strong>⚠️ Potential Phishing Attempt Detected</strong>
    <p>Confidence: ${(analysis.confidence * 100).toFixed(1)}%</p>
    <ul>
      ${analysis.indicators.map(indicator => `<li>${indicator}</li>`).join('')}
    </ul>
  `;
  emailElement.insertBefore(banner, emailElement.firstChild);
}

// Main function to scan emails
async function scanEmails() {
  const emailElements = document.querySelectorAll('.email:not(.phishshield-scanned)');
  
  for (const emailElement of emailElements) {
    const emailContent = extractEmailContent(emailElement);
    
    try {
      const analysis = await chrome.runtime.sendMessage({
        type: 'SCAN_EMAIL',
        emailContent
      });
      
      if (analysis.isPhishing) {
        addWarningBanner(emailElement, analysis);
      }
      
      emailElement.classList.add('phishshield-scanned');
    } catch (error) {
      console.error('Error scanning email:', error);
    }
  }
}

// Start scanning
setInterval(scanEmails, SCAN_INTERVAL);

// Initial scan
scanEmails();