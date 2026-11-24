// ---------- Tema claro/escuro (a escolha fica salva entre as páginas) ----------
const btnTema = document.getElementById('btn-tema');

function aplicarTema(escuro) {
    document.body.classList.toggle('escuro', escuro);
    btnTema.textContent = escuro ? '☀️ Tema claro' : '🌙 Tema escuro';
}

let temaSalvo = null;
try { temaSalvo = localStorage.getItem('tema'); } catch (e) { /* sem armazenamento */ }
aplicarTema(temaSalvo === 'escuro');

btnTema.addEventListener('click', function () {
    const escuro = !document.body.classList.contains('escuro');
    aplicarTema(escuro);
    try { localStorage.setItem('tema', escuro ? 'escuro' : 'claro'); } catch (e) { /* ignora */ }
});

// ---------- Filtro de categorias (página do cardápio) ----------
const filtros = document.querySelectorAll('.filtro');
const categorias = document.querySelectorAll('.categoria');

filtros.forEach(function (botao) {
    botao.addEventListener('click', function () {
        const escolhida = botao.dataset.categoria;

        filtros.forEach(function (b) { b.classList.remove('ativo'); });
        botao.classList.add('ativo');

        categorias.forEach(function (secao) {
            const mostrar = escolhida === 'todos' || secao.dataset.categoria === escolhida;
            secao.classList.toggle('oculta', !mostrar);
        });
    });
});

// ---------- Confirmação antes de excluir ----------
document.querySelectorAll('.form-excluir').forEach(function (form) {
    form.addEventListener('submit', function (evento) {
        const nome = form.dataset.nome;
        if (!confirm('Tem certeza que deseja excluir "' + nome + '" do cardápio?')) {
            evento.preventDefault();
        }
    });
});

// ---------- Aviso de sucesso some sozinho ----------
const aviso = document.getElementById('aviso');
if (aviso) {
    setTimeout(function () { aviso.classList.add('sumindo'); }, 3000);
    setTimeout(function () { aviso.remove(); }, 3600);
}

// ---------- Validação do formulário de item ----------
const formItem = document.getElementById('form-item');

if (formItem) {
    const caixaErros = document.getElementById('erros');
    const campoNome = document.getElementById('nome');
    const campoPreco = document.getElementById('preco');
    const campoDesc = document.getElementById('descricao');
    const contagem = document.getElementById('contagem-desc');

    // contador de caracteres da descrição
    function atualizarContagem() { contagem.textContent = campoDesc.value.length; }
    campoDesc.addEventListener('input', atualizarContagem);
    atualizarContagem();

    formItem.addEventListener('submit', function (evento) {
        const erros = [];
        campoNome.classList.remove('invalido');
        campoPreco.classList.remove('invalido');

        if (campoNome.value.trim() === '') {
            erros.push('Informe o nome do item.');
            campoNome.classList.add('invalido');
        }

        const preco = parseFloat(campoPreco.value.replace(',', '.'));
        if (isNaN(preco) || preco <= 0) {
            erros.push('O preço deve ser um número maior que zero (ex.: 12,50).');
            campoPreco.classList.add('invalido');
        }

        if (erros.length > 0) {
            evento.preventDefault();
            caixaErros.querySelector('ul').innerHTML = erros
                .map(function (e) { return '<li>' + e + '</li>'; })
                .join('');
            caixaErros.classList.add('visivel');
            caixaErros.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    });
}
