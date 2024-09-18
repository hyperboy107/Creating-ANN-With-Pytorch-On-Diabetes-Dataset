const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to handle JSON request bodies
app.use(express.json());

// Serve static files (HTML, CSS, JS)
app.use(express.static(path.join(__dirname, 'public')));

// POST endpoint to handle prediction request
app.post('/predict', (req, res) => {
    const { age, bmi, glucose, bloodPressure, insulin } = req.body;

    // Dummy logic for diabetes prediction (this could be replaced with actual ML logic)
    let prediction = "Low risk of diabetes";

    if (age > 50 && bmi > 30 && glucose > 140 && bloodPressure > 90 && insulin > 150) {
        prediction = "High risk of diabetes";
    } else if (glucose > 180 || insulin > 200) {
        prediction = "Possible diabetes";
    } else if (glucose > 140 || bmi > 25) {
        prediction = "Moderate risk of diabetes";
    }

    res.json({ prediction });
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
