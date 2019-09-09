from flask import Flask
import redis

app = Flask(__name__)

class RedisClient:
    pool = redis.ConnectionPool(host='redis', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)
    
    @classmethod
    def SETNX(cls, key, value):
        return cls.r.setnx(key, value)
    
    @classmethod
    def SET(cls, key, value):
        return cls.r.set(key, value)

    @classmethod
    def EXPIRE(cls, key, time):
        return cls.r.expire(key, time)

    @classmethod
    def DEL(cls, key):
        return cls.r.delete(key)



@app.route('/')
def hello():
    
    name = RedisClient.SETNX('kaori', 'True')
    if name == 0:
        return "No"
    else:
        RedisClient.EXPIRE('kaori', 30)
        return "True"



if __name__ == "__main___":
    app.run()