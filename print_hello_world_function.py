import os

secret = os.environ.get("MY_SECRET", "NO_SECRET_FOUND")

print("Hello, world!")
print(f"My secret is: {secret}")