from app.controllers.datarecord import DataRecord
from bottle import template, redirect, request, response, app, Bottle 
import logging
logging.basicConfig(level=logging.DEBUG)

class Application():
    def __init__(self):
        self.pages = {
            'pagina': self.pagina,
            'login': self.login,
            'AmigosFur': self.AmigosFur,
            'cadastropet': self.cadastropet,
            'gatos': self.gatos,
            'cachorros': self.cachorros,
            'roedores': self.roedores,
            'exoticos': self.exoticos,
            'meg': self.meg,
            'fred': self.fred,
            'ruivoemadona': self.ruivoemadona,
            'amora': self.amora,
            'perfil': self.perfil,
            'editperfil':self.editperfil,
            'About_us': self.About_us,
            'petsinform': self.petsinform
            }
        
        self.__model = DataRecord(
            user_file_path='app/controllers/db/users.json',
            pet_file_path='app/controllers/db/cadastropet.json'
        )
        self.__current_username = None
        self.app = Bottle()
        self.app.config['secret_key']= 'bananasdepijama2024'

    

    def render(self, page, parameter=None):
        content = self.pages.get(page, self.helper)
        if not parameter:
            return content()
        else:
            return content(parameter)
        
#---------------------------------------------------------------------------------
 #NÃO MEXER       
    def render_with_kwargs(self, page, **kwargs):
        content = self.pages.get(page, self.helper)
        return content(**kwargs)
#---------------------------------------------------------------------------------

    def get_session_id(self):
        return request.get_cookie('session_id')

    def helper(self):
        return template('app/views/html/helper')
    
    def AmigosFur(self):
        return template('app/views/html/AmigosFur')
    
    def gatos(self):
        return template('app/views/html/gatos/gatos')
    
    def About_us(self):
        return template('app/views/html/About-us')
    def amora(self):
        return template('app/views/html/gatos/amora')
    
    def cachorros(self):
        return template('app/views/html/cachorros/cachorros')
    
    def meg(self):
        return template('app/views/html/cachorros/meg')
    
    def exoticos(self):
        return template('app/views/html/exoticos/exoticos')
    
    def fred(self):
        return template('app/views/html/exoticos/fred')
    
    def roedores(self):
        return template('app/views/html/roedores/roedores')
    
    def ruivoemadona(self):
        return template('app/views/html/roedores/ruivoemadona')

    def login(self, error_message=None):
        return template('app/views/html/login', error_message=error_message)
    
    #def pagina(self, parameter=None, **kwargs):
        username = kwargs.get('username')
        
        if parameter:
            session_id = self.get_session_id()  # Obtém o session_id atual
            user = self.__model.getCurrentUser(session_id)  # Obtém os dados do usuário logado com base no session_id

            if user: 
                transfered = True
                data = {
                'username': user['username'],  # Usa o nome de usuário do objeto retornado
                'password': user['password']
                }
            else:
                transfered = False
                data = None
        else:
            transfered = False
            data = None
    
    
        return template('app/views/html/pagina', transfered=transfered, data=data, username=username)
    
    #def pagina(self, username):
        session_id = self.get_session_id()
        user = self.__model.getCurrentUser(session_id)
        if user:
            return template('app/views/html/pagina.tpl', username=user['username'])
        else:
            return template('app/views/html/pagina.tpl', username=username)
        
    def pagina(self, username=None, error_message=None):
        session_id = self.get_session_id()
        user = self.__model.getCurrentUser(session_id)
    
        if user:
            data = {
            'username': user['username'], 
            'password': user['password']
            }
            transfered = True
        else:
            data = None
            transfered = False
    
        return template('app/views/html/pagina', transfered=transfered, data=data, username=username, error_message=error_message)


    def is_authenticated(self, username):
        session_id = self.get_session_id()
        user = self.__model.getCurrentUser(session_id)
        return username == self.__current_username
    
    def cadastropet(self, username):
        if request.method == 'POST':
            pet_data = {
                "nome": request.forms.get('name'),
                "tipo": request.forms.get('pet_type'),
                "raça": request.forms.get('pet_breed'),
                "idade": request.forms.get('pet_age'),
                "descrição": request.forms.get('pet_description'),
                "responsável": request.forms.get('name'),  # O nome do responsável pode ser o mesmo do dono do login, ajuste conforme necessário
                "celular": request.forms.get('number'),
                "gênero": request.forms.get('gender')
        }
            self.__model.add_pet(pet_data)
            return redirect(f'/pagina/{username}')
    
        return template('app/views/html/cadastropet', username=username)
    
 #---------------------------------------------------------------------------------   
