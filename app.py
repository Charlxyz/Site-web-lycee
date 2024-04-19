from flask import Flask, render_template

app = Flask(__name__, template_folder='./flaskr/templates', static_folder='./flaskr/static')

@app.route('/')
@app.route('/accueil')
def start():
    return render_template("page1.html")

@app.route('/learn-more')
def page2():
    return render_template("page2.html")

@app.route('/product-Home')
def  product_home():
    return render_template('product-page.html') 

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route("/404")
def page_404():
    return render_template('404.html')

@app.errorhandler(404)
def page_not_found(e):
    return page_404()

app.run(debug=True, host='0.0.0.0', port=8001)