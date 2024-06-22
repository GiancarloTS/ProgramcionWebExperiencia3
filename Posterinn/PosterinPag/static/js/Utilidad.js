var tiempo = {}; 
var clock = new Date("2024-07-01 5:00:00 PM"); // Obtener la fecha y almacenar en clock

function mostrar_hora(){
  var now = new Date();  
  var diff = clock - now;
  // Inserta la hora almacenada en clock en el span con id hora
  tiempo.horas = document.getElementById('hora');
  tiempo.horas.innerHTML = now.getHours() - clock.getHours(); 
  
  
  // Inserta los minutos almacenados en clock en el span con id minuto
  tiempo.minuto = document.getElementById('minuto');
  tiempo.minuto.innerHTML = clock.getMinutes()+60 - now.getMinutes();
  
  // Inserta los segundos almacenados en clock en el span con id segundo
  tiempo.segundos = document.getElementById('segundo')
  tiempo.segundos.innerHTML = "0" + clock.getSeconds()+60 - now.getSeconds();
  
  tiempo.dias = document.getElementById('dias')
  total = diff/(1000*60*60*24)
  tiempo.dias.innerHTML = math.floor(total);

}

mostrar_hora();

setInterval(mostrar_hora,1);