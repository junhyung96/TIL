NGINX는 트래픽이 많은 웹사이트의 서버(WAS)를 도와주는 비동기 이벤트 기반 구조의 웹 구조 서버 프로그램

웹 서버, 리버스 프록시, 메일 프록시, 그리고 HTTP 캐시와 같은 다양한 기능을 제공하는 소프트웨어입니다. 

처음에는 웹 서버로 개발되었지만, 현재는 로드 밸런싱, HTTP 캐싱, 리버스 프록시 기능을 포함하여 고성능 및 고가용성을 요구하는 웹 애플리케이션을 위한 중요한 도구로 널리 사용됩니다.

### NGINX의 주요 기능

- **웹 서버**: 정적 콘텐츠(HTML, CSS, JavaScript 파일 등)를 제공하는 데 사용됩니다. NGINX는 비동기 이벤트 기반의 아키텍처를 사용하여 높은 동시성을 처리할 수 있습니다.
- **리버스 프록시**: 클라이언트의 요청을 받아 하나 이상의 백엔드 서버로 전달하고, 백엔드 서버의 응답을 클라이언트에게 다시 전송합니다. 이를 통해 부하 분산, SSL 종료, 정적 콘텐츠 캐싱 등을 수행할 수 있습니다.
- **로드 밸런서**: 여러 서버에 걸쳐 클라이언트의 요청을 분산시킵니다. 이는 웹 애플리케이션의 확장성과 가용성을 향상시킵니다.
- **HTTP 캐시**: 자주 요청되는 웹 페이지나 파일을 메모리 또는 디스크에 저장하여, 동일한 요청에 대해 더 빠르게 응답할 수 있게 합니다.
- **메일 프록시**: IMAP, POP3, SMTP 프로토콜을 지원하여 메일 서비스의 리버스 프록시 기능을 제공합니다.

### NGINX의 장점

- **성능**: NGINX는 비동기 이벤트 기반 모델을 사용하여 매우 높은 동시 연결을 처리할 수 있습니다. 이는 특히 정적 콘텐츠를 제공하거나 리버스 프록시로 사용될 때 큰 장점입니다.
- **유연성**: 다양한 프로토콜을 지원하고, URL 기반 라우팅, SSL/TLS 종료, 웹소켓, HTTP/2 지원 등 다양한 기능을 제공합니다.
- **확장성**: 로드 밸런싱 기능을 통해 애플리케이션을 수평적으로 확장할 수 있으며, 동적으로 서버를 추가하거나 제거할 수 있습니다.
- **보안**: 요청 필터링, IP 주소 기반의 액세스 제어, SSL/TLS 프로토콜을 통한 데이터 암호화 등 다양한 보안 기능을 제공합니다.
- **효율성**: 리소스 사용이 경제적이며, 적은 메모리와 CPU 사용으로 많은 수의 동시 연결을 처리할 수 있습니다.

NGINX는 다양한 운영 체제에서 사용할 수 있으며, 웹 사이트의 성능 향상, 보안 강화, 그리고 고가용성 구축을 위한 솔루션을 제공합니다. 이러한 이유로, 많은 인기 있는 웹 사이트와 서비스에서 NGINX를 선택하여 사용하고 있습니다.

