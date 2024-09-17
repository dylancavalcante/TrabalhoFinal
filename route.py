from app.controllers.application import Application
from app.controllers.datarecord import DataRecord
from bottle import Bottle, request, static_file, redirect, response, template

app = Bottle()
app.config['secret_key'] = 'bananasdepijama2024'
ctl = Application()
ctl.__model = DataRecord(user_file_path='app/controllers/db/users.json', pet_file_path='app/controllers/db/cadastropet.json')

# -----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

@app.route('/AmigosFur', method='GET')
def AmigosFur():
    return ctl.render('AmigosFur')

@app.route('/About-us', method='GET')
def About_us():
    return ctl.render('app/views/html/About-us')

#ANIMAIS

@app.route('/gatos/gatos', method='GET')
def gatos():
    return ctl.render('gatos')

@app.route('/cachorros/cachorros', method='GET')
def cachorros():
    return ctl.render('cachorros')

@app.route('/roedores/roedores', method='GET')
def roedores():
    return ctl.render('roedores')

@app.route('/exoticos/exoticos', method='GET')
def exoticos():
    return ctl.render('exoticos')

@app.route('/gatos/amora', method='GET')
def amora():
    return ctl.render('amora')

@app.route('/cachorros/meg', method='GET')
def meg():
    return ctl.render('meg')

@app.route('/roedores/ruivoemadona', method='GET')
def ruivoemadona():
    return ctl.render('ruivoemadona')
@app.route('/exoticos/fred', method='GET')
def fred():
    return ctl.render('fred')

# -----------------------------------------------------------------------------
#LOGIN/CADASTRO (NÃO MEXER NAS ROTAS ABAIXO!!!!!!!!!!!)

@app.route('/login', method='GET')
def login():
    return ctl.render('login')

@app.route('/login', method='POST')
def action_login():
    username_or_email = request.forms.get('username')  # Captura o campo de login (pode ser email ou username)
    password = request.forms.get('password')
    session_id, error_message = ctl.authenticate_user(username_or_email, password)
    
    if session_id:
        response.set_cookie('session_id', session_id, httponly=True, secure=False, max_age=3600,  secret=app.config['secret_key'])
        redirect(f'/pagina/{username_or_email}')
    else:
        error_message = 'Nome de usuário ou senha incorretos.'
        return ctl.render_with_kwargs('login', error_message=error_message)

@app.route('/signup', method='POST')
def signup():
    username = request.forms.get('username')
    email = request.forms.get('email')
    password = request.forms.get('password')

    user_added = ctl.add_user(username, email, password)
    if user_added:
        redirect('/login')
    else:
        error_message = 'Usuário já existe.'
        return ctl.render_with_kwargs('login', error_message=error_message)
    
# -----------------------------------------------------------------------------
#PAGINA USUÁRIO APÓS LOGIN

#@app.route('/pagina/<username>', method='GET')
#def pagina(username):
    #return ctl.render_with_kwargs('pagina', username=username)
@app.route('/pagina/<username>', method='GET')
def pagina(username):
    return ctl.pagina(username)


#cadastro de adoação 
@app.route('/cadastropet/<username>', method='GET')
def cadastropet(username):
    return ctl.render('cadastropet', username)

@app.route('/cadastropet/<username>', method='POST')
def action_cadastropet(username):
    pet_data = {
        'name': request.forms.get('name'),
        'pet_type': request.forms.get('pet_type'),
        'pet_breed': request.forms.get('pet_breed'),
        'pet_age': request.forms.get('pet_age'),
        'pet_description': request.forms.get('pet_description'),
        'responsible': request.forms.get('responsible'),
        'number': request.forms.get('number'),
        'gender': request.forms.get('gender')
    }

    
    success = ctl.add_pet(pet_data)
    
    if success:
        redirect(f'/pagina/{username}')
    else:
        error_message = 'Erro ao cadastrar o pet.'
        return ctl.render_with_kwargs('cadastropet', username=username, error_message=error_message)

# -----------------------------------------------------------------------------

#visualização do perfil
@app.route('/perfil', method='GET')
def perfil():
    return ctl.perfil()

@app.route('/logout')
def logout():
    session_id = request.get_cookie('session_id', secret=app.config['secret_key'])
    ctl.remove_session(session_id)
    response.delete_cookie('session_id')
    redirect('/AmigosFur')

#editar perfil
@app.route('/editperfil/<username>', method=['GET', 'POST'])
def editperfil(username):
    return ctl.editperfil(username)

#deletar Usuario
@app.route('/delete_user_profile', method='POST')
def delete_user_profile():
    return ctl.delete_user_profile()

@app.route('/petsinform', method='GET')
def petsinform():
    return ctl.petsinform()
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

