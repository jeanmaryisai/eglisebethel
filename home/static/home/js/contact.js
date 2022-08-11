var btn = document.getElementById('btn');
    btn.addEventListener('click', function(e) {
            var name = document.getElementById('name').value;
            console.log('adfdfadafs')
            var msj = document.getElementById('message').value;
            var email = document.getElementById('email').value;
            var body = "name: " + name + '<br/> Subject: ' + 'Message du Blog Eglise Bethel' + ' <br/> From: ' + email + "<br/> body:" + msj;
            e.preventDefault()
            Email.send({
                Host: "smtp.elasticemail.com",
                Username: "jeanmaryisai@gmail.com",
                Password: "46B5863CB0D083F266E0609BBDD71538380F",
                To: 'jeanmaryisai@gmail.com',
                From: "jeanmaryisai@gmail.com",
                Subject: "Message from your blog",
                Body: body
            }).then(
                document.querySelector("message-sent").style.display = "flex",
                message => alert(message), console.log(body)
            )
        })