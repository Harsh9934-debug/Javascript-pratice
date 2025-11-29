class rectangle{
    constructor(height,width,color){
        this.height=height;
        this.width=width;
        this.color=color;
    }
    area(){
        return this.height*this.width;
    }   
    colorInfo(){
        return `The color of the rectangle is ${this.color}`;
    }
}





const rect1=new rectangle(10,5,'blue');  // this is how we create an object in the rectangle class 
// rect1.height=10;
// rect1.width=5;
// rect1.color='blue';

// this is how we access the methods of the class in the object also we can pass the parameters in the constructor

console.log(rect1.area());
console.log(rect1.colorInfo());