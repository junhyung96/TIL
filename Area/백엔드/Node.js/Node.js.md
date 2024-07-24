
- 자바스크립트를 어디서든 동작하게 하기 위한 [[런타임 환경]]
	- 브라우저 밖에서 자바스크립트 코드 실행 가능
- 노드를 사용하기 위해서는 비동기에 익숙해져야 한다
### 특징
#### 1. 이벤트 기반의 비동기 I/O 프레임워크
- 클라이언트는 어플리케이션에 요청을 보낸다
- 요청을 이벤트로 만들고 이벤트 큐에 쌓음
- 이벤트 루프는 이벤트를 하나씩 꺼내 작업을 완료
- 비동기 처리 
	- 이벤트가 시간이 오래걸리는 경우 다른 워커 스레드에게 위임함 ( Non-blocking Worker )
	- 워커 스레드는 이벤트 결과를 반환
	- 결과는 이벤트 큐에 저장됨 ( 이후 이벤트 루프에서 작업 완료 후 클라이언트에게 반환 ) 

#### 2.  CommonJS 를 구현한 모듈 시스템
- 브라우저에서는 윈도우 컨텍스트를 사용하거나, RequireJS 같은 의존성 로더를 사용함
- 노드는 파일 형태로 모듈을 관리할 수 있는 CommonJS 로 구현
	- 파일 형태로 모듈을 관리할 수 있다
		- 웹 브라우저 안에서는 파일에 접근할 수 없었지만
		- Node.js 는 서버이기에 파일을 읽을 수 있다
	- 기본 모듈
	- 써드파티 모듈
	- 사용자 정의 모듈

- 확장성을 가지고 있다
	- 이하 문서 공부 후 추가

- Node.js® is a free, open-source, cross-platform JavaScript runtime environment that lets developers create servers, web apps, command line tools and scripts.

- As an asynchronous event-driven JavaScript runtime, Node.js is designed to build scalable network applications. In the following "hello world" example, many connections can be handled concurrently. Upon each connection, the callback is fired, but if there is no work to be done, Node.js will sleep.
```js
const { createServer } = require('node:http');

const hostname = '127.0.0.1';
const port = 3000;

const server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

```

- This is in contrast to today's more common concurrency model, in which OS threads are employed. Thread-based networking is relatively inefficient and very difficult to use. Furthermore, users of Node.js are free from worries of dead-locking the process, since there are no locks. Almost no function in Node.js directly performs I/O, so the process never blocks except when the I/O is performed using synchronous methods of Node.js standard library. Because nothing blocks, scalable systems are very reasonable to develop in Node.js.

- [Blocking vs. Non-Blocking](https://nodejs.org/en/learn/asynchronous-work/overview-of-blocking-vs-non-blocking)

- Node.js is similar in design to, and influenced by, systems like Ruby's [Event Machine](https://github.com/eventmachine/eventmachine) and Python's [Twisted](https://twisted.org/). Node.js takes the event model a bit further. It presents an event loop as a runtime construct instead of as a library. In other systems, there is always a blocking call to start the event-loop. Typically, behavior is defined through callbacks at the beginning of a script, and at the end a server is started through a blocking call like `EventMachine::run()`. In Node.js, there is no such start-the-event-loop call. Node.js simply enters the event loop after executing the input script. Node.js exits the event loop when there are no more callbacks to perform. This behavior is like browser JavaScript — the event loop is hidden from the user.

- HTTP is a first-class citizen in Node.js, designed with streaming and low latency in mind. This makes Node.js well suited for the foundation of a web library or framework.

- Node.js being designed without threads doesn't mean you can't take advantage of multiple cores in your environment. Child processes can be spawned by using our [`child_process.fork()`](https://nodejs.org/api/child_process.html) API, and are designed to be easy to communicate with. Built upon that same interface is the [`cluster`](https://nodejs.org/api/cluster.html) module, which allows you to share sockets between processes to enable load balancing over your cores.