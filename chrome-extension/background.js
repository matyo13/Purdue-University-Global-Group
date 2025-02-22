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
chrome.runtime.onMessage.addListener(async (request, sender, sendResponse) => {
  if (request.type === 'SCAN_EMAIL') {
    const emailContent = request.emailContent;
    
    // Example: Send email content to a server for model inference
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(emailContent)
      });
      const analysis = await response.json();
      sendResponse(analysis);
    } catch (error) {
      console.error('Error fetching model prediction:', error);
      sendResponse({ error: 'Error fetching model prediction' });
    }
    
    return true; // Indicates that the response will be sent asynchronously
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