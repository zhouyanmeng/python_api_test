####1接口基础：http协议----interface
##usb-->是一个接口   硬件接口
##3.5耳机口-->是一个接口   硬件接口
##www.baidu,com -->不是接口
##函数不一定是一个接口      ##私有函数   共有函数        APIs---应用程序可编程接口
##UI-----user interface  -->是接口



####2  http请求
###http  是协议
###https  安全
#域名：https://xs.ydcfo.com    IP地址

####3消息头
#1请求网址
#2请求方法：get  post delete head patch option（get，post请求的区别）
#3远程地址
'''
地址----域名
邮编----ip
tcp/ip协议：：：域名/远程地址
DNS解析：将域名解析成ip
服务器：（后端：处理请求：被动方）
客户端：浏览器，app，硬件，其他（前端：发送请求：主动方）
    '''
#4状态码
#5版本
#6referrer政策

####4请求信息：请求头 请求体  header说明信息
#Accept
#Accept-Encoding
#Accept-Language
#Connection
#Cookie
#Host
#Upgrade-Insecure-Requests
#User-Agent    篡改消息头

#get 请求头里面可以包含请求内容（请求参数）
#https://api.gitbug.com?content=你最接近好吗？
#请求体
#Cookie：！=缓存
#会员机制
#http无状态，记性不好，记不住事，
#cookie，1第一次请求一个网址，==网址会给我们派发一个会员卡，session_id
#保存，浏览器会自动的保存cookie信息，请求是允许浏览器保存--》保存目标网站，cookie值，cookie类型
#2第二次请求目标网站，浏览器会自动带上目标网站的cookie

#####5响应信息：响应头，响应体
#http：都会发送一个回信给请求方，，，信息：响应body主题
#状态码：http内部管理的一种机制，   每一个动作状态都标记一个状态，
#200：请求成功：只是表示请求成功，
#201：一个资源被创建，请求已成功，通常用在put请求
#202：请求收到，就是不响应
#204
#300：；重定向
#304：没有修改，从缓存里面取出来的，你要的资源没有发生变化修改，我就不走服务器直接从缓存里面给你就好了
#400:请求参数有误
#401：用户没有通过验证，不具备权限（对不上）
#403：服务器已经理解，但是拒绝执行（对上了，没权限）
#404：没有发现这个网址：基本就是请求地址错误
#405：请求方法不允许
#408：请求超时
#500:5开头的，都是服务器的问题

####5.1响应头
####5.2响应体：


###cookie session，token
#cookie：浏览器保存在本地的信息
#session：服务器处理的信息
#token：令牌，口令：：：1随时待在身上，每一次请求都带带着令牌 2动态的
## 都有记住我是谁的功能
##区别：cookie只能访问目标网站，浏览器储存的
##token是随时戴在身上的，
##token是动态的
##token：是跨平台的，cookies是浏览器上面的
##token：是跨平台的，cookies是浏览器上面的













