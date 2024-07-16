var agora = new Date()
var hora = agora.getHours()
var minuto = agora.getMinutes()
console.log(`Agora são ${hora} hora(s) e ${minuto} minuto(s).`)
if (hora > 4 && hora < 12) {
    console.log('Bom Dia!')
} else if (hora >=12 && hora < 18) {
    console.log('Boa Tarde!')
} else if (hora >= 18) {
    console.log('Boa Noite!')
} else {
    console.log('Boa Madrugada!')
}
