import os

import redis


PORT = 6379
HOST = os.getenv("HOST", "localhost")


def main():
    client = redis.Redis(host=HOST, port=PORT)
    client.set("key1", "abc")
    value = client.get("key1")
    print(value)


if __name__ == "__main__":
    main()
