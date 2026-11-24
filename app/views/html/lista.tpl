% rebase('base', titulo='Cardápio')

% if mensagem:
<div class="aviso" id="aviso" role="status">{{mensagem}}</div>
% end

<section class="intro">
    <h2>Nosso cardápio</h2>
    <p>Gerencie aqui os itens servidos na cafeteria: adicione novidades, ajuste preços e retire o que saiu de linha.
       Hoje temos <strong>{{len(itens)}}</strong> itens cadastrados.</p>
    <a class="btn-principal" href="/itens/novo">➕ Adicionar item</a>
</section>

<nav class="filtros" aria-label="Categorias do cardápio">
    <button class="filtro ativo" data-categoria="todos" type="button">Todos</button>
    % for chave, (nome_cat, icone) in categorias.items():
    <button class="filtro" data-categoria="{{chave}}" type="button">{{nome_cat}}</button>
    % end
</nav>

<div class="cardapio">
    % for chave, (nome_cat, icone) in categorias.items():
    % itens_cat = [i for i in itens if i.categoria == chave]
    <section class="categoria" data-categoria="{{chave}}">
        <h2>{{icone}} {{nome_cat}} <span class="contador">{{len(itens_cat)}}</span></h2>
        % if not itens_cat:
        <p class="vazio">Nenhum item nesta categoria ainda.</p>
        % else:
        <ul class="itens">
            % for item in itens_cat:
            <li class="item">
                <div class="item-info">
                    <h3>{{item.nome}}</h3>
                    <p>{{item.descricao}}</p>
                    <div class="item-acoes">
                        <a class="btn-acao editar" href="/itens/{{item.id}}/editar">✏️ Editar</a>
                        <form class="form-excluir" method="post" action="/itens/{{item.id}}/excluir" data-nome="{{item.nome}}">
                            <button class="btn-acao excluir" type="submit">🗑️ Excluir</button>
                        </form>
                    </div>
                </div>
                <span class="preco">{{item.preco_formatado}}</span>
            </li>
            % end
        </ul>
        % end
    </section>
    % end
</div>
