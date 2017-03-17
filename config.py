import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
#SECRET_KEY 配置仅仅当 CSRF 激活的时候才需要，它是用来建立一个加密的令牌，用于验证一个表单。当你编写自己的应用程序的时候，请务必设置很难被猜测到密钥。既然我们有了配置文件，我们需要告诉 Flask 去读取以及使用它。我们可以在 Flask 应用程序对象被创建后去做
SECRET_KEY = 'you-will-never-guess'


#为了让用户更方便地使用这些常用的 OpenID 登录到我们的网站，我们把它们的链接转成短名称，用户不必手动地输入这些 OpenID。我首先开始定义一个 OpenID 提供者的列表。我们可以把它们写入我们的配置文件中(文件 config ):
#登录视图函数中使用它们
#在登录模板中渲染这些提供商的链接
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
    
#sqlite 数据库是小型应用的最方便的选择，每一个数据库都是存储在单个文件里
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')