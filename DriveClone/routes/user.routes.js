// routes/user.routes.js

const express = require('express');
const router = express.Router();

// Route to display the main landing page
// URL: http://localhost:3000/user
router.get('/', (req, res) => {
    res.render('index');
});

// Route to display the registration form page
// URL: http://localhost:3000/user/register
router.get('/register', (req, res) => {
    res.render('register');
});

// Route to handle the registration form submission
// Handles the POST request from the form
router.post('/register', (req, res) => {
    // Because of the middleware in app.js, req.body now contains your form data
    const { name, email, password } = req.body;

    // Log the data to the terminal to confirm it's working
    console.log("✅ New user data received:");
    console.log({
        fullName: name,
        emailAddress: email,
        chosenPassword: password, // Note: Never log passwords in a real application!
    });

    // Send a success response back to the user's browser
    res.send(`
        <div style="font-family: sans-serif; text-align: center; padding: 40px;">
            <h1>Registration Successful!</h1>
            <p>Thank you for signing up, <strong>${name}</strong>.</p>
            <p>Your data has been received and logged to the server terminal.</p>
            <a href="/user">Return to Home Page</a>
        </div>
    `);
});

module.exports = router;