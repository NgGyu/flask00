u = User.query.get(1)
p = Post(body='my first post!', author=u)
db.session.add(p)
db.session.commit()

u.posts.all()
posts = Post.query.all()
for p in posts:
    print(p.id, p.author.username, p.body)
User.query.order_by(User.username.desc()).all()