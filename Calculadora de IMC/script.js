function calcular() {
    let peso = parseFloat(document.getElementById("peso").value)
    let altura = parseFloat(document.getElementById("altura").value)

    let calc = peso / (altura ** 2)
    calc = calc.toFixed(2)

    if(calc <= 18.5) {
        document.getElementById("resultado").innerText = `IMC = ${calc}\nAbaixo do peso`
    } else if (calc > 18.5 && calc <= 24.99) {
        document.getElementById("resultado").innerText = `IMC = ${calc}\nNormal`
    } else if (calc > 25 && calc <= 29.99) {
        document.getElementById("resultado").innerHTML = `IMC = ${calc}\nSobrepeso`
    } else if (calc > 30) {{
        document.getElementById("resultado").innerHTML = `IMC = ${calc}\nObesidade`
    }}

}
/*
let idade1 = parseInt(prompt("Digite uma idade"))
let idade2 = parseInt(prompt("Digite uma segunda idade"))

let calc = idade1 + idade2
*/

/*
if(idade >= 18) {
    document.write("Maior")
} else {
    document.write("Menor")
}
*/