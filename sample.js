function greet(user) {
    if (user.gender == "male") {
        return "Welcome Mr. " + user.firstname + "and your age is "+user.age;
    } else if (user.gender == "female") {
        return "Welcome Mrs. " + user.firstname + "and your age is "+user.age;
    } else {
        return "Welcome Miss. " + user.firstname + "and your age is "+user.ag;
    }
}

let user = {
    firstname: "harsh",
    age: 19,
    gender: "male"
}

console.log(greet(user));