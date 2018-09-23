
$(function() {
    $('[data-toggle="tooltip"]').tooltip();
});

$(function() {
    $('[data-toggle="popover"]').popover();
});


$("#id_nome").blur(function() { validaNomeFunction() });
$("#id_email").blur(function() { validaEmailFunction() });
$("#id_faixa_etaria").change(function (){validaFaixaEtariaFunction()});

$("#id_feminino").click(function (){validaSexoFunction()});
$("#id_masculino").click(function (){validaSexoFunction()});

$("#id_esporte").change(function (){validaPreferenciasFunction()});
$("#id_cinema").change(function (){validaPreferenciasFunction()});
$("#id_literatura").change(function (){validaPreferenciasFunction()});


$("#formulario").submit(function(e) {
    e.preventDefault();
    let nomeValido = validaNomeFunction();
    let email = validaEmailFunction();
    let idade = validaFaixaEtariaFunction();
    let sexo = validaSexoFunction();
    let pref = validaPreferenciasFunction();
    if (nomeValido) {
        if(email){
            if(idade){
                if(sexo){
                    if(pref) {
                        alert("Tudo OK!");
                    }
                    else {
                        alert("Preferencias incorretas!");
                    }
                }else{
                    alert("Sexo Incorreto!");
                }

            }else{
                alert('Idade Incorreta!');
            }
        }else{
            alert('Email Incorreto!');
        }
    }
    else {
        alert('Nome Incorreto!');
    }
});

function validaNomeFunction() {
    // console.log(e.charCode);
    // return e.charCode >= 48 && e.charCode <= 57;
    let nome = $("#id_nome");
    console.log(nome.val());
    if (nome.val() === '') {
        nome.addClass('is-invalid');
        nome.removeClass('is-valid');
        $("#idNomeRequired").removeClass('d-none');
        return false;
    }
    else {
        nome.removeClass('is-invalid');
        nome.addClass('is-valid');
        $("#idNomeRequired").addClass('d-none');
        return true;
    }
}

function validaEmailFunction() {
    let email = $("#id_email");
    if (email.val() === '') {
        email.addClass('is-invalid');
        email.removeClass('is-valid');
        $("#idEmailRequired").removeClass('d-none')
        return false;
    }
    else {
        $("#idEmailRequired").addClass('d-none');
        if (emailValido(email.val())) {
            email.removeClass('is-invalid');
            email.addClass('is-valid');
            $("#idEmailRequired").addClass('d-none');
            $("#idEmailValido").addClass('d-none');
            return true;
        }
        else {
            email.removeClass('is-valid');
            email.addClass('is-invalid');
            $("#idEmailRequired").addClass('d-none');
            $("#idEmailValido").removeClass('d-none');
            return false;
        }
    }
}

function emailValido(email) {
    let re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function validaFaixaEtariaFunction(){
    let idade = $("#id_faixa_etaria");
    if(idade.val() ==='0'){
        idade.removeClass('is-valid');
        idade.addClass('is-invalid');
        $("#id_faixa_etaria_required").removeClass("d-none");
    }else {
        idade.addClass('is-valid');
        idade.removeClass('is-invalid');
        $("#id_faixa_etaria_required").addClass("d-none");
        return true;
    }
}

function validaSexoFunction() {
    var  sexoM = $("#id_masculino");
    var  sexoF = $("#id_feminino");
    if(!sexoM.prop("checked") && !sexoF.prop("checked")){
        sexoM.removeClass('is-valid');
        sexoM.addClass('is-invalid');
        sexoF.removeClass('is-valid');
        sexoF.addClass('is-invalid');
        $("#id_sexo_required").removeClass("d-none");
    }else {
        sexoM.addClass('is-valid');
        sexoM.removeClass('is-invalid');
        sexoF.addClass('is-valid');
        sexoF.removeClass('is-invalid');
        $("#id_sexo_required").addClass("d-none");
        return true;
    }
}

function validaPreferenciasFunction() {
    let sport = $("#id_esporte");
    let cinema = $("#id_cinema");
    let literatura = $("#id_literatura");

    if(!sport.prop("checked") && !cinema.prop("checked") && !literatura.prop("checked") ){
        sport.removeClass('is-valid');
        sport.addClass('is-invalid');
        cinema.removeClass('is-valid');
        cinema.addClass('is-invalid');
        literatura.removeClass('is-valid');
        literatura.addClass('is-invalid');
        $("#id_preferencias_required").removeClass("d-none");
    }else{
        sport.addClass('is-valid');
        sport.removeClass('is-invalid');
        cinema.addClass('is-valid');
        cinema.removeClass('is-invalid');
        literatura.addClass('is-valid');
        literatura.removeClass('is-invalid');
        $("#id_preferencias_required").addClass("d-none");
        return true;
    }

}