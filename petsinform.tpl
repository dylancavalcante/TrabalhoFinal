<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/style.css"> <!-- Link para o seu CSS -->
    <title>Informações dos Pets para Adoção</title>
</head>
<body>
    <div class="container">
        <h1>Pets Disponíveis para Adoção</h1>
        <div class="pets-list">
            {{#each pets}}
                <div class="pet-card">
                    <h2>{{this.name}}</h2>
                    <p><strong>Tipo:</strong> {{this.type}}</p>
                    <p><strong>Raça:</strong> {{this.breed}}</p>
                    <p><strong>Idade:</strong> {{this.age}} anos</p>
                    <p><strong>Descrição:</strong> {{this.description}}</p>
                    <p><strong>Responsável:</strong> {{this.responsible}}</p>
                    <p><strong>Celular:</strong> {{this.cellphone}}</p>
                    <p><strong>Gênero:</strong> {{this.gender}}</p>
                </div>
            {{/each}}
        </div>
        <a href="/pagina/{{username}}"><button>Voltar</button></a>
    </div>
</body>
</html>
