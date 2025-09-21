from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar las tareas en memoria
tareas = ["Aprender Python", "Crear un entregable", "Practicar Flask"]


@app.route('/')
def index():
    """Muestra la lista de todas las tareas."""
    return render_template('index.html', tareas=tareas)


@app.route('/agregar', methods=['POST'])
def agregar_tarea():
    """Agrega una nueva tarea a la lista."""
    nueva_tarea = request.form.get('tarea')
    if nueva_tarea:
        tareas.append(nueva_tarea)
    return redirect(url_for('index'))


@app.route('/eliminar/<int:indice>')
def eliminar_tarea(indice):
    """Elimina una tarea específica de la lista por su índice."""
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
    return redirect(url_for('index'))


@app.route('/editar/<int:indice>', methods=['GET', 'POST'])
def editar_tarea(indice):
    """Permite editar una tarea existente."""
    if request.method == 'POST':
        tarea_editada = request.form.get('tarea_editada')
        if tarea_editada and 0 <= indice < len(tareas):
            tareas[indice] = tarea_editada
        return redirect(url_for('index'))
    else:
        # Muestra el formulario para editar la tarea
        if 0 <= indice < len(tareas):
            return render_template('editar.html',
                                   tarea=tareas[indice],
                                   indice=indice)
        else:
            return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)