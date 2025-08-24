from flask import Flask, render_template

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def index():
    # Renderizar la plantilla index.html
    return render_template('index.html')

# Ruta para la página "Acerca de"
@app.route('/about')
def about():
    # Renderizar la plantilla about.html
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Punto de entrada principal
if __name__ == '__main__':
    # Ejecutar la aplicación en modo debug
    app.run(debug=True)