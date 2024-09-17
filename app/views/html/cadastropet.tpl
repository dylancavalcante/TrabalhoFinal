<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="/static/css/cadastropet.css">
    <title>Cadastro de Pet</title>
</head>
<body>
    <div class="container">
        <div class="form-image">
            <img src="/static/img/undraw_fish_bowl_uu88.svg" alt="Imagem de Pet">
        </div>
        <div class="form">
            <div class="login-button">
                <a href="/pagina/{{username}}">
                    <button>Voltar</button>
                </a>
            </div>

            <form action="/cadastropet/{{username}}" method="POST">
                <div class="form-header">
                    <div class="title">
                        <h1>Cadastro Pet</h1>
                    </div>
                </div>

                <div class="input-group">
                    <div class="input-box"> 
                        <label for="name">Nome do Pet</label>
                        <input id="name" type="text" name="name" placeholder="Digite o nome do pet (opcional)">
                    </div>

                    <div class="input-box"> 
                        <label for="pet_type">Tipo de pet</label>
                        <select id="pet_type" name="pet_type" required>
                            <option value="dog">Cachorro</option>
                            <option value="cat">Gato</option>
                            <option value="other">Outro</option>
                        </select><br>
                    </div>

                    <div class="input-box"> 
                        <label for="pet_breed">Raça do pet</label>
                        <input id="pet_breed" type="text" name="pet_breed" placeholder="Digite a raça do pet" required>
                    </div>

                    <div class="input-box"> 
                        <label for="pet_age">Idade do pet</label>
                        <input id="pet_age" type="number" name="pet_age" placeholder="Digite a idade do pet">
                    </div>

                    <div class="input-box"> 
                        <label for="pet_description">Descrição do Pet</label>
                        <textarea id="pet_description" name="pet_description" placeholder="Descreva o pet" rows="4" cols="50"></textarea>
                    </div>

                    <div class="input-box"> 
                        <label for="responsible">Nome do Responsável</label>
                        <input id="responsible" type="text" name="responsible" placeholder="Digite o nome do Responsável pela adoção" required>
                    </div>

                    <div class="input-box"> 
                        <label for="number">Celular</label>
                        <input id="number" type="tel" name="number" placeholder="(xx) xxxx-xxxx" required>
                    </div>
                </div>

                <div class="gender-inputs">
                    <div class="gender-title">
                        <h6>Categoria de Gênero do Pet</h6>
                    </div>

                    <div class="gender-input">
                        <input type="radio" id="female" name="gender" value="femea">
                        <label for="female">Fêmea</label>
                    </div>

                    <div class="gender-input">
                        <input type="radio" id="male" name="gender" value="macho">
                        <label for="male">Macho</label>
                    </div>
                </div>

                <div class="enviar-button">
                    <button type="submit">Enviar</button>
                </div>
            </form>
        </div>        
    </div>
</body>
</html>