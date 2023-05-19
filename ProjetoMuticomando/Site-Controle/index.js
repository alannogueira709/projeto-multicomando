var contentApresentacao = document.getElementsByClassName("content-apresentacao")[0];
var contentControle = document.getElementsByClassName("content-controle")[0];

var inputModalidade = document.getElementById("modalidade");
var url_modo = "http://localhost:8000/modo"
var url_atos = "http://localhost:8000/acts"
var url_apresentacao = "http://localhost:8000/presentation"


inputModalidade.addEventListener("change", event => {
    var value = event.target.value;
    
    if (value == "Apresentação") {
        if(contentApresentacao.classList.contains("display-none")) {
            contentApresentacao.classList.remove("display-none");
        }
        if(!contentControle.classList.contains("display-none")) {
            contentControle.classList.add("display-none");
        }
    } else {
        if(!contentApresentacao.classList.contains("display-none")) {
            contentApresentacao.classList.add("display-none");
        }
        if(contentControle.classList.contains("display-none")) {
            contentControle.classList.remove("display-none");
        }
    }

    fetch(url_modo, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'modo':value})
    })
})


var numRobos = 3;
var elementsRobos = document.getElementsByClassName("robo");

Array.from(elementsRobos).forEach((value, index) => {
    index += 1;
    if(index <= numRobos) {
        if(value.classList.contains("robo-offline")) {
            value.classList.remove("robo-offline")
        }
        value.classList.add("robo-online");
    } else {
        if(value.classList.contains("robo-online")) {
            value.classList.remove("robo-online")
        }
        value.classList.add("robo-offline")
    }
})

var apresentacaoInput = document.getElementById("apresentacao");
var numApresentacao;

apresentacaoInput.addEventListener('change', event => {
    numApresentacao = event.target.value;

    fetch(url_apresentacao, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'apresentacao':numApresentacao})
    })
});

var musicaInput = document.getElementById("musica");
var musicaNome;
var piscarCheckbox = document.getElementById("piscar");
var piscar;

musicaInput.addEventListener('change', event => {
    musicaNome = event.target.value;

    fetch(url_atos, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'musica':musicaNome})
    })
})

piscarCheckbox.addEventListener('change', event => {
    piscar = event.target.checked

    fetch(url_atos, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'piscar': piscar})
    })
})

var joystickCima = document.getElementById("button-cima");
var joystickEsquerda = document.getElementById("button-esquerda");
var joystickDireita = document.getElementById("button-direita");
var joystickBaixo = document.getElementById("button-baixo");

joystickCima.onmousedown = () => {
    fetch(url_atos, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'movimento': "frente"})
    })
}

joystickCima.onmouseup = () => {
    fetch(url_atos, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'movimento': "parar"})
    })
}

joystickEsquerda.onmousedown = () => {
    fetch(url_atos, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'movimento': "esquerda"})
    })
}

joystickEsquerda.onmouseup = () => {
    fetch(url_atos, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'movimento': "parar"})
    })
}

joystickDireita.onmousedown = () => {
    fetch(url_atos, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'movimento': "direita"})
    })
}

joystickDireita.onmouseup = () => {
    fetch(url_atos, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'movimento': "parar"})
    })
}

joystickBaixo.onmousedown = () => {
    fetch(url_atos, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'movimento': "tras"})
    })
}

joystickBaixo.onmouseup = () => {
    fetch(url_atos, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'movimento': "parar"})
    })
}

var ledInputs = document.getElementsByClassName("led-input");
var ledByte = [0, 0, 0, 0, 0, 0, 0, 0];
var ledFinal;

Array.from(ledInputs).forEach((led, index) => {
    led.addEventListener('change', event => {
        var ledState = event.target.checked ? 1 : 0;

        ledByte[index] = ledState
        ledFinal = ledByte.join().replaceAll(",", "");
        fetch(url_atos, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'leds': ledFinal})
        })
    })
})