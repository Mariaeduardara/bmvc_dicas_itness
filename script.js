function adicionarDica() {
    const input = document.getElementById("input-dica");
    const texto = input.value.trim();

    if (texto === "") {
        alert("Digite uma dica antes de adicionar!");
        return;
    }

    const lista = document.getElementById("lista-dicas");
    const novaDica = document.createElement("li");
    novaDica.textContent = texto;

    lista.appendChild(novaDica);
    input.value = "";
}
