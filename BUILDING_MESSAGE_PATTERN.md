# Goal

N client -> broker (automatic loading balance) -> M yolo workers

Basically we are following Synchronous Request/Response broker pattern.

Version

version : 20.0.0

# best practice

About `Context` object

One process one context. Technically, the context is the container for all sockets in a single process, and acts as the transport for `inproc` sockets, which are the fastest way to connect threads in one process. If two ZeroMQ instances is not what you want. Do

Call `zmq_ctx_new()` once at the start of a process and `zmq_ctx_destroy()` once at the end. Otherwise, the resource is hanged by the socket connection you built.

# getting start

Since we have `07_cross_machine_broker` , we are in a good start.

Still, we need a cross-process, cross-thread sample code so that we can dive into our work.

# 08_cross_process_thread

不需要mutexes, lock 或是任何跨Thread的連接，請使用ZeroMQ sockets，ZeroMQ作者認為透過ZeroMQ來寫多線程任務是很完美的，同樣的設計可以再任意程式語言，任意作業系統，任意規模的CPU，近乎不用等待時間

注意事項 ： 請不要共享狀態

使用ZeroMQ撰寫，要注意的事項如下

1. 資料分離，不要在多個thread之間共享資料，只能用ZeroMQ context(threadsafe)傳遞資料
2. 不要使用傳統的concurrenct mechanisms，例如mutexes, criticl sections, ...
3. 在Process啟動時，產生一個ZeroMQ context，然後傳給其他需要使用inproc socket的thread
4. 利用 attached thread 產生 structure，並以 inproc 的 PAIR socket 連接到 parent threads，pattern 為 bind parent socket，然後產生連接該 socket 的 child thread
5. 使用 attached threads 以他們自己的 contexts 模擬獨立 tasks，以 tcp 方式連線。然後再將程式移到 stand-alone processes。
6. 只能用 ØMQ message 在 thread 之間傳遞資料
7. 不要在 thread 之間分享 ØMQ socket，因為 ØMQ socket 不是 threadsafe

# 09_control_traffic

knowing how many clients comes in, and design how many workers we need to turn on, and turn off.

# Note

## The connection string

[Create Zero-Point Failure Distributed Tasks With Python and ZeroMQ](https://medium.com/better-programming/create-zero-point-failure-distributed-tasks-with-python-and-zeromq-e2a20941d85b)

The connection string of ZeroMQ is well designed for elegant usage.

The form is `transport:endpoint`

transport : 

1. **inproc** - thread to thread within a single process
2. **ipc** - inter-process communication(Linux only and bot available in any of the native ports as yet)
3. **tcp** - box to box communication and iter-process when ipc isn't available
4. **epgm, pgm** - multicase protocols

## Poller vs Proxy

poller 

zmq_poll : 訊息傳遞器，在兩個socket之間傳遞，該物件不管理任何queue，用於request-reply模型

proxy 

zmq_proxy : 看poller的code，還要再寫一個while loop去監聽frontend以及backend，ZeroMQ把poller包起來，讓你可以直接用proxy

# Tech debt

* difference between poller and proxy
