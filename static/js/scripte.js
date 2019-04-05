var colors = ["#e6194B", "#3cb44b", "#ffe119", "#4363d8", "#f58231", "#911eb4", "#42d4f4", "#f032e6", "#bfef45", "#fabebe", "#469990", "#e6beff", "#9A6324", "#fffac8", "#800000", "#aaffc3", "#808000", "#ffd8b1", "#000075", "#a9a9a9", "#ffffff"];

function setColor() {
    var randNum = Math.floor(Math.random() * 20);
    var header = document.getElementsByTagName("header");
    header[0].style.borderBottomColor = colors[randNum];
}
