from app.controllers.application import Application
from app.controllers.datarecord import DataRecord

import json
import os
import hashlib
from typing import Dict, Any

class SuperAdmin:
    def __init__(self, user_file_path, pet_file_path):
        self.user_file_path = user_file_path
        self.pet_file_path = pet_file_path

    def _read_data(self, file_path):
        if not os.path.exists(file_path):
            return {}
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def _write_data(self, file_path, data):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def add_user(self, username, email, password):
        data = self._read_data(self.user_file_path)
        if 'users' not in data:
            data['users'] = []
        if any(user['username'] == username for user in data['users']):
            print("Usuário já existe.")
            return False
        hashed_password = self.hash_password(password)
        data['users'].append({'username': username, 'email': email, 'password': hashed_password})
        self._write_data(self.user_file_path, data)
        print("Usuário adicionado com sucesso.")
        return True

    def remove_user(self, username):
        data = self._read_data(self.user_file_path)
        if 'users' not in data:
            print("Nenhum usuário encontrado.")
            return False
        data['users'] = [user for user in data['users'] if user['username'] != username]
        self._write_data(self.user_file_path, data)
        print("Usuário removido com sucesso.")
        return True

    def add_pet(self, pet_data):
        data = self._read_data(self.pet_file_path)
        if 'pets' not in data:
            data['pets'] = []
        data['pets'].append(pet_data)
        self._write_data(self.pet_file_path, data)
        print("Pet adicionado com sucesso.")

    def remove_pet(self, pet_name):
        data = self._read_data(self.pet_file_path)
        if 'pets' not in data:
            print("Nenhum pet encontrado.")
            return False
        data['pets'] = [pet for pet in data['pets'] if pet['name'] != pet_name]
        self._write_data(self.pet_file_path, data)
        print("Pet removido com sucesso.")
        return True