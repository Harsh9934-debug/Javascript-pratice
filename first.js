const allUsers =[{
    firstname : "harsh",
    gender:"male"
},{
    firstname:"sakshi", 
    gender:"female"
},{
    firstname:"honey",
    gender:"female"
}]
let n = allUsers.length
for(let i=0;i<n;i++){
    if(allUsers[i]["gender"]=="male"){
        console.log(allUsers[i]["firstname"])
    }
}