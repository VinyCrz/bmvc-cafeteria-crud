# Cardápio — Café Grão Dourado (BMVC II)

Projeto BMVC (Bottle + MVC em Python) para **gerenciar o cardápio de uma cafeteria fictícia**. Pelas páginas é possível listar, cadastrar, editar e excluir os itens servidos (cafés quentes, bebidas geladas, doces e salgados), com descrição e preço de cada um. Ou seja, é um CRUD completo.

## Modelo

`ItemCardapio` (`app/models/item_cardapio.py`) é uma classe Python com os atributos:

| Atributo    | Tipo  | Exemplo                       |
|-------------|-------|-------------------------------|
| `id`        | int   | `1`                           |
| `nome`      | str   | `"Cold Brew"`                 |
| `categoria` | str   | `"cafes"`, `"gelados"`, `"doces"` ou `"salgados"` |
| `descricao` | str   | `"Café extraído a frio..."`   |
| `preco`     | float | `12.0` (exibido como R$ 12,00) |

O `CardapioRepository` (`app/models/cardapio_repository.py`) guarda os objetos em `app/models/data/cardapio.json` e oferece os métodos `listar`, `buscar`, `criar`, `atualizar` e `excluir`.

## Rotas

| Método | Rota                      | Ação                    |
|--------|---------------------------|-------------------------|
| GET    | `/` ou `/cardapio`        | Lista o cardápio (Read) |
| GET    | `/itens/novo`             | Formulário de novo item |
| POST   | `/itens/novo`             | Cria o item (Create)    |
| GET    | `/itens/<id>/editar`      | Formulário de edição    |
| POST   | `/itens/<id>/editar`      | Salva a edição (Update) |
| POST   | `/itens/<id>/excluir`     | Exclui o item (Delete)  |
| GET    | `/static/<arquivo>`       | Serve o CSS e o JS      |

## CSS e JS

- **CSS** (`app/static/css/style.css`): layout em grade, paleta de cores, tema escuro, estilo dos formulários e botões, e responsividade para celular.
- **JS** (`app/static/js/script.js`): tema claro/escuro (salvo entre as páginas), filtro por categoria, confirmação antes de excluir, validação dos formulários (nome obrigatório e preço maior que zero), contador de caracteres da descrição e aviso de sucesso que some sozinho.

## Estrutura

```
route.py                              # rotas e ponto de entrada (localhost:8080)
app/controllers/application.py        # controlador (regras do CRUD e validação)
app/models/item_cardapio.py           # modelo ItemCardapio
app/models/cardapio_repository.py     # persistência em JSON
app/models/data/cardapio.json         # dados do cardápio
app/views/html/base.tpl               # layout comum (cabeçalho e rodapé)
app/views/html/lista.tpl              # listagem do cardápio
app/views/html/formulario.tpl         # formulário de criar/editar
app/static/css/style.css
app/static/js/script.js
```

## Como executar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 route.py
```

Depois, acesse http://localhost:8080 no navegador.
