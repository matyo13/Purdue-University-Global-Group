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
                    console.log("Extracted email data:", emailData);  // Log extracted data

                    // Send email content to the Flask server
                    fetch('http://localhost:5000/predict', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ email_content: emailData.body })
                    })
                    .then(response => {
                        console.log("Received response from server:", response);  // Log server response
                        if (!response.ok) {
                            throw new Error('Network response was not ok');
                        }
                        return response.json();
                    })
                    .then(data => {
                        console.log("Prediction result:", data);  // Log prediction result
                        let prediction = data.prediction === 1 ? 'Phishing' : 'Legitimate';
                        document.getElementById("prediction").innerText = `Prediction: ${prediction}`;
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        document.getElementById("prediction").innerText = `Error: ${error.message}`;
                    });
                } else {
                    console.error("No email data extracted");
                    document.getElementById("prediction").innerText = "Error: No email data extracted";
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