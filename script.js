const selectClass = document.querySelector("#pjclass");
const mudarImagem = document.querySelector("#imagem");
const rangeForca = document.querySelector("#rangeForca");
const rangeDestreza = document.querySelector("#rangeDestreza");
const rangeConstituicao = document.querySelector("#rangeConstituicao");
const rangeSabedoria = document.querySelector("#rangeSabedoria");
const rangeInteligencia = document.querySelector("#rangeInteligencia");
const mudarValorForca = document.querySelector("#mudarValorForca");
const mudarValorDestreza = document.querySelector("#mudarValorDestreza");
const mudarValorConstituicao = document.querySelector(
  "#mudarValorConstituicao"
);
const mudarValorSabedoria = document.querySelector("#mudarValorSabedoria");
const mudarValorInteligencia = document.querySelector(
  "#mudarValorInteligencia"
);
const imagemCampo = document.querySelector("#imagemCampo");
const classeEscolha = document.querySelector("#classeEscolha");
const pontosParaDistribuir = document.querySelector("#pontos");

console.log(pontosParaDistribuir);

selectClass.addEventListener("change", function () {
  let valor = selectClass.options[selectClass.selectedIndex].value;
  let valorText = selectClass.options[selectClass.selectedIndex].text;
  mudarImagem.setAttribute("src", `../static/img/${valor}.jpg`);

  // não deixar dar submit se valor == 0
  if (valor == 0) {
    console.log("Escolha uma classe 1");
  } else {
    console.log(valorText);
    classeEscolha.value = valorText;
    console.log(mudarImagem.getAttribute("src"));
    imagemCampo.value = mudarImagem.getAttribute("src");
  }
});

rangeForca.addEventListener("input", function () {
  mudarValorForca.textContent = this.value;
 
});

rangeDestreza.addEventListener("input", function () {
  mudarValorDestreza.textContent = this.value;
});

rangeConstituicao.addEventListener("input", function () {
  mudarValorConstituicao.textContent = this.value;
});

rangeSabedoria.addEventListener("input", function () {
  mudarValorSabedoria.textContent = this.value;
});

rangeInteligencia.addEventListener("input", function () {
  mudarValorInteligencia.textContent = this.value;
});


function teste() {
  let pontos = pontosParaDistribuir.textContent;
  let pontosInts = parseInt(pontos)
  let pt = pontosInts - 1
  console.log(--pt)
}