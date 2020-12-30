# Infos

精通Python 第十一章 - 並行與網路

[github](https://github.com/zeromq/pyzmq)

[Pyzmq介紹](https://iter01.com/524761.html)

[doc](https://zeromq.org/get-started/?language=python&library=pyzmq#)

[doc中文翻譯 - third party](https://blog.maxkit.com.tw/2019/09/zeromq-2-sockets-and-patterns.html)

[pyzmq code and examples](https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/pyzmq.html)

# getting start

 `pip install pyzmq`

## 01_hello_world

client或是server先開啟服務都可以，client找不到server可以丟的時候 `zmq` 會把狀態暫存起來，包含你要傳什麼，你要傳到哪裡，
這也就是為什麼一開始要開啟一個 `context` 物件

中途server掛了client也不會死，東西會存在context物件中

而所有的連線都必須基於context物件來建立，否則就無法讀取暫存的東西了，這是ZeroMQ的設計

## 02_n_clients_1_server

zmq的context物件中有紀錄誰先誰後，達成公平的回應，先排隊的先處理(queue)

## n_clients_m_server

### 03_n_clients_m_server_failed

server不能同時bind，會出現
 `zmq.error.ZMQError: Address already in use`

精通Python書中說明可以使用DEALER以及ROUTER來達到多client多server的運作模式

### 04_n_clients_m_server_broker

check `n_clients_m_server_broker/`

加入一個broker，broker作為一個代理，frontend接收client，backend接收worker

成功實現單一機器上，兩個client，兩個worker

[search the borker on docuemtnation](https://zguide.zeromq.org/docs/chapter2/)

### 05_zmq server with tcp client

TCP/ZMQ可以進行連接及傳送資訊，但是header有些不同，zmq對於tcp協定是侵入式的，他們魔改了一部分，可以參考[這裡](https://www.cnblogs.com/neooelric/p/9020872.html)

### 06_cross_machine

[check official documentation](http://api.zeromq.org/2-1:zmq-tcp)

server : `socket.bind("tcp://*:5555")`

client : connect `tcp://server_ip:5555`

easy!

### 07_cross_machine_broker

broker : 

 `frontend = context.socket(zmq.ROUTER)`

 `backend = context.socket(zmq.DEALER)`

 `frontend.bind("tcp://*:5559")`

 `backend.bind("tcp://*:5560")`

client : connect `tcp://broker_ip:5559`

server : connect `tcp://broker_ip:5560`

easy!

### cross language client

offical guarantee

### inter-process/inter-thread

offical guarantee

# 三種模式

[ZeroMQ及其模式](https://zhuanlan.zhihu.com/p/22947038)

# 通訊協定

ZeroMQ實作了自己的通訊協定，但API和socket很像，連接方式和tcp很像，但其實是魔改後的版本，稱作[ZMTP](https://rfc.zeromq.org/spec/23/)，ZeroMQ目前在分散式訊息列隊中有著最好的效能，但目前並不是主流協定，ZeroMQ也實作了自己的http協定稱為[ZHTTP](https://rfc.zeromq.org/spec/33/)

# 單字

[IPC(Inter-Process Communication)](https://www.jianshu.com/p/5788fb2345ce)

[Socket]

1. (https://www.jianshu.com/p/5788fb2345ce)
2. (https://zh.wikipedia.org/zh-tw/Berkeley%E5%A5%97%E6%8E%A5%E5%AD%97)

* BSD Socket - 一種用於本地端進程間通訊或是跨機器通訊的API

# 缺點

ZeroMQ對TCP協定魔改，改變了TCP必須1對1的這個做法，可以做到M to N，這也就意味著無法透過ZeroMQ實現目前市面上有的網路協定，例如HTTP，SMTP等

ZeroMQ貌似使用了自己開發的通訊協定，從傳輸層到應用層都有自己開發的痕跡，這意味著跨團隊的合作會對其他團隊增加理解成本

[check here](https://blog.csdn.net/zhangzhebjut/article/details/12884149)
