//показ превью через File API
document.getElementById("id_file").onchange = function () {
    var reader = new FileReader();

    reader.onload = function (e) {
        document.getElementById("id_clear").style.display = "block";
        var image = document.getElementById("id_preview");
        image.src = e.target.result;
        image.classList.add("bordered");
        document.getElementById("id_file_label").hidden = true;
    };

    reader.readAsDataURL(this.files[0]);
};
// resetнуть выбранное изображение
document.getElementById("id_clear").onclick = function () {
    var image = document.getElementById("id_preview");
    image.src = "";
    image.classList.remove("bordered");
    document.getElementById("id_file").value = "";
    document.getElementById("id_file_label").hidden = false;
    document.getElementById("id_clear").style.display = "none";
}