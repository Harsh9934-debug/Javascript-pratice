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

const rect1=new rectangle(10,20,'blue');
console.log(rect1.area());
console.log(rect1.colorInfo());