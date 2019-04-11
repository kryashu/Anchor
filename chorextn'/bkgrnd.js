 chrome.runtime.onInstalled.addListener(function() { 
function timer(ms) {
 return new Promise(res => setTimeout(res, ms));
}

async function load (data){
var obj = JSON.parse(data);
for (var i = 0, len = obj.length; i < len; i++){
var j = 0;	
window.open('https://api.whatsapp.com/send?phone=91'+obj[i].phone+'&text='+obj[i].mesaage);
const http = new XMLHttpRequest();
http.open("GET", "http://localhost:8080/message/"+obj[i].phone);
http.send();
j++;
var n = Math.floor((Math.random() * 10)+1);
await timer(n*1000);

}
}

const http = new XMLHttpRequest()
http.open("GET", "http://localhost:8080/phone")
http.send()
http.onload = () => load(http.responseText)
});