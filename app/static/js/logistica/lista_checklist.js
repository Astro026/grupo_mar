function toggleItems(index) {
    var itensDiv = document.getElementById("itens-" + index);
    if (itensDiv.style.display === "block") {
        itensDiv.style.display = "none";
    } else {
        itensDiv.style.display = "block";
    }
}



