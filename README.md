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
