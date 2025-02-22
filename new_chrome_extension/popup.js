document.getElementById("extractBtn").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript(
            {
                target: { tabId: tabs[0].id },
                function: extractEmailContent
            },
            (injectionResults) => {
                if (injectionResults && injectionResults[0] && injectionResults[0].result) {
                    let emailData = injectionResults[0].result;
                    document.getElementById("subject").innerText = emailData.subject;
                    document.getElementById("body").innerText = emailData.body;
                }
            }
        );
    });
});

// Injected function to extract email content
function extractEmailContent() {
    let subject = document.querySelector("h2, .hP")?.innerText || "No Subject Found";
    let bodyElement = document.querySelector(".adn .a3s, .email-body, .ii.gt");
    let body = bodyElement ? bodyElement.innerText : "No Content Found";
    return { subject, body };
}