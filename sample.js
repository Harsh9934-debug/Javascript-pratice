function greet(user) {
    if (user.gender == "male") {
        return "Welcome Mr. " + user.firstname;
    } else if (user.gender == "female") {
        return "Welcome Mrs. " + user.firstname;
    } else {
        return "Welcome Miss. " + user.firstname;
    }
}

let user = {
    firstname: "harsh",
    age: 19,
    gender: "male"
}

console.log(greet(user));