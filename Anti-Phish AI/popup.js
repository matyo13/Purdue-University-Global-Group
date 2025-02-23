document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("scanBtn").addEventListener("click", () => {
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            chrome.scripting.executeScript(
                {
                    target: { tabId: tabs[0].id },
                    function: extractEmailContent
                },
                (injectionResults) => {
                    if (injectionResults && injectionResults[0] && injectionResults[0].result) {
                        let emailData = injectionResults[0].result;

                        // Send email content to the Flask server
                        fetch('http://localhost:5000/predict', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({ email_content: emailData.body })
                        })
                        .then(response => response.json())
                        .then(data => {
                            let prediction = data.prediction === 1 ? 'a SCAM' : 'Legitimate';
                            document.getElementById("prediction").innerText = `This email is ${prediction}`;
                        })
                        .catch(error => console.error('Error:', error));
                    }
                }
            );
        });
    });
});

// Injected function to extract email content
function extractEmailContent() {
    let subject = document.querySelector("h2, .hP")?.innerText || "No Subject Found";
    let bodyElement = document.querySelector(".adn .a3s, .email-body, .ii.gt");
    let body = bodyElement ? bodyElement.innerText : "No Content Found";
    return { subject, body };
}