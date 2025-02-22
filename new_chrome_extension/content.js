function extractEmailContent() {
    let subject = document.querySelector("h2, .hP")?.innerText || "No Subject Found";
    
    // Try multiple selectors for Gmail email body
    let bodyElement = document.querySelector(".adn .a3s, .email-body, .ii.gt");
    let body = bodyElement ? bodyElement.innerText : "No Content Found";

    return { subject, body };
}

// Listen for messages from popup.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "extract_email") {
        let emailData = extractEmailContent();
        sendResponse(emailData);
    }
});


// Listen for messages from popup.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "extract_email") {
        let emailData = extractEmailContent();
        sendResponse(emailData);
    }
});
