from flask import Flask, render_template, request

application = Flask(__name__)


@application.get("/wallet")
def wallet_connect():
    """Wallet Connect page."""

    address = request.args.get("recipientAddress")
    amount = request.args.get("amountToSend")
    request_type = request.args.get("type")

    return render_template(
        "wallet_connect.html", address=address, amount=amount, request_type=request_type
    )
