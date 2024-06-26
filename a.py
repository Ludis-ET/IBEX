
    <style>

      #ex4 .p1[data-count]:after{
  position:absolute;
  right:10%;
  top:8%;
  content: attr(data-count);
  font-size:40%;
  padding:.2em;
  border-radius:50%;
  line-height:1em;
  color: white;
  background:rgba(255,0,0,.85);
  text-align:center;
  min-width: 1em;
  //font-weight:bold;
}


#ex3 .fa-stack[data-count]:after{
  position:absolute;
  right:0%;
  top:1%;
  content: attr(data-count);
  font-size:30%;
  padding:.6em;
  border-radius:50%;
  line-height:.8em;
  color: white;
  background:rgba(255,0,0,.85);
  text-align:center;
  min-width: 1em;
  font-weight:bold;
}


/* on ex2 if you include bootstrap v3 css the number is a rounded circle with the .has-badge class */
#ex2 .fa-stack[data-count]:after{
  position:absolute;
  right:0%;
  top:1%;
  content: attr(data-count);
  font-size:30%;
  padding:.6em;
  border-radius:999px;
  line-height:.75em;
  color: white;
  background:rgba(255,0,0,.85);
  text-align:center;
  min-width:2em;
  font-weight:bold;
  padding:5px;
}




#ex1 .icon-grey {color: grey}
#ex1 i {   
    width:100px;
    text-align:center;
    vertical-align:middle;
    position: relative;
}
#ex1 .badge:after{
    content:"100";
    position: absolute;
    background: rgba(0,0,255,1);
    height:2rem;
    top:1rem;
    right:1.5rem;
    width:2.5rem;
    text-align: center;
    line-height: 2rem;;
    font-size: 1rem;
    border-radius: 50%;
    color:white;
    border:1px solid blue;
}
    </style>