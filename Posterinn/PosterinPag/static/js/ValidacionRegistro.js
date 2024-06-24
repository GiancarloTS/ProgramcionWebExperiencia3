const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');


const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	password: /^.{4,12}$/, // 4 a 12 digitos.
	correo: /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/, // /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{7,14}$/ // 7 a 14 numeros.
}

const campos = { //En mayusculas ya que las Id que estan en validar campo estan en mayusculas
    Nombre: false,
    Usuario: false,
    Correo: false,
    Clave: false
}

const validarFormulario = (evento) => {
    switch (evento.target.name) {
        case "nombre":
            validarCampo(expresiones.nombre, evento.target, 'Nombre');
        break;
        case "usuario":
            validarCampo(expresiones.usuario, evento.target, 'Usuario');
        break;
        case "correo":
            validarCampo(expresiones.correo, evento.target, 'Correo');
        break;
        case "clave":
            validarCampo(expresiones.password, evento.target, 'Clave');
            validarClave2();
        break;
        case "clave2":
            validarClave2();
        break;

    }
}



const validarCampo = (expresion, input, campo) => {
    if(expresion.test(input.value)){
        document.getElementById(`grupo${campo}`).classList.remove('formulario-incorrecto');
        document.getElementById(`grupo${campo}`).classList.add('formulario-correcto');
        document.querySelector(`#grupo${campo} i`).classList.remove('fa-circle-xmark');
        document.querySelector(`#grupo${campo} i`).classList.add('fa-circle-check');
        document.querySelector(`#grupo${campo} .mensajeError`).classList.remove('mensajeError-activo');
        campos[campo] = true;
    }
    else{
        document.getElementById(`grupo${campo}`).classList.add('formulario-incorrecto');
        document.querySelector(`#grupo${campo} i`).classList.add('fa-circle-xmark');
        document.querySelector(`#grupo${campo} i`).classList.remove('fa-clipboard-check');
        document.querySelector(`#grupo${campo} .mensajeError`).classList.add('mensajeError-activo');
        campos[campo] = false;
    }
}


const validarClave2 = () => {
    const inputClaves1 = document.getElementById('inputClave');
    const inputClaves2 = document.getElementById('inputClave2');

    if(inputClaves1.value !== inputClaves2.value){
        document.getElementById(`grupoClave2`).classList.add('formulario-incorrecto');
        document.querySelector(`#grupoClave2 i`).classList.add('fa-circle-xmark');
        document.querySelector(`#grupoClave2 i`).classList.remove('fa-circle-check');
        document.querySelector(`#grupoClave2 .mensajeError`).classList.add('mensajeError-activo');
        campos['inputClave'] = false;
    }
    else{
        document.getElementById(`grupoClave2`).classList.remove('formulario-incorrecto');
        document.getElementById(`grupoClave2`).classList.add('formulario-correcto');
        document.querySelector(`#grupoClave2 i`).classList.remove('fa-circle-xmark');
        document.querySelector(`#grupoClave2 i`).classList.add('fa-circle-check');
        document.querySelector(`#grupoClave2 .mensajeError`).classList.remove('mensajeError-activo');
        campos['inputClave'] = true;
    }
}




inputs.forEach((input) => { //CADA INPUT TENDRA UN EVENTO
    input.addEventListener('keyup' , validarFormulario);
    input.addEventListener('blur' , validarFormulario);
});

formulario.addEventListener('submit', (evento) => {
    evento.preventDefault();//NO PASARA NADA CUANDO SE PRESIONE EL BOTON7//
    
    if(campos.Nombre && campos.Correo && campos.Usuario && campos.Clave){
        formulario.reset();

        document.getElementById('mensajeExito').classList.add('mensajeExito-activo');
        setTimeout(() => {
            document.getElementById('mensajeExito').classList.remove('mensajeExito-activo');
        }, 4000);

        document.querySelectorAll('.formulario-correcto').forEach((icono) => {
            icono.classList.remove('formulario-correcto');
        });

        document.getElementById('formularioMensaje').classList.remove('formularioMensaje-activo');
    }
    else{
        document.getElementById('formularioMensaje').classList.add('formularioMensaje-activo');
    }
    
}); 