from flask import Flask, request, jsonify
from datetime import datetime
from token_bucket import TokenBucket

app = Flask(__name__)
buckets = {}

@app.before_request
def rate_limit():
    user = request.headers.get("X-User", "anonymous")

    if user not in buckets:
        buckets[user] = TokenBucket(
            capacity=10,
            refill_rate=1.0,
            tokens=10,
            last_refill=datetime.utcnow()
        )

    bucket = buckets[user]
    allowed = bucket.allow(datetime.utcnow())

    if not allowed:
        return jsonify({"error": "Rate limit exceeded"}), 429

@app.get("/hello")
def hello():
    return jsonify({"message": "Hello!"})

if __name__ == "__main__":
    app.run(debug=True)