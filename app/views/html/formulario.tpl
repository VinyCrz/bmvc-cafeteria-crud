% rebase('base', titulo=titulo)

<section class="painel-form">
    <h2>{{titulo}}</h2>
    <p class="dica">Preencha os dados abaixo. Campos com * são obrigatórios.</p>

    <div id="erros" class="erros{{' visivel' if erros else ''}}" role="alert">
        <ul>
            % for erro in erros:
            <li>{{erro}}</li>
            % end
        </ul>
    </div>

    <form id="form-item" method="post" action="{{acao}}" novalidate>
        <label for="nome">Nome do item *</label>
        <input id="nome" name="nome" type="text" maxlength="80" value="{{dados['nome']}}" placeholder="Ex.: Mocha com Avelã">

        <label for="categoria">Categoria *</label>
        <select id="categoria" name="categoria">
            % for chave, (nome_cat, icone) in categorias.items():
            <option value="{{chave}}" {{'selected' if dados['categoria'] == chave else ''}}>{{icone}} {{nome_cat}}</option>
            % end
        </select>

        <label for="descricao">Descrição</label>
        <textarea id="descricao" name="descricao" rows="3" maxlength="200" placeholder="Conte o que vai no item e o que ele tem de especial.">{{dados['descricao']}}</textarea>
        <small class="contagem"><span id="contagem-desc">0</span>/200 caracteres</small>

        <label for="preco">Preço (R$) *</label>
        <input id="preco" name="preco" type="text" inputmode="decimal" value="{{dados['preco']}}" placeholder="Ex.: 12,50">

        <div class="acoes-form">
            <button class="btn-principal" type="submit">{{botao}}</button>
            <a class="btn-secundario" href="/">Cancelar</a>
        </div>
    </form>
</section>
