<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Heart Disease Prediction</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f7f7f7; }
        .container { max-width: 400px; margin: 40px auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 0 10px #ccc; }
        h2 { text-align: center; }
        label { display: block; margin: 15px 0 5px; }
        input, select { width: 100%; padding: 8px; }
        button { margin-top: 20px; padding: 10px; width: 100%; background: #007bff; color: white; border: none; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Heart Disease Prediction</h2>
        <form id="predictionForm">
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" required>

            <label for="gender">Gender:</label>
            <select id="gender" name="gender" required>
                <option value="">Select</option>
                <option value="1">Male</option>
                <option value="0">Female</option>
            </select>

            <label for="cholesterol">Cholesterol (mg/dl):</label>
            <input type="number" id="cholesterol" name="cholesterol" required>

            <label for="blood_pressure">Resting Blood Pressure (mm Hg):</label>
            <input type="number" id="blood_pressure" name="blood_pressure" required>

            <label for="diabetes">Diabetes:</label>
            <select id="diabetes" name="diabetes" required>
                <option value="">Select</option>
                <option value="1">Yes</option>
                <option value="0">No</option>
            </select>

            <label for="smoker">Smoker:</label>
            <select id="smoker" name="smoker" required>
                <option value="">Select</option>
                <option value="1">Yes</option>
                <option value="0">No</option>
            </select>

            <button type="submit">Predict</button>
        </form>
        <div id="result" style="margin-top:20px;text-align:center;"></div>
    </div>

    <script>
        document.getElementById('predictionForm').onsubmit = async function(event) {
            event.preventDefault();
            const form = event.target;
            const data = {
                age: form.age.value,
                gender: form.gender.value,
                cholesterol: form.cholesterol.value,
                blood_pressure: form.blood_pressure.value,
                diabetes: form.diabetes.value,
                smoker: form.smoker.value
            };

            // Example: Replace '/predict' with your backend endpoint
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });

            const result = await response.json();
            document.getElementById('result').innerText = 
                result.prediction ? "High risk of Heart Disease" : "Low risk of Heart Disease";
        }
    </script>
</body>
</html>
