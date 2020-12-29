# Goal

N client -> broker (automatic loading balance) -> M yolo workers

Basically we are following Synchronous Request/Response broker pattern.

Version

version : 20.0.0

# getting start

Since we have `07_cross_machine_broker` , we are in a good start.

Still, we need a cross-process, cross-thread sample code so that we can dive into our work.

# 08_cross_process

[Create Zero-Point Failure Distributed Tasks With Python and ZeroMQ](https://medium.com/better-programming/create-zero-point-failure-distributed-tasks-with-python-and-zeromq-e2a20941d85b)

The connection string of ZeroMQ is well designed for elegant usage.

The form is `transport:endpoint`

transport : 

1. **inproc** - thread to thread within a single process
2. **ipc** - inter-process communication(Linux only and bot available in any of the native ports as yet)
3. **tcp** - box to box communication and iter-process when ipc isn't available
4. **epgm, pgm** - multicase protocols

Getting the Context Right

One process one context. Technically, the context is the container for all sockets in a single process, and acts as the transport for `inproc` sockets, which are the fastest way to connect threads in one process. If two ZeroMQ instances is not what you want. Do

Call `zmq_ctx_new()` once at the start of a process and `zmq_ctx_destroy()` once at the end. Otherwise, the resource is hanged by the socket connection you built.

* **poller** vs **proxy**

# 09_control_traffic

knowing how many clients comes in, and design how many workers we need to turn on, and turn off.

# Tech debt

* difference between poller and proxy

* 
