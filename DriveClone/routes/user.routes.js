const express = require('express');
const router = express.Router();



router.get('/',(req,res) =>{
    res.render('index')
})

router.get('/register',(req,res) =>{
    res.render('register')
})

router.post('/register',async (req,res) =>{
    const {name,email,password} = req.body
    const user = new userModel({name,email,password})
    await user.save()
    res.redirect('/')
})

module.exports = router;