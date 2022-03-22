from flask import Flask, jsonify, render_template, request

application = Flask(__name__)


@application.get("/wallet")
def wallet_connect():
    """Wallet Connect page."""

    address = request.args.get("recipientAddress")
    amount = request.args.get("amountToSend")
    request_type = request.args.get("requestType")
    txn_method = request.args.get("txnMethod")
    device_type = request.args.get("deviceType")

    return render_template(
        "wallet_connect.html",
        address=address,
        amount=amount,
        request_type=request_type,
        txn_method=txn_method,
        device_type=device_type,
    )


@application.get("/")
def index():
    return jsonify({"status": 1, "message": "Welcome to DeCHO"})
