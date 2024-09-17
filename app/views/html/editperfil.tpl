<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="/static/css/editperfil.css">
    <title>Editar Perfil</title>
</head>
<body>
    <div class="container">
        <div class="form-image">
            <img src="/static/img/undraw_reminder_re_fe15.svg" alt="Imagem de Pet">
        </div>
        <div class="form">
            <div class="login-button">
                <a href="/pagina/{{ user['username'] }}">
                    <button>Voltar</button>
                </a>
            </div>

            <form action="/editperfil/{{ user['username'] }}" method="POST">
                <div class="form-header">
                    <div class="title">
                        <h1>Editar Perfil</h1>
                    </div>
                </div>

                <div class="input-box">
                    <label for="username">Novo Nome de Usuário</label>
                    <input id="username" type="text" name="username" value="{{ user['username'] }}" placeholder="Digite o novo nome de usuário" required>
                </div>

                <div class="input-box">
                    <label for="email">Novo Email</label>
                    <input id="email" type="email" name="email" value="{{ user['email'] }}" placeholder="Digite o novo email" required>
                </div>

                <div class="input-box">
                    <label for="password">Nova Senha</label>
                    <input id="password" type="password" name="password" placeholder="Digite a nova senha" required>
                </div>

                <div class="enviar-button">
                    <button type="submit">Enviar</button>
                </div>
            </form>
        </div>
    </div>
</body>
</html>