#NÃO MEXER
    def authenticate_user(self, username, password):
        user = self.__model.get_user(username)
        if user and user['password'] == self.__model.hash_password(password):
            session_id = self.__model.create_session(user)
            self.__current_username = user['username']
            return session_id, user['username']
        return None, None


#---------------------------------------------------------------------------------

    def logout_user(self):
        self.__current_username = None
        session_id = self.get_session_id()
        if session_id:
            self.__model.remove_session(session_id)
            response.delete_cookie('session_id')

#---------------------------------------------------------------------------------   
#NÃO MEXER
    def add_user(self, username, email, password):
        return self.__model.add_user(username, email, password)
#--------------------------------------------------------------------------------

    def add_pet(self, pet_data):
        data = self.__model._read_pet_data()
        pet_entry = {
            'name': pet_data.get('name'),
            'type': pet_data.get('pet_type'),
            'breed': pet_data.get('pet_breed'),
            'age': pet_data.get('pet_age'),
            'description': pet_data.get('pet_description'),
            'responsible': pet_data.get('responsible'),
            'cellphone': pet_data.get('number'),
            'gender': pet_data.get('gender')
    }

        data['pets'].append(pet_entry)
        self.__model._write_pet_data(data)
        return True
#--------------------------------------------------------------------------------
#Perfil
    def perfil(self):
        user = None
        if self.__current_username:
            user = self.__model.get_user(self.__current_username)
        if user:
            return template('app/views/html/perfil.tpl', user=user)
        return redirect('/login')

    def logout_user(self):
        self.__current_username = None
        session_id = self.get_session_id()
        if session_id:
            self.__model.remove_session(session_id)
            response.delete_cookie('session_id')
#--------------------------------------------------------------------------------
#Editar perfil
    def editperfil(self, username):
        user = self.__model.get_user(username)

        if request.method == 'POST':
            new_username = request.forms.get('username')
            new_email = request.forms.get('email')
            new_password = request.forms.get('password')
            updated_data = {
                "username": new_username,
                "email": new_email,
                "password": new_password  # Apenas a senha deve ser atualizada
            }
            self.__model.update_user(username, updated_data)
            return redirect(f'/pagina/{new_username}')

        if user:
            return template('app/views/html/editperfil', user=user)
        else:
            return redirect('/login')
#--------------------------------------------------------------------------------
#EXCLUIR PERFIL


    def delete_user_profile(self):
        session_id = request.get_cookie('session_id', secret=self.app.config['secret_key'])
        if not session_id:
            return self.render_with_kwargs('login', error_message='Por favor, faça login para excluir seu perfil.')

        # Busca o usuário com base na sessão e remove
        user = self.__model.getCurrentUser(session_id)
        if user and self.__model.delete_user(user['username']):
            response.delete_cookie('session_id')  # Remove o cookie da sessão
            return redirect('/login')
        return self.render_with_kwargs('pagina', error_message='Erro ao excluir o perfil.')
    
    def helper(self):
        return template('app/views/html/About-us')
    
    def petsinform(self):
        pets = self.__model.get_pets()  # Obtém a lista de pets do modelo
        return template('app/views/html/petsinform', pets=pets)  # Passa a lista de pets para o template

    def remove_session(self, session_id):
        data = self.__model._read_data()
        for user in data['users']:
            if user.get('session_id') == session_id:
                user['session_id'] = None  # Remove a sessão do usuário
                break
        self.__model._write_data(data)  # Salva as alterações de volta no arquivo

