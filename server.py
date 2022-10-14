from flask import Flask  
app = Flask(__name__)   
@app.route('/')          
def hello_world():
    return 'Hello World!'  


@app.route('/say/<name>')
def say(name):
    return f'Hello {name}'

@app.route('/repeat/<int:num>/<name>')
def repeat(num, name):
    return f'{name * num}'

if __name__=="__main__":   
    app.run(debug=True)    

