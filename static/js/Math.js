function Autonomo() {
    const level1 = document.getElementById("l1_A")
    const level2 = document.getElementById("l2_a")
    const level3 = document.getElementById("l3_a")
    const level4 = document.getElementById("l4_a")
    const processor_in = document.getElementById("processor_a")
    const net_in = document.getElementById("net_a")

    var l1 = 3
    var l2 = 4
    var l3 = 6
    var l4 = 7
    
    var p = 6
    var n = 4

    return (l1 * level1) + (l2 * level2) + (l3 * level3) + (l4 * level4) + (processor_in * p) + (net_in * n)

}

function TeleOp() {
    const level1 = document.getElementById("l1_t")
    const level2 = document.getElementById("l2_t")
    const level3 = document.getElementById("l3_t")
    const level4 = document.getElementById("l4_t")
    const processor_in = document.getElementById("processor_t")
    const net_in = document.getElementById("net_t")

    var l1 = 3
    var l2 = 4
    var l3 = 6
    var l4 = 7
    
    var p = 6
    var n = 4

    return (l1 * level1) + (l2 * level2) + (l3 * level3) + (l4 * level4) + (processor_in * p) + (net_in * n)
}

function End() {
    const pos = document.getElementById("estaciona")

    if (pos == "No se estaciono") {
        pos = 0
    } else if (pos == "Intento pero no pudo") {
        pos = 0
    } else if (pos == "barage zone") {
        pos = 2
    } else if (pos == "shallow cage") {
        pos = 6
    } else if (pos == "deep cage") {
        pos = 12
    }

    return pos


}

let autonomo = Autonomo()
let teleOp = TeleOp()
let end = End()

document.getElementById("autonomo").innerHTML = autonomo;
document.getElementById("teleOp").innerHTML = teleOp;
document.getElementById("end").innerHTML = end;