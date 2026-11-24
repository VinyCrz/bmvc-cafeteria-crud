<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{titulo}} — Café Grão Dourado</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header class="topo">
        <div class="topo-conteudo">
            <h1><a href="/">Café Grão Dourado</a></h1>
            <p class="slogan">Cafés especiais torrados na casa, desde 2015</p>
        </div>
        <button id="btn-tema" class="btn-tema" type="button" aria-label="Alternar tema">🌙 Tema escuro</button>
        <nav class="menu" aria-label="Menu principal">
            <a href="/">📋 Cardápio</a>
            <a href="/itens/novo">➕ Novo item</a>
        </nav>
    </header>

    <main class="conteudo">
        {{!base}}
    </main>

    <footer class="rodape">
        <p><strong>Horário:</strong> segunda a sábado, das 7h às 20h · domingo, das 8h às 14h</p>
        <p>Rua das Palmeiras, 120 — Centro · Aceitamos Pix e cartões</p>
    </footer>

    <script src="/static/js/script.js"></script>
</body>
</html>
