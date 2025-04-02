function toggleExpand(element) {
    element.classList.toggle("expanded");
}

ocument.addEventListener("DOMContentLoaded", function() {
    // Pega todos os radios
    const radios = document.querySelectorAll("input[name='searchType']");
    const searchInput = document.getElementById("searchInput");

    // Adiciona evento para alterar o input conforme o radio selecionado
    radios.forEach(radio => {
        radio.addEventListener("change", function() {
            if (this.value === "data") {
                searchInput.type = "date";
                searchInput.placeholder = "Selecione a data";
            } else {
                searchInput.type = "text";
                searchInput.placeholder = "Digite para pesquisar...";
            }
        });
    });
});

// Função para pesquisar (pode ser conectada ao backend depois)
function pesquisar() {
    const selectedOption = document.querySelector("input[name='searchType']:checked").value;
    const searchValue = document.getElementById("searchInput").value;

    if (!searchValue) {
        alert("Por favor, insira um valor para pesquisa!");
        return;
    }

    alert(`Pesquisando por ${selectedOption}: ${searchValue}`);
}