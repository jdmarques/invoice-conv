from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/invoices", methods=["POST"])
def invoice_post():
    return jsonify({"message": "Invoice received"})


@app.route("/invoices", methods=["GET"])
def invoice_get():
    return jsonify({"message": "Invoice received"})


if __name__ == "__main__":
    app.run(debug=True)
