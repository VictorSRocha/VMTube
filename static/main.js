function some_botao() {
  var element = document.getElementById("enviar");
  element.classList.add("downloading");
  element.value = 'Downloading...';
  element.removeAttribute("onclick")
  element.style.cursor = 'auto';
}

function fechar_modal() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}

function show_pix() {
  var span_pix = document.getElementsByClassName("span-pix")[0];
  var pix = document.getElementsByClassName("wid300")[0];
  pix.style.paddingRight = "150px";
  span_pix.style.opacity =  '1';
  span_pix.style.paddingLeft =  '20px';
}
