var colors = ["#FFFF00", "#E6FB04", "#FF0000", "#FD1C03", "#FF3300", "#FF6600", "#00FF00", "#00FF33", "#00FF66", "#33FF00 ", "#00FFFF", "#099FFF", "#0062FF", "#0033FF", "#FF00FF", "#FF00CC", "#FF0099", "#CC00FF", "#9D00FF", "#CC00FF", "#6E0DD0", "#9900FF"];

function setColor() {
    var randNum = Math.floor(Math.random() * 22);
    var header = document.getElementsByTagName("header");
    var footer = document.getElementsByTagName("footer");
    header[0].style.borderBottomColor = colors[randNum];
    footer[0].style.borderTopColor = colors[randNum];
}
