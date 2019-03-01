##配置文件  ini   conf   propties  py文件里面的变量也是一种配置项
login_info=[["http://47.107.168.87:8080/futureloan/mvc/api/member/login", "get", {"mobilephone": "18688773467", "pwd": "123456"},
       "登录成功"],
      ["http://47.107.168.87:8080/futureloan/mvc/api/member/login","post",
       {"mobilephone": "18688773467", "pwd": "123456"},  "登录成功"],
      ["http://47.107.168.87:8080/futureloan/mvc/api/member/login", "post",
       {"mobilephone": "18688773422", "pwd": "123456"}, "用户名或密码错误"],
      ["http://47.107.168.87:8080/futureloan/mvc/api/member/login","post",
       {"mobilephone": "18688773467", "pwd": "111111"}, "用户名或密码错误"]
]
