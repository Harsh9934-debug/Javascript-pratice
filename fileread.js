const fs = require("fs")

// fs is for the file system and this is used in reading the file 

fs.readFile("a.txt","utf-8",function(err,data){
    console.log(data)
})
   