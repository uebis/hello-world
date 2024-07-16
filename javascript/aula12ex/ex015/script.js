function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.querySelector('div#res')
    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert('[ERRO] Verifique os dados e tente novamente')
    }else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var gênero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fsex[0].checked) {
            gênero = 'Homem'
            if (idade >= 0 && idade < 10) {
                //Criança
                img.setAttribute('src', 'foto-bebe-h.png')
            } else if (idade < 21) {
                //Jovem
                img.setAttribute('src', 'foto-adolescente-h.png')
            }else if (idade < 50) {
                //Adulto
                img.setAttribute('src', 'foto-adulto-h.png')
            }else {
                //Idoso
                img.setAttribute('src', 'foto-idoso-h.png')
            }
        }else {
            gênero = 'Mulher'
            if (idade >= 0 && idade < 10) {
                //Criança
                img.setAttribute('src', 'foto-bebe-f.png')
            } else if (idade < 21) {
                //Jovem
                img.setAttribute('src', 'foto-adolescente-f.png')
            }else if (idade < 50) {
                //Adulta
                img.setAttribute('src', 'foto-adulta-f.png')
            }else {
                //Idosa
                img.setAttribute('src', 'foto-idosa-f.png')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${gênero} com ${idade} anos.`
        res.appendChild(img)
    }
}