const express = require ("express")
const { strict } = require("node:assert")
const app = express()
const dbconnection = require('./config/db')
const userModel = require('./models/user')


// this is used in the connection of the index.ejs from the frontend  
app.set("view engine","ejs")

// these are the 2 middlewears that are user when the routes are the post 

app.use(express.json())
app.use(express.urlencoded({extended:true}))


app.use(express.static("public"))  // linking of thhe css file 


app.get('/',(req,res) =>{  // this is used in the rendering of the file from the views folder 
    res.render('index')
})
app.get('/register',(req,res) =>{  // this is used in the rendering of the file from the views folder 
    res.render('register')
})


app.get('/about',(req,res)=>{
    res.send('This is the about page')
})

app.post('/register', async (req, res) => {
    try {
        const { username, email, password } = req.body
        await userModel.create({
            username,
            email,
            password,
        })
        return res.redirect('/register')
    } catch (err) {
        console.error('Error registering user:', err)
        return res.status(500).send('Internal server error')
    }
})

// this is used for getting all the users inside the find we can apply the condition 
// READ method 

app.get('/get-user',(req,res)=>{
    userModel.find({ //inside this we can write the condition
        }).then ((user)=>{
            res.send(user)
        })
})


// this is for the update section
// remember this is the asyncronous function

app.get('/update_user',async (req,res)=>{
    await userModel.findOneAndUpdat({
        username:'a'
    },
    {
        email:"c@c.com"
    })
    res.send("User updated")
})

// this is the section for the  user deletion
// this is also the asyncronous function 

app.get('/delete_user',async (req,res)=>{
    await userModel.findOneAndDelete({
        username:'a'
    })
    res.send("user deleted")
})
 
// this is for the form submittion 
app.post('/form',(req,res) =>{
    console.log(req.body)
    res.send("This is the form fill up section ")
})

app.listen(3000)