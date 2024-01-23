import logging
import os

import redis

logging.basicConfig(level=logging.INFO, format="")
logger = logging.getLogger(__package__)

r = redis.Redis(
        host=os.environ["REDIS_STUDY_HOST"],
        port=int(os.environ["REDIS_STUDY_PORT"]),
        password=os.environ["REDIS_STUDY_PASSWORD"],
        decode_responses=True,
        ssl=False,
)

logger.info(r)
logger.info(r.ping())

logger.info(r.set("foo", "bar"))
logger.info(r.get("foo"))

logger.info(r.hset(
    "user-session:123",
    mapping={
        "name": "John",
        "surname": "Smith",
        "company": "Redis",
        "age": 29,
    },
))
logger.info(r.hget("user-session:123", "name"))
logger.info(r.hgetall("user-session:123"))
r.close()

