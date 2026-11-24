"""Repositório que guarda os objetos ItemCardapio em um arquivo JSON."""

import json
import os

from app.models.item_cardapio import ItemCardapio

ARQUIVO_PADRAO = os.path.join(os.path.dirname(__file__), 'data', 'cardapio.json')


class CardapioRepository:

    def __init__(self, caminho=ARQUIVO_PADRAO):
        self.caminho = caminho

    # ---------- leitura e gravação do arquivo ----------

    def _carregar(self):
        if not os.path.exists(self.caminho):
            return []
        with open(self.caminho, encoding='utf-8') as arquivo:
            return [ItemCardapio.from_dict(d) for d in json.load(arquivo)]

    def _salvar(self, itens):
        with open(self.caminho, 'w', encoding='utf-8') as arquivo:
            json.dump([i.to_dict() for i in itens], arquivo, ensure_ascii=False, indent=4)

    # ---------- CRUD ----------

    def listar(self):
        return self._carregar()

    def buscar(self, id):
        for item in self._carregar():
            if item.id == id:
                return item
        return None

    def criar(self, nome, categoria, descricao, preco):
        itens = self._carregar()
        novo_id = max((i.id for i in itens), default=0) + 1
        item = ItemCardapio(novo_id, nome, categoria, descricao, preco)
        itens.append(item)
        self._salvar(itens)
        return item

    def atualizar(self, id, nome, categoria, descricao, preco):
        itens = self._carregar()
        for item in itens:
            if item.id == id:
                item.nome = nome
                item.categoria = categoria
                item.descricao = descricao
                item.preco = float(preco)
                self._salvar(itens)
                return item
        return None

    def excluir(self, id):
        itens = self._carregar()
        restantes = [i for i in itens if i.id != id]
        if len(restantes) == len(itens):
            return False
        self._salvar(restantes)
        return True
