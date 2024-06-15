import paypalrestsdk
import logging

paypalrestsdk.configure({
    "mode": "sandbox",
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET"
})

logging.basicConfig(level=logging.INFO)
