# myflasky

### Turn the virtualenv on
```
source venv/bin/activate
```

### Turn the virtualenv off
```
deactivate
```

### 删除本地标签：
```
git tag -d 标签名
```  

### 删除远程标签：
```
git push origin :refs/tags/标签名
```

### Run server
```
venv/bin/python run.py runserver
```

### 手动创建并初始化数据库的方式

```
venv/bin/python
Python 2.7.10 (default, Oct 18 2015, 19:53:45) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.72)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import db
>>> db.create_all()
```

### 创建数据库migrate操作相关的脚本和目录 
```
venv/bin/python run.py db init
```

### creat and migration database

I should aways clean the folder 'migrations/versions/' before I run the
command below

```
venv/bin/python run.py db migrate -m "initial migration"
```

#### database upgrade. Call this command immeditely after migrating database
```
venv/bin/python run.py db upgrade
```

### 手动测试邮件发送
```
~/iCodeSpace/Project/myflasky 
$venv/bin/python run.py shell
>>> from flask.ext.mail import Message
>>> from app import mail
>>> msg = Message('test subject', sender='info@gracegene.com', recipients=['huangshujia@gracegene.com'])
>>> msg.body = 'text body'
>>> msg.html = '<b>HTML</b> body'
>>> with app.app_context():
...     mail.send(msg)
... 
>>>
``` 

### 单元测试
```
venv/bin/python run.py test
```

### 添加用户，以便测试用户登录
```
$venv/bin/python run.py shell

>>> u = User(email="john@example.com", username='john', password='cat')
>>> db.session.add(u)
>>> db.session.commit()
>>>
```
现在就可以用`john@example.com` 和密码`cat`登录进去了。由于还未实现注册页，目前只能通过命令行这种形式注册用户，而其他的用户则是不能登录的。

### 如何给新注册用户发送验证信息，使用`itsdangerous`生成有限期限的token id
```
$venv/bin/python run.py shell 
>>> from run import app
>>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
>>> s = Serializer(app.config['SECRET_KEY'], expires_in = 3600)
>>> token = s.dumps({ 'confirm': 23 })
>>> token
'eyJhbGciOiJIUzI1NiIsImV4cCI6MTQ1MDc3OTMyNiwiaWF0IjoxNDUwNzc1NzI2fQ.eyJjb25maXJtIjoyM30.i82WdsdJJ3x1b5lRhHMG0dKcs28FqFvBbOTuBHvplKI'
>>> data = s.loads(token)
>>> data
{u'confirm': 23}
````

### 初始化用户角色和权限
```
$venv/bin/python run.py shell

>>> Role.insert_roles()
>>> Role.query.all()
[<Role u'Moderator'>, <Role u'Administrator'>, <Role u'User'>]
>>> 
```

### 生成虚拟内容

```
$venv/bin/python run.py shell
>>> User.generate_fake(100)
>>> Post.generate_fake(100)
>>> 
```

http --json --auth : GET http://localhost:5000/api/v1.0/posts/
http --auth huangshujia@gracegene.com:cat --json GET http://localhost:5000/api/v1.0/token
http --auth huangshujia@gracegene.com:cat --json POST http://localhost:5000/api/v1.0/posts/ "body=I'm adding a post from the *command line*."


### 部署

```
venv/bin/gunicorn run:app
```


