from flask import Flask, render_template, request, redirect, flash, session
import os

app = Flask(__name__)
app.secret_key='secret_key'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def new_user():
    return redirect('/')

@app.route('/result', methods=["POST"])
def result():
    if len(request.form['name']) < 1:
        flash('Please fill in your name')
        return redirect('/')
    elif len(request.form['message']) < 1:
        flash('Please type a comment')
        return redirect('/')
    return render_template("result.html", name = request.form["name"], location=request.form['location'], lan=request.form['language'], message=request.form['message'])

if __name__ == "__main__":
    app.run(debug=True)