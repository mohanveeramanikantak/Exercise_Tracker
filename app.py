from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__, template_folder='templates')

# In-memory database (for simplicity)
expenses = []
next_id = 1

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses, total_expenditure=calculate_total_expenditure())

@app.route('/add-expense', methods=['POST'])
def add_expense():
    global next_id
    description = request.form['description']
    amount = float(request.form['amount'])
    date = request.form['date']
    
    expense = {
        'id': next_id,
        'description': description,
        'amount': amount,
        'date': date
    }
    expenses.append(expense)
    next_id += 1
    
    return redirect(url_for('index'))

@app.route('/delete-expense/<int:expense_id>')
def delete_expense(expense_id):
    global expenses
    expenses = [expense for expense in expenses if expense['id'] != expense_id]
    return redirect(url_for('index'))

@app.route('/total-expenditure')
def total_expenditure():
    total = calculate_total_expenditure()
    return jsonify({'total': total})

def calculate_total_expenditure():
    return sum(expense['amount'] for expense in expenses)

if __name__ == '__main__':
    app.run(debug=True)
