const screen = document.getElementById("screen")
 function insert(value){
    if (screen.textcontent===0){
        screen.textContent = value;
    }
    else{
        screen.textContent+=value;
    }
}
function clear(){
    screen.textContent==="0";
}
function del(){
    if (screen.textContent.length==="1"){
        screen.textContent=="0";
    }
    else {
        screen.textContent=screen.textContent.slice(0,-1) ;
    }
}
function equal(){
    try{
        screen.textContent=eval(screen.textContent);
    }
    catch{
        screen.textContent="Error";
    }

}
function sqr(){
    try{
        screen.textContent=eval(screen.textContent**2);
    }
    catch{
        screen.textContent="Error";
    }
}

function root(){
    try{
        screen.textContent=eval(Math.sqrt(screen.textContent));
    }    
    catch{
        screen.textContent="Error";
    }
}
