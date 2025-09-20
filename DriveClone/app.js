const express = require('express')
const userRouter  = require('./routes/user.routes')

const app = express()


app.set('view engine','ejs')

app.user('/user',userRouter)

app.listen(3000,() =>{
    console.log("Server is running at the port 3000")
})