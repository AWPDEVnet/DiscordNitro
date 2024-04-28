import requests
import random
import string

# Function to generate a random alphanumeric string of a specified length
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Prompt the user for the Discord webhook URL
webhook_url = input("Please enter your Discord webhook URL: ")

# Validate the webhook URL
if not webhook_url.startswith("https://discord.com/api/webhooks/"):
    raise ValueError("Invalid Discord webhook URL.")

prefix = "discord.gift/"

# Function to send a message to the Discord webhook
def send_to_discord(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:  # 204 is "No Content," indicating success
        raise Exception(f"Failed to send message to Discord. Status code: {response.status_code}")

# Generate strings indefinitely and send them to the Discord webhook
while True:
    random_string = generate_random_string(16)
    full_string = prefix + random_string
    send_to_discord(webhook_url, full_string)
    print(f"Sent to Discord: {full_string}")
