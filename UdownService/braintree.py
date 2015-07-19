import braintree
import django
braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="5rkq7p4h66b848hz",
                                  public_key="txp62v4fqh966gcb",
                                  private_key="bf94f5f34c699735666b79af0ea85dd0")

@app.route("/client_token", methods=["GET"]) 

def client_token():
    return braintree.ClientToken.generate()

@app.route("/payment-methods", methods=["POST"])
def create_purchase():
    nonce = request.form["payment_method_nonce"]

result = braintree.Transaction.sale({
    "amount": "10.00",
    "payment_method_nonce": nonce_from_the_client
})