from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Datos de ejemplo para los productos de PC
productos_pc = [
    {"nombre": "Cafe", "precio": 20.00},
    {"nombre": "Coca", "precio": 15},
    {"nombre": "Doritos", "precio": 5},
    {"nombre": "Emperador", "precio": 8},
    {"nombre": "Fritos", "precio": 5}
]

# Nombres de gente de Inglaterra
usuarios_inglaterra = [
    {"nombre": "Jose", "apellido": "Smith"},
    {"nombre": "Sara", "apellido": "Bones"},
    {"nombre": "Enrique", "apellido": "Brown"},
    {"nombre": "Ana", "apellido": "Cohen"},
    {"nombre": "James", "apellido": "Wilson"}
]


# Nombres de gente de Suecia
clientes_suecia = [
    {"nombre": "Emma", "apellido": "Flores"},
    {"nombre": "Abby", "apellido": "Borrego"},
    {"nombre": "Ruba", "apellido": "Eduardo"},
    {"nombre": "Sara", "apellido": "Flores"},
    {"nombre": "Alan", "apellido": "Pettersson"}
]

# Ruta para la página de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))  # Redirige a index si ya ha iniciado sesión
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Aquí puedes añadir la lógica para verificar el nombre de usuario y la contraseña
        # Si la autenticación es exitosa, establece el usuario en la sesión y redirige a index
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('login.html')

# Ruta para cerrar sesión
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Ruta para la página principal
@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

# Ruta para mostrar los productos
@app.route('/productos')
def mostrar_productos():
    if 'username' in session:
        return render_template('productos.html', productos=productos_pc)
    return redirect(url_for('login'))

# Ruta para mostrar los usuarios
@app.route('/usuarios')
def mostrar_usuarios():
    if 'username' in session:
        return render_template('usuarios.html', usuarios=usuarios_inglaterra)
    return redirect(url_for('login'))

# Ruta para mostrar los clientes
@app.route('/clientes')
def mostrar_clientes():
    if 'username' in session:
        return render_template('clientes.html', clientes=clientes_suecia)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
