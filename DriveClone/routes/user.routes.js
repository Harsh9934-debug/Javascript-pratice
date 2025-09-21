const express = require('express');
const app = express();
const userRouter = require('./routes/user.routes');
const path = require('path');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));

// ✅ THIS MUST COME BEFORE THE ROUTER
app.use(express.urlencoded({ extended: true })); // parse form POST
app.use(express.json()); // parse JSON POST

// Mount router
app.use('/user', userRouter);

// Redirect root
app.get('/', (req, res) => res.redirect('/user'));

app.listen(3000, () => console.log("Server running on port 3000"));
