from flask import Flask, render_template, request, url_for, redirect
from database import get_all_posts, _save_to_database
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

posts = get_all_posts()
# posts = {
#     1: {'id': 1,
#         'title': "First Post",
#         'content': "Hello. My name is Shreyash. I am writing a Flask Web-application that uses a SQLite database"
#     }
# }


@app.route('/')
def home():
    posts = get_all_posts()
    return render_template('home.html', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    posts = get_all_posts()
    post = posts.get(post_id)
    if not post:
        return render_template('404.html', message=f"A post with id: {post_id} is not found")
    return render_template('post.html', post=post)


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        # title = request.args.get('title')      # works with GET method
        # content = request.args.get('content')
        posts = get_all_posts()
        title = request.form.get("title")   # Works with POST method
        content = request.form.get("content")
        post_id = len(posts) + 1
        post = {'id': post_id, 'title': title, 'content': content}
        _save_to_database(post)
        return redirect(url_for('post', post_id=post_id))
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)

