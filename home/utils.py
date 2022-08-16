from http import client
import moncashify

def moncashPayment(id,money):
    client_id='5963fcd6da676836aa985d13ee53bef7'
    secret_key='oHrr4tbnB1PH0uz6VQNUvbvyBM0aiLPgBxVs22tJEj22zoHrURKFvjBykwveAFIr'
    moncash=moncashify.API(client_id, secret_key, debug=True)
    payment = moncash.payment(id, money)
    url=payment.get_redirect_url()
    return url