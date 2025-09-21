const express = require('express');
const app = express();
const userRouter = require('./routes/user.routes');
const path = require('path');

// EJS
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

// ✅ Body-parsing middleware MUST come before router
app.use(express.urlencoded({ extended: true })); // for form data
app.use(express.json()); // for JSON payloads

// Router
app.use('/user', userRouter);

// Redirect root
app.get('/', (req, res) => res.redirect('/user'));

app.listen(3000, () => console.log("Server running on port 3000"));
