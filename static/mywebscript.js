function RunSentimentAnalysis() {
    let textToAnalyze = document.getElementById("textToAnalyze").value.trim();
    let resultDiv = document.getElementById("system_response");

    if (!textToAnalyze) {
        resultDiv.innerHTML = "Invalid text! Please try again!";
        return;
    }

    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            resultDiv.innerHTML = this.responseText;
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze),
        true
    );

    xhttp.send();
}
