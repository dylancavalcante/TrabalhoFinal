import json
import hashlib
import uuid

class DataRecord:

#BANCO DE DADOS PESSOAS

    def __init__(self, user_file_path='app/controllers/db/users.json', pet_file_path='app/controllers/db/cadastropet.json'):
        self.user_file_path = user_file_path
        self.pet_file_path = pet_file_path

    def _read_data(self):
        try:
            with open(self.user_file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {"users": []}

    def _write_data(self, data):
        with open(self.user_file_path, 'w') as file:
            json.dump(data, file, indent=4)

#BANCO DE DADOS ANIMAIS

    def _read_pet_data(self):
        try:
            with open(self.pet_file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {'pets': []}
        except json.JSONDecodeError:
            return {'pets': []}

    def _write_pet_data(self, data):
        with open(self.pet_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file,ensure_ascii=False, indent=4)

    def add_pet(self, pet_data):
        data = self._read_pet_data()
        data['pets'].append(pet_data)
        self._write_pet_data(data)
        return True  # Adiciona o pet com sucesso

    def get_pets(self):
        return self._read_pet_data().get('pets', [])
#---------------------------------------------------------------------------------
 #NÃO MEXER  
    def getCurrentUser(self, session_id):
        data = self._read_data()
        for user in data['users']:
            if user.get('session_id') == session_id:
                return user
        return None
#---------------------------------------------------------------------------------

    def get_user(self, username_or_email):
        data = self._read_data()
        for user in data['users']:
            # Verifica tanto o username quanto o email
            if user.get('username') == username_or_email or user.get('email') == username_or_email:
                return user
        return None
#---------------------------------------------------------------------------------
 #NÃO MEXER  
    def add_user(self, username, email, password):
        data = self._read_data()
        if self.get_user(username):
            return False  # Usuário já existe
        hashed_password = self.hash_password(password)
        data['users'].append({
            "username": username,
            "email": email,
            "password": hashed_password
        })
        self._write_data(data)
        return True
#---------------------------------------------------------------------------------

    def checkUser(self, username, password):
        user = self.get_user(username)
        if user and user['password'] == self.hash_password(password):
            return True  # Usuário autenticado
        return False  # Falha na autenticação
    
#---------------------------------------------------------------------------------
 #NÃO MEXER  
    def hash_password(self, password):
        # Hash simples usando SHA-256 (para produção, considere usar bcrypt ou outra biblioteca segura)
        return hashlib.sha256(password.encode()).hexdigest()
#---------------------------------------------------------------------------------


    # Novo método para criar uma sessão
    def create_session(self, user):
        session_id = str(uuid.uuid4())
        data = self._read_data()
        for u in data['users']:
            if u['username'] == user['username']:
                u['session_id'] = session_id
                break
        self._write_data(data)
        return session_id

    # Novo método para remover uma sessão
    def remove_session(self, session_id):
        data = self._read_data()
        for user in data['users']:
            if user.get('session_id') == session_id:
                user['session_id'] = None
                break
        self._write_data(data)

#---------------------------------------------------------------------------------
    #Método para atualizar os dados do usuário no JSON
    def update_user(self, username, updated_data):
        data = self._read_data()
        for user in data['users']:
            if user['username'] == username:
                user['username'] = updated_data['username']  # Atualiza o nome de usuário
                user['email'] = updated_data['email']        # Atualiza o email
                user['password'] = self.hash_password(updated_data['password'])  # Atualiza a senha
                break
        self._write_data(data)


    def create_session(self, user):
        session_id = str(uuid.uuid4())
        data = self._read_data()
        for u in data['users']:
            if u['username'] == user['username']:
                u['session_id'] = session_id  # Atualiza o session_id
                break
        self._write_data(data)
        return session_id

    def remove_session(self, session_id):
        data = self._read_data()
        for user in data['users']:
            if user.get('session_id') == session_id:
                user['session_id'] = None
                break
        self._write_data(data)

    def delete_user(self, username):
        data = self._read_data()
        for user in data['users']:
            if user['username'] == username:
                data['users'].remove(user)
                self._write_data(data)
                return True
        return False