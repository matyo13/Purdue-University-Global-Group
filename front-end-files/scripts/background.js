// Constants
const API_ENDPOINT = 'YOUR_AI_API_ENDPOINT';

// Handle installation
chrome.runtime.onInstalled.addListener(() => {
  // Initialize extension settings
  chrome.storage.local.set({
    isEnabled: true,
    scanningThreshold: 0.8,
    lastScanTime: null
  });
});

// Listen for messages from content script
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === 'SCAN_EMAIL') {
    analyzeEmail(request.emailContent)
      .then(result => sendResponse(result))
      .catch(error => sendResponse({ error: error.message }));
    return true; // Required for async response
  }
});

// Function to analyze email content
async function analyzeEmail(emailContent) {
  try {
    const response = await fetch(API_ENDPOINT, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_API_KEY'
      },
      body: JSON.stringify({
        content: emailContent,
        type: 'phishing_detection'
      })
    });

    const data = await response.json();
    return {
      isPhishing: data.phishingProbability > 0.8,
      confidence: data.phishingProbability,
      indicators: data.phishingIndicators
    };
  } catch (error) {
    console.error('Error analyzing email:', error);
    throw error;
  }
}