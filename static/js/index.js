var intervalo;

function scrollDireita(idx){
  console.log(idx)
  intervalo = setInterval(function(){ document.getElementById('scroller'+idx).scrollLeft += 1 }  , 5);
};
function scrollEsquerda(idx){
  intervalo = setInterval(function(){ document.getElementById('scroller'+idx).scrollLeft -= 1 }  , 5);
};
function clearScroll(){
  clearInterval(intervalo);
};
