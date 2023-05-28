var username = window.prompt("Please enter your name: ")
usernamediv= document.getElementById("username")
usernamediv.innerText = username



// use websocket to connect to the remote server

let mywebsocket  = new WebSocket("ws://localhost:8000")
console.log(mywebsocket)

mywebsocket.onopen= function (){

    // console.log("connection opened")
    // send my to the server ?
    data_to_send = {
        "username": username,
        "login":true
    }

    // sending data from client to server --> as string
    data = JSON.stringify(data_to_send)
    // console.log(data, typeof data)
    mywebsocket.send(data)
}