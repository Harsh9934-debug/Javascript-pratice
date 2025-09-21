const express = require('express')
const userRouter  = require('./routes/user.routes')

const app = express()


app.set('view engine','ejs')
app.use(express.static('public'))

app.get('/', (req, res) => {
    res.redirect('/user')
})

app.use('/user',userRouter)

app.listen(3000,() =>{
    console.log("Server is running at the port 3000")
})