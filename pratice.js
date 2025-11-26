// write a js program fir the function that takes arrays as an input and returns the users whose are is >18 and are male using loop
function filterAdultMales(users) {
    let adultMales = [];
    for (let i = 0; i < users.length; i++) {
        if (users[i].age > 18 && users[i].gender === "male") {
            adultMales.push(users[i]);
        }
    }
    return adultMales;
}





let users=[
    {
    firstname:"sakshi",
    age:20,
    gender:"female"
    },
    {
    firstname:"honey",
    age:170,
    gender:"female"     
    },

    {
    firstname:"rahul",
    age:22,
    gender:"male"   
    }
]



let adultMales = filterAdultMales(users);
console.log(adultMales);



// also with the filter method
function filterAdultMalesWithFilter(users) {
    return users.filter(user => user.age > 18 && user.gender === "male");
}

let adultMalesWithFilter = filterAdultMalesWithFilter(users);
// console.log(adultMalesWithFilter);  


