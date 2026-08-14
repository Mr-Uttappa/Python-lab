from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    products = [
        {"name": "Product 1", "price": "$10", "image": "https://via.placeholder.com/200x150"},
        {"name": "Product 2", "price": "$15", "image": "https://via.placeholder.com/200x150"},
        {"name": "Product 3", "price": "$20", "image": "https://via.placeholder.com/200x150"},
    ]
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
