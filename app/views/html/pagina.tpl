<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal</title>
    <style>
        body {
            font-family: 'Montserrat', sans-serif;
            background: #fff;
            text-align: center;
            color: darkorange;
            padding: 0;
            margin: 0;
        }

        .box {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: rgba(255, 165, 0, 0.6);
            padding: 50px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        a, .button {
            display: block;
            text-decoration: none;
            color: black;
            border: 3px solid darkorange;
            border-radius: 25px;
            padding: 15px;
            margin: 10px 0;
            background-color: #fff;
            transition: background-color 0.3s, color 0.3s;
        }

        a:hover, .button:hover {
            background-color: darkorange;
            color: #fff;
        }

        .button {
            cursor: pointer;
            text-align: center;
            display: inline-block;
        }
    </style>
</head>
<body>
    <br>
    <br>
    <br>
    <h1>Bem-vindo(a) ao AmigosFur!</h1>
    <div class="box">
        <a href="/perfil">Visualizar Perfil</a>
        <a href="/editperfil/{{username}}">Editar Perfil</a>
        <a href="/cadastropet/{{username}}">Cadastrar Pet para Adoção</a>
        <a class="button" href="/logout">Sair</a>
        <form action="/delete_user_profile" method="POST" style="display:inline;">
    </div>
</body>
</html>