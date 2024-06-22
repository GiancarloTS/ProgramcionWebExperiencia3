function ActualizarHora(){
    var fecha = new Date();
    var segundos = fecha.getSeconds();
    var minutos = fecha.getMinutes();
    var horas = fecha.getHours();

    var elementoHoras = document.getElementById("Horas");
    var elementoMinutos = document.getElementById("Minutos");
    var elementoSegundos = document.getElementById("Segundos");

    elementoHoras.textContent = horas;
    elementoMinutos.textContent = minutos;
    elementoSegundos.textContent = segundos;
}

ActualizarHora();

setInterval(ActualizarHora,1000);