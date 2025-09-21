const express = require('express');
const router = express.Router();



router.get('/',(req,res) =>{
    res.render('index')
})

router.get('/register',(req,res) =>{
    res.render('register')
})

router.post('/register',async(req,res) =>{

    console.log(req.body)
    const {name,email,password} = req.body
    res.send('user registered successfully')
})

module.exports = router;