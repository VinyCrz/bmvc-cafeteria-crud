"""Modelo de domínio: um item do cardápio da cafeteria."""

# Categorias aceitas no cardápio: chave interna -> (nome exibido, ícone)
CATEGORIAS = {
    'cafes': ('Cafés Quentes', '☕'),
    'gelados': ('Bebidas Geladas', '🧊'),
    'doces': ('Doces', '🍰'),
    'salgados': ('Salgados', '🥐'),
}


class ItemCardapio:

    def __init__(self, id, nome, categoria, descricao, preco):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.descricao = descricao
        self.preco = float(preco)

    @property
    def nome_categoria(self):
        return CATEGORIAS.get(self.categoria, (self.categoria, ''))[0]

    @property
    def preco_formatado(self):
        valor = f'{self.preco:,.2f}'
        valor = valor.replace(',', 'X').replace('.', ',').replace('X', '.')
        return f'R$ {valor}'

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'categoria': self.categoria,
            'descricao': self.descricao,
            'preco': self.preco,
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            id=dados['id'],
            nome=dados['nome'],
            categoria=dados['categoria'],
            descricao=dados.get('descricao', ''),
            preco=dados['preco'],
        )

    def __repr__(self):
        return f'ItemCardapio(id={self.id}, nome={self.nome!r}, preco={self.preco})'
