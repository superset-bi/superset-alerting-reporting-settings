SCREENSHOT_LOCATE_WAIT = 100
SCREENSHOT_LOAD_WAIT = 600

# Slack configuration
SLACK_API_TOKEN = "xoxb-"

# Email configuration
SMTP_HOST = "smtp.yandex.ru" # change to your host
SMTP_PORT = 587 # your port, e.g. 587
SMTP_STARTTLS = True
SMTP_SSL_SERVER_AUTH = True # If your using an SMTP server with a valid certificate
SMTP_SSL = False
SMTP_USER = "your-email-username@yandex.com" # use the empty string "" if using an unauthenticated SMTP server
SMTP_PASSWORD = "your_password_qwerty123" # use the empty string "" if using an unauthenticated SMTP server
SMTP_MAIL_FROM = "your-email-username@yandex.com"
EMAIL_REPORTS_SUBJECT_PREFIX = "[Report] superset-bi.ru" # optional - overwrites default value in config.py of "[Report] "

# WebDriver configuration
# If you use Firefox, you can stick with default values
# If you use Chrome, then add the following WEBDRIVER_TYPE and WEBDRIVER_OPTION_ARGS
WEBDRIVER_TYPE = "chrome"
WEBDRIVER_OPTION_ARGS = [
    "--force-device-scale-factor=2.0",
    "--high-dpi-support=2.0",
    "--headless",
    "--disable-gpu",
    "--disable-dev-shm-usage",
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-extensions",
]