import pymongo
from pymongo.errors import ConnectionFailure, ConfigurationError, InvalidURI

def check_mongodb_url(url: str):
    try:
        client = pymongo.MongoClient(url, serverSelectionTimeoutMS=3000)
        client.server_info()
        print("[✓] MongoDB URL is valid and connected successfully!")
    except (ConnectionFailure, ConfigurationError, InvalidURI) as e:
        print("[✗] Invalid MongoDB URL or connection failed!")
        print("Error:", e)
    finally:
        try:
            client.close()
        except:
            pass

def main():
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("MongoDB URL Validator")
    print("Made by Syntax Development | https://discord.gg/vMTDMVYE74")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    mongo_url = input("Enter your MongoDB URL to check: ").strip()
    check_mongodb_url(mongo_url)