
const express = require('express');
const app = express();
const userRouter = require('./routes/user.routes');
const path = require('path');

app.set('view engine', 'ejs');

app.use(express.urlencoded({ extended: true }));
app.use(express.json());


app.use('/user', userRouter);
app.get('/', (req, res) => res.redirect('/user'));

app.listen(3000, () => {
    console.log("✅ Server is running correctly on http://localhost:3000");
});