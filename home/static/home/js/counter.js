setInterval(()=>{
	const divcounter=document.getElementById('count-down')
    const linked=document.getElementById('linked')
    const time= divcounter.dataset['time']
    const time2= Date.parse(time)
    const now= new Date().getTime()
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
        divcounter.innerHTML= "Live strats in "+ h+ " hours "+ m +" minutes "+ s +" secondes."
    }
        linked.innerHTML=" Allez nous suivre."
    }
        else{
            divcounter.innerHTML="We are currently live, rejoin us!"
    }
},1000)