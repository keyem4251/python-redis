import os

import redis


PORT = 6379
HOST = os.getenv("HOST", "localhost")


def main():
    r = redis.Redis(host=HOST, port=PORT)
    with r.pipeline() as pipe:
        pipe.set("key1", "abc")
        pipe.hmset("product_1", {
            "color": "green",
            "price": 100,
        })


if __name__ == "__main__":
    main()
