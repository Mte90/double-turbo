DRF_STRIPE = {
    "STRIPE_API_SECRET": environ.get("STRIPE_API_SECRET", ""),
    "STRIPE_WEBHOOK_SECRET": "my_stripe_webhook_key",
    "FRONT_END_BASE_URL": "http://localhost:3000",
    "DJANGO_USER_MODEL": "api.User"
    "NEW_USER_FREE_TRIAL_DAYS": 30,
    #"BILLING_ACCOUNT_MODEL": "api.company",
    "DEFAULT_MAX_SUBSCRIPTION_QUANTITY": 9999,
    "CHECKOUT_SUCCESS_URL_PATH": "admin/api/user/payments/",
    "CUSTOMER_PORTAL_RETURN_URL_PATH": "admin/api/user/payments/",
}
if DEBUG:
    DRF_STRIPE["FRONT_END_BASE_URL"] = "http://localhost:8000"
STRIPE_API_PUBLIC = environ.get("STRIPE_API_PUBLIC", "")
STRIPE_DEFAULT_PRICE_ID = environ.get("STRIPE_DEFAULT_PRICE_ID", "")

