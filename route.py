from bottle import Bottle, run, static_file, request
from app.controllers.application import Application

app = Bottle()
ctl = Application()


# ---------- Arquivos estáticos (CSS e JS) ----------

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')


# ---------- READ: listagem do cardápio ----------

@app.get('/')
@app.get('/cardapio')
def cardapio():
    return ctl.listar(request.query.get('msg'))


# ---------- CREATE: novo item ----------

@app.get('/itens/novo')
def novo_item_form():
    return ctl.formulario_novo()


@app.post('/itens/novo')
def novo_item_salvar():
    return ctl.criar(request.forms)


# ---------- UPDATE: editar item ----------

@app.get('/itens/<id:int>/editar')
def editar_item_form(id):
    return ctl.formulario_editar(id)


@app.post('/itens/<id:int>/editar')
def editar_item_salvar(id):
    return ctl.atualizar(id, request.forms)


# ---------- DELETE: excluir item ----------

@app.post('/itens/<id:int>/excluir')
def excluir_item(id):
    return ctl.excluir(id)


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
