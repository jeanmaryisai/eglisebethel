setInterval(()=>{
    console.log('hi')
	const divcounter=document.getElementById('count-down')
    const linked=document.getElementById('linked')
    const time= divcounter.dataset['time']
    const time2= Date.parse(time)
    var dt = new Date();
    var utc = dt.getTime() + (dt.getTimezoneOffset() * 60000);

    // create new Date object for different city
    // using supplied offset
    var now = new Date(utc + (3600000*'-4'))

    const nowd= new Date().getTime()
    const diff= time2-now
    const d= Math.floor((time2/ (1000 * 60 * 60 *24)) - (now / (1000 * 60 * 60*24 )))
    const h= Math.floor(((time2/ (1000 * 60 * 60)) - (now / (1000 * 60 * 60 )))%24)
    const m= Math.floor(((time2/ (1000 * 60 )) - (now / (1000 * 60  )))%60)
    const s= Math.floor(((time2/ (1000)) - (now / (1000)))%60)
    if(diff>0){
        if(d>0){
            divcounter.innerHTML= "Live will starts in "+d+" days "+ h+ " hours "+ m +" minutes "+ s +" secondes."
        }
        else{
        divcounter.innerHTML= "Live starts in "+ h+ " hours "+ m +" minutes "+ s +" secondes."
    }
        linked.innerHTML=" Allez nous suivre."
    }
        else{
            divcounter.innerHTML="We are currently live, rejoin us!"
    }
},1000)