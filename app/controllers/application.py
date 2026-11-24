from bottle import template, redirect, abort, TEMPLATE_PATH

from app.models.item_cardapio import CATEGORIAS
from app.models.cardapio_repository import CardapioRepository

TEMPLATE_PATH.insert(0, './app/views/html')

MENSAGENS = {
    'criado': 'Item adicionado ao cardápio com sucesso!',
    'editado': 'Item atualizado com sucesso!',
    'excluido': 'Item removido do cardápio.',
}


class Application:

    def __init__(self):
        self.repo = CardapioRepository()

    # ---------- READ ----------

    def listar(self, codigo_msg=None):
        return template(
            'lista',
            itens=self.repo.listar(),
            categorias=CATEGORIAS,
            mensagem=MENSAGENS.get(codigo_msg),
        )

    # ---------- CREATE ----------

    def formulario_novo(self):
        dados = {'nome': '', 'categoria': 'cafes', 'descricao': '', 'preco': ''}
        return self._form('Novo item do cardápio', '/itens/novo', 'Adicionar item', dados)

    def criar(self, form):
        dados, erros = self._validar(form)
        if erros:
            return self._form('Novo item do cardápio', '/itens/novo', 'Adicionar item', form_dados(form), erros)
        self.repo.criar(**dados)
        redirect('/?msg=criado')

    # ---------- UPDATE ----------

    def formulario_editar(self, id):
        item = self._buscar_ou_404(id)
        dados = {
            'nome': item.nome,
            'categoria': item.categoria,
            'descricao': item.descricao,
            'preco': f'{item.preco:.2f}'.replace('.', ','),
        }
        return self._form(f'Editar: {item.nome}', f'/itens/{id}/editar', 'Salvar alterações', dados)

    def atualizar(self, id, form):
        item = self._buscar_ou_404(id)
        dados, erros = self._validar(form)
        if erros:
            return self._form(f'Editar: {item.nome}', f'/itens/{id}/editar', 'Salvar alterações', form_dados(form), erros)
        self.repo.atualizar(id, **dados)
        redirect('/?msg=editado')

    # ---------- DELETE ----------

    def excluir(self, id):
        if not self.repo.excluir(id):
            abort(404, 'Item não encontrado.')
        redirect('/?msg=excluido')

    # ---------- auxiliares ----------

    def _buscar_ou_404(self, id):
        item = self.repo.buscar(id)
        if item is None:
            abort(404, 'Item não encontrado.')
        return item

    def _form(self, titulo, acao, botao, dados, erros=None):
        return template(
            'formulario',
            titulo=titulo,
            acao=acao,
            botao=botao,
            dados=dados,
            categorias=CATEGORIAS,
            erros=erros or [],
        )

    def _validar(self, form):
        """Valida os dados enviados pelo formulário (também validados no JS)."""
        bruto = form_dados(form)
        erros = []

        if not bruto['nome']:
            erros.append('Informe o nome do item.')
        if bruto['categoria'] not in CATEGORIAS:
            erros.append('Escolha uma categoria válida.')

        try:
            preco = float(bruto['preco'].replace(',', '.'))
            if preco <= 0:
                erros.append('O preço deve ser maior que zero.')
        except ValueError:
            preco = 0
            erros.append('Informe um preço válido, por exemplo 12,50.')

        dados = {
            'nome': bruto['nome'],
            'categoria': bruto['categoria'],
            'descricao': bruto['descricao'],
            'preco': round(preco, 2),
        }
        return dados, erros


def form_dados(form):
    """Lê os campos do formulário como texto (UTF-8), sem espaços nas pontas."""
    return {
        campo: (form.getunicode(campo) or '').strip()
        for campo in ('nome', 'categoria', 'descricao', 'preco')
    }
