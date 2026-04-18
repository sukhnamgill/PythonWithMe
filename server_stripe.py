from flask import Flask, request, jsonify
import stripe
import os

app = Flask(__name__)

# 🔐 Set your Stripe Secret Key (use environment variable in production)
stripe.api_key = "sk_test_51TK9JUDRSMHDC52aIEXkvUcvAzpMR2jwH4gfoBAT5MJBBgqX7n0uUxUDkkehC8V7KdL93pwrAnjir5FqeFWCUBop00RDGILchE"

@app.route("/")
def home():
    return "Stripe Backend Running ✅"

# ✅ Create PaymentIntent
@app.route("/create-payment-intent", methods=["POST"])
def create_payment_intent():
    try:
        data = request.get_json()

        amount = data.get("amount")  # in cents (e.g., 1000 = $10)
        currency = data.get("currency", "usd")

        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            automatic_payment_methods={
                "enabled": True
            }
        )

        return jsonify({
            "clientSecret": intent.client_secret
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ✅ Webhook (VERY IMPORTANT for production)
@app.route("/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")
    endpoint_secret = "whsec_XXXXXXXXXXXXXXXX"

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    # 🎯 Handle events
    if event["type"] == "payment_intent.succeeded":
        intent = event["data"]["object"]
        print("✅ Payment successful:", intent["id"])

    elif event["type"] == "payment_intent.payment_failed":
        print("❌ Payment failed")

    return jsonify({"status": "success"})

if __name__ == "__main__":
    # ⚠️ Important for local + network access
    app.run(host="0.0.0.0", port=4242)