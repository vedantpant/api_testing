from flask import Flask, jsonify, request

app = Flask(__name__)

posts = [
    {"id": 1, "title": "Hello World"},
    {"id": 2, "title": "Testing with Flask"},
]

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts), 200

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post:
        return jsonify(post), 200
    return jsonify({"error": "Post not found"}), 404

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Missing title"}), 400
    new_post = {
        "id": len(posts) + 1,
        "title": data["title"]
    }
    posts.append(new_post)
    return jsonify(new_post), 201


if __name__ == '__main__':
    app.run(debug=True)
