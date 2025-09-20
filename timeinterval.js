let count = 0;
let id = setInterval(() => {
  console.log("Count: " + count);
  count++;
  if (count > 30) {
    clearInterval(id); 
  }
}, 1000);



// time interval is used in the counter and can be changes every second
 