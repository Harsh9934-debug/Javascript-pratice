const express = require('express')
const app = express()

app.get('/',(req,res)=>{
    res.send("Hello world");
})

app.get('/create-todo',(req,res)=>{
    res.send("Create Todo Page");   
})

app.get('/read-todo',(req,res)=>{
    res.send("Create Todo Page");   
})
app.get('/update-todo',(req,res)=>{
    res.send("Create Todo Page");   
})
app.get('/delete-todo',(req,res)=>{
    res.send("Create Todo Page");   
})


app.listen(3000,
    console.log("http://localhost:3000")
)