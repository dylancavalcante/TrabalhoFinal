<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/css/petsinform.css"> 
    <title>Pets para Adoção</title>
</head>
<body>
    <div class="container">
        <h1>Pets Disponíveis para Adoção</h1>
        <div class="pet-list">
            % for pet in pets:
                <div class="pet-card">
                    <h2>{{ pet['name'] }}</h2>
                    <p><strong>Tipo:</strong> {{ pet['type'] }}</p>
                    <p><strong>Raça:</strong> {{ pet['breed'] }}</p>
                    <p><strong>Idade:</strong> {{ pet['age'] }} anos</p>
                    <p><strong>Gênero:</strong> {{ pet['gender'] }}</p>
                    <p><strong>Descrição:</strong> {{ pet['description'] }}</p>
                    <p><strong>Responsável:</strong> {{ pet['responsible'] }}</p>
                    <p><strong>Celular:</strong> {{ pet['cellphone'] }}</p>
                </div>
            % end
        </div>
        <a href="/AmigosFur">Voltar</a>
    </div>
</body>
</html>
