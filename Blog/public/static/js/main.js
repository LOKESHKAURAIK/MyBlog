function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value


    if (username == '' && password == '') {
        alert('You must enter both')
        
    }

    var data = {
         "username" : username,
         "password" : password
        
    }
                            // code for fetching an APIs { https://www.brennantymrak.com/articles/fetching-data-with-ajax-and-django }
    fetch('/api/login/' ,{
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf,
        },
        body : JSON.stringify(data) 
    }).then(result => result.json())
    .then(response => {
        if(response.status == 200){
            window.location.href = '/'
          }
          else{
            alert(response.message)
          }
    })
    
}

// document.getElementById("new-btn").addEventListener("click", ()=>{
//     if(username == "" && password == ""){
//         console.log("Please enter name and pass");
//     }
// })