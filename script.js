document.getElementById('predictionForm').onsubmit = async function(event) {
    event.preventDefault();
    const features = [
        parseFloat(document.getElementById('feature1').value),
        parseFloat(document.getElementById('feature2').value),
        parseFloat(document.getElementById('feature3').value),
        parseFloat(document.getElementById('feature4').value),
    ];
    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ features })
    });
    const data = await response.json();
    document.getElementById('result').innerText = 'Prediction: ' + data.prediction;
};
