from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)

"""我们添加了一个 Post 类，这是用来表示用户编写的 blog。在 Post 类中的 user_id 字段初始化成外键，因此 Flask-SQLAlchemy 知道这个字段是连接到用户上。
值得注意的是我们已经在 User 类中添加一个新的字段称为 posts，它是被构建成一个 db.relationship 字段。这并不是一个实际的数据库字段，因此是不会出现在上面的图中。对于一个一对多的关系，db.relationship 字段通常是定义在“一”这一边。在这种关系下，我们得到一个 user.posts 成员，它给出一个用户所有的 blog"""
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)