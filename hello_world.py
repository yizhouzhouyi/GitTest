print("hello world!")
str1 = "hello world!"
str2 = "zhouyi"
f = open('helloworld.html','w')
message = """
<html>
<head></head>
<body>
<p>Welcome</p>
<p>%s</p>
<h1>%s</h1>
</body>
</html>"""%(str1,str2)

f.write(message)
f.close()