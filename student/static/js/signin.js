var email=document.getElementById('email')
var pass1=document.getElementById('pass1')

function validmail(){
    var mail=email.value;
    var re=/^[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5}$/;
    if (re.test(mail)){
        email.className= "success";
        document.getElementById("text").innerHTML= "";
    }
    else{
        email.className= "error";
        document.getElementById("sign").disabled = true
        document.getElementById("text").innerHTML= "please enter a valid mail id"
    }
}
function validpass(){
    var passl=pass1.value.length;
    if (passl >= 8 & passl <= 16){
        pass1.className="success"
        document.getElementById("sign").disabled = false
        document.getElementById("text").innerHTML=""
    }
    else{
        pass1.className="error"
        document.getElementById("sign").disabled = true
        document.getElementById("text").innerHTML="Password length must be greater than 8 characters and not must be 16"

    }
}
document.getElementById("sign").disaabled = true
