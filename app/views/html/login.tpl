<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Junte-se ao AmigosFur!</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="/static/css/login.css">
</head>
<body>
    <div class="container" id="container">

        <!-- Mensagem de erro -->
        {% if error_message %}
            <div class="error-message">
                <p>{{ error_message }}</p>
            </div>
        {% endif %}

        <div class="form-container sign-up-container">
            <form action="/signup" method="POST">
                <h1>Crie uma conta</h1>
                <div class="social-container">
                    <a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
                    <a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
                    <a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
                </div>
                <span>Ou use seu email para registro</span>
                <input type="text" name="username" placeholder="Email ou Username" required />
                <input type="email" name="email" placeholder="Email" required />
                <input type="password" name="password" placeholder="Password" required />
                <button type="submit">Sign Up</button>
            </form>
        </div>
        <div class="form-container sign-in-container">
            <form action="/login" method="POST">
                <h1>Conecte-se!</h1>
                <div class="social-container">
                    <a href="#" class="social"><i class="fab fa-facebook-f"></i></a>
                    <a href="#" class="social"><i class="fab fa-google-plus-g"></i></a>
                    <a href="#" class="social"><i class="fab fa-linkedin-in"></i></a>
                </div>
                <span>ou use sua conta!</span>
                <input type="email" name="username" placeholder="Email" required />
                <input type="password" name="password" placeholder="Password" required />
                <a href="#">Esqueceu a senha?</a>
                <button type="submit">Conecte-se</button>
            </form>
        </div>
        <div class="overlay-container">
            <div class="overlay">
                <div class="overlay-panel overlay-left">
                    <h1>Bem vindo de volta!</h1>
                    <p>Para se conectar use suas informações já cadastradas</p>
                    <button class="ghost" id="signIn">CONECTE-SE</button>
                </div>
                <div class="overlay-panel overlay-right">
                    <h1>Prazer em te conhecer!</h1>
                    <p>Cadastre-se e comece uma nova jornada conosco</p>
                    <button class="ghost" id="signUp">CADASTRE-SE</button>
                </div>
            </div>
        </div>
    </div>

    <footer>
    <script src="/static/js/login.js"></script>
</body>
</html>