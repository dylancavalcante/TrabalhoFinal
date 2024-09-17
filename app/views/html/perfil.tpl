<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="/static/css/perfil.css">
    <title>Perfil</title>
</head>
<body>
    <div class="container">
        <div class="form">
            <div class="info">
                <div class="form-header">
                    <h1>Perfil</h1>
                </div>

                <div class="text">
                    <label for="name">Nome do Usuário</label>
                    <input id="name" type="text" name="name" value="{{ user['username'] }}" readonly>
                </div>

                <div class="text">
                    <label for="email">Email</label>
                    <input id="email" type="text" name="email" value="{{ user['email'] }}" readonly>
                </div>

                <div class="buttons">
                    <a href="/editperfil/{{ user['username'] }}">
                        <button type="button">Editar Perfil</button>
                    </a>
                    <form action="/delete_user_profile" method="POST" style="display:inline;">
                        <button type="submit" class="button" style="background-color: red; color: white;">Excluir Perfil</button>
                    </form>
                    <a href="/AmigosFur">
                        <button type="button">Voltar à Página Inicial</button>
                    </a>
                </div>
            </div>
        </div>
        <div class="form-image">
            <img src="/static/img/undraw_friends_r511.svg" alt="Imagem de Perfil">
        </div>
    </div>
</body>
</html>