const express = require('express');
const app = express();

function oldenoughMiddleware(req, res, next) {
    const age = req.query.age;
    if (age >= 14) {
        next();
    } else {
        res.send("You are not old enough to ride the roller coaster! Must be 14 or older.");
    }
}

app.get('/ride1', oldenoughMiddleware, (req, res) => {
    res.send("Welcome to the roller coaster!");
});




app.listen(3000, () => {
    console.log("Server is running on http://localhost:3000");
});