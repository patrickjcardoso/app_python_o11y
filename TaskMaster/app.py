from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_url_path='/static')

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/create_task', methods=['POST'])
def create_task():
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = request.form.get('due_date')

    task = {'title': title, 'description': description, 'due_date': due_date}
    tasks.append(task)

    return redirect('/')

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    # Subtrai 1 do ID da tarefa para obter o índice correto na lista
    task_index = task_id - 1

    # Verifica se o índice está dentro dos limites da lista de tarefas
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]

        if request.method == 'POST':
            title = request.form.get('title')
            description = request.form.get('description')
            due_date = request.form.get('due_date')

            task['title'] = title
            task['description'] = description
            task['due_date'] = due_date

            return redirect('/')

        return render_template('edit_task.html', task=task, task_id=task_id)

    return redirect('/')

@app.route('/delete_task/<int:task_id>', methods=['GET'])
def delete_task(task_id):
    # Subtrai 1 do ID da tarefa para obter o índice correto na lista
    task_index = task_id - 1

    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

