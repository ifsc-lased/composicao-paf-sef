var iconeCheck = "<i class=\"fa fa-check\" aria-hidden=\"true\"></i>";
var iconeClock = "<i class=\"fa fa-clock\" aria-hidden=\"true\"></i>";
var iconeBug = "<i class=\"fa fa-bug text-warning\" style=\"background: #fff; padding: 3px;\" aria-hidden=\"true\"></i>";
var iconeVer = "<i class=\"fa fa-eye\" aria-hidden=\"true\"></i>";
var iconeCarregando = "<img id=\"carregando\" src=\"" + $SCRIPT_ROOT + "/static/load.gif\"/>"

function getTime() {
    var dt = new Date();
    var hr = dt.getHours();
    hr = hr > 9 ? hr : "0" + hr;
    var min = dt.getMinutes();
    min = min > 9 ? min : "0" + min;
    var sec = dt.getSeconds();
    sec = sec > 9 ? sec : "0" + sec;
    var mse = dt.getMilliseconds();
    mse = mse > 9 ? mse : "0" + mse;
    mse = mse > 99 ? mse : "0" + mse;
    var time = hr + ":" + min + ":" + sec + "-" + mse;
    return time;
}

function execPasso(passo, token) {
    $("#l" + passo + " .time").html(getTime());
    $("#l" + passo + " .descricao").html($PASSOS[passo].descricao);
    $("#l" + passo + ">.icone").html(iconeCarregando);

    $.post($SCRIPT_ROOT + '/' + $PASSOS[passo].rota, {token: token}, function (data) {
            $("#l" + passo + " .icone").html(iconeCheck);
            $("#l" + passo + " .mostrar").html(iconeVer);

            pedido_antes = ""
            if (data.pedido.antes)
                pedido_antes = data.pedido.antes + '\n';

            pedido = data.pedido.texto
            if (data.pedido.tipo == "xml")
                pedido = vkbeautify.xml(pedido, 2);
            else if (data.pedido.tipo == "json")
                pedido = vkbeautify.json(pedido, 2);
            pedido = pedido_antes + pedido
            $("#l" + passo + " .up").text(pedido);

            resposta_antes = ""
            if (data.resposta.antes)
                resposta_antes = data.resposta.antes + '\n';
            if (data.resposta.antes_js)
                resposta_antes = resposta_antes + vkbeautify.json(data.resposta.antes_js, 2) + '\n';

            resposta_depois = ""
            if (data.resposta.depois)
                resposta_depois = '\n' + data.resposta.depois;
            if (data.resposta.depois_js)
                resposta_depois = resposta_depois + '\n' + vkbeautify.json(data.resposta.depois_js, 2);

            resposta = data.resposta.texto
            if (data.resposta.tipo == "xml")
                resposta = vkbeautify.xml(resposta, 2);
            else if (data.resposta.tipo == "json")
                resposta = vkbeautify.json(resposta, 2);
            resposta = resposta_antes + resposta + resposta_depois
            $("#l" + passo + " .down").text(resposta);

            $("#l" + passo + " .resultado").html(data.resultado);
            if (passo < $PASSOS.length - 1 && data.res_id == '0' && !data.erro)
                execPasso(passo + 1, data.token);
            else {
                if (data.res_id == '2')
                    $("#tentar_novamente").removeClass("hidden");
                $("#iniciar").html("<i class=\"fas fa-play\"></i>&nbsp;&nbsp;Iniciar");
                $("#iniciar").attr("executando", 0);
                if (!data.erro) {
                    $("#fim .time").html(getTime());
                    $("#fim .icone").html(iconeCheck);
                    $("#fim .resultado").html("Cenário concluído");
                } else {
                    $("#fim").addClass("btn-danger");
                    $("#fim .time").html(getTime());
                    $("#fim .icone").html(iconeBug);
                    $("#l" + passo + " .icone").html(iconeBug);
                    $("#l" + passo).removeClass("bg-light");
                    $("#l" + passo).addClass("btn-danger");
                    $("#fim .resultado").html("CENÁRIO INTERROMPIDO POR RESPOSTA INESPERADA!");
                }
            }
        }
        , 'json');
}

function resetPassos() {
    $(".passo").removeClass("btn-danger");
    $(".passo .time").html("");
    $(".passo .icone").html(iconeClock);
    $(".passo .resultado").html("");
    $("#fim").removeClass("btn-danger");
    $("#fim .time").html("");
    $(".msgs").hide();
    $(".mostrar").html("");
    $("#fim .icone").html(iconeClock);
}

$(window).load(function () {
    $(".mostrar").click(function () {
        var id = $(this).parent().attr("id");
        $("#" + id + ">table").toggle();
        var icone = $(this).children(0).attr("class");
        if ($(this).children(0).attr("class") == "fa fa-eye") {
            $(this).children(0).attr("class", "fa fa-eye-slash");
            $(this).attr("title", "Esconder mensagens de pedido e resposta");
        } else {
            $(this).children(0).attr("class", "fa fa-eye");
            $(this).attr("title", "Mostrar mensagens de pedido e resposta");
        }
    });

    $("#tentar_novamente").click(function () {
        $.post($SCRIPT_ROOT + '/passo_cancelar_processo', function (data) {
            $(this).html(iconeCarregando + " Cancelar processo e tentar novamente");
            if (data.res_id == '0' && !data.erro)
                location.reload();
        }, 'json');
    });
    resetPassos();
    $("#fim .icone").html(iconeCarregando);
    $("#fim .resultado").html("Executando cenário");
    $(this).html(iconeCarregando + "&nbsp;&nbsp; Executando");
    execPasso(0);
});