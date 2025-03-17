

function abrir_div(param){

    document.getElementById(param).style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
    
    var id_front = param

    console.log('abrir | parametro', param)
    return id_front
}


function fechar_div(){
    document.getElementById('overlay').style.display = 'none';
    document.querySelectorAll(".modal").forEach(div => {
        div.style.display = 'none';
    });


}