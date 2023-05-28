var username = window.prompt("Please enter your name: ")
usernamediv= document.getElementById("username")
usernamediv.innerText = username
let msg = document.getElementById('msg')
let chat = document.getElementById('chat')

let mywebsocket  = new WebSocket("ws://localhost:8000")
console.log(mywebsocket)

mywebsocket.onopen= function (){
    data_to_send = {
        "username": username,
        "login":true
    }

    data = JSON.stringify(data_to_send)
    mywebsocket.send(data)
}


mywebsocket.onmessage= function (event){
    // console.log("--- message is being sent =====")
    console.log(event.data, typeof data) // string
    data = JSON.parse(event.data)
    chat.innerHTML += data.message
}

mywebsocket.onerror = function (){
    alert("server is not accepting connection right now ")
}

mywebsocket.onclose = function (){


}

msg.addEventListener("keyup",function (event) {
    console.log(event)
    if (event.code==="Enter"){
        mymsg =msg.value
        data_to_send = {
        "message": mymsg,
        "type":"chat",
        "username":username
        };

        data= JSON.stringify(data_to_send);
        mywebsocket.send(data);
        msg.value='';
        chat.innerHTML+="Me:"+mymsg+"\n"

    }
});