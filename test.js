function sum(a,b,refcall){
    let result = a+b;
    refcall(result);
}
function display(data){
    console.log("Result of the sum is :"+data);
}

function displayresult(data){
    console.log("The of the data value is "+data);
}

const answer = sum(1,4,displayresult) 