from bottle import Bottle, run, template, static_file
import os

app = Bottle()

# Caminho absoluto até a pasta views
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIEWS_DIR = os.path.join(BASE_DIR, 'app', 'views')

# Rota de arquivos estáticos (CSS e JS)
@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=VIEWS_DIR)

# Página principal — usando lookup (forma correta)
@app.route('/')
def index():
    return template('index.tpl', lookup=[VIEWS_DIR])

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
