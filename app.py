from flask import Flask, jsonify, render_template, request

application = Flask(__name__)


@application.get("/wallet")
def wallet_connect():
    """Wallet Connect page."""

    address = request.args.get("recipientAddress")
    amount = request.args.get("amountToSend")
    txn_type = request.args.get("txnType")
    txn_method = request.args.get("txnMethod")

    return render_template(
        "wallet_connect.html",
        address=address,
        amount=amount,
        txn_type=txn_type,
        txn_method=txn_method,
    )


@application.get("/")
def index():
    return jsonify({"status": 1, "message": "Welcome to DeCHO"})
