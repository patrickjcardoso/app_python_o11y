from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__, static_url_path='/static')

# Conecte-se ao servidor do MongoDB
client = MongoClient('mongodb://localhost:27017')

# Acesse o banco de dados
db = client['taskmaster']

# Acesse a coleção (tabela) de tarefas
tasks_collection = db['tasks']

@app.route('/')
def index():
    # Obtenha todas as tarefas da coleção
    tasks = tasks_collection.find()
    return render_template('index.html', tasks=tasks)

@app.route('/create_task', methods=['POST'])
def create_task():
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = request.form.get('due_date')

    # Insira a nova tarefa na coleção
    task = {'title': title, 'description': description, 'due_date': due_date}
    tasks_collection.insert_one(task)

    return redirect('/')

@app.route('/edit_task/<string:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    # Verifique se a tarefa existe na coleção
    task = tasks_collection.find_one({'_id': task_id})
    if task:
        if request.method == 'POST':
            title = request.form.get('title')
            description = request.form.get('description')
            due_date = request.form.get('due_date')

            # Atualize a tarefa na coleção
            tasks_collection.update_one({'_id': task_id}, {'$set': {'title': title, 'description': description, 'due_date': due_date}})

            return redirect('/')

        return render_template('edit_task.html', task=task, task_id=task_id)

    return redirect('/')

@app.route('/delete_task/<string:task_id>', methods=['GET'])
def delete_task(task_id):
    # Remova a tarefa da coleção
    tasks_collection.delete_one({'_id': task_id})

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
