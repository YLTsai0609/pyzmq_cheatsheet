# Infos

精通Python 第十一章 - 並行與網路

[github](https://github.com/zeromq/pyzmq)

[Pyzmq介紹](https://iter01.com/524761.html)

[doc](https://zeromq.org/get-started/?language=python&library=pyzmq#)

# getting start

 `pip install pyzmq`

## hello world

client或是server先開啟服務都可以，client找不到server可以丟的時候 `zmq` 會把狀態暫存起來，包含你要傳什麼，你要傳到哪裡，
這也就是為什麼一開始要開啟一個 `context` 物件

中途server掛了client也不會死，東西會存在context物件中

而所有的連線都必須基於context物件來建立，否則就無法讀取暫存的東西了，這是ZeroMQ的設計

## n_clients_1_server

zmq的context物件中有紀錄誰先誰後，達成公平的回應，先排隊的先處理(queue)

## n_clients_m_server

### failed case

check `n_clients_m_server_failed/`

server不能同時bind，會出現
 `zmq.error.ZMQError: Address already in use`

精通Python書中說明可以使用DEALER以及ROUTER來達到多client多server的運作模式

### successed case (local)

check `n_clients_m_server_broker/`

加入一個broker，broker作為一個代理，frontend接收client，backend接收worker

成功實現單一機器上，兩個client，兩個worker

[search the borker on docuemtnation](https://zguide.zeromq.org/docs/chapter2/)

### successed case (network)

### zmq server with tcp client

### cross language client

# 三種模式

# 通訊協定?
