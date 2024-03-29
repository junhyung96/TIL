### GET 요청
목적: 데이터를 검색하거나 요청하기 위해 사용되는 HTTP 메서드입니다. 
예를 들어, 웹 페이지를 불러오거나, 검색 엔진에서 검색어를 전달할 때 사용됩니다.

데이터 전송 방식: URL의 일부로 데이터를 전송합니다. 예를 들어, http://example.com?query=keyword와 같이 URL 끝에 ? 뒤에 파라미터를 추가하여 데이터를 전달합니다.

제한 사항: URL 길이에 제한이 있기 때문에 전송할 수 있는 데이터의 양이 제한적입니다. 또한, 민감한 데이터를 전송하기에는 보안에 취약합니다.

캐싱: GET 요청은 결과를 캐싱할 수 있으므로, 같은 요청에 대해 서버의 부담을 줄일 수 있습니다.
### POST 요청
목적: 서버에 데이터를 제출하여 생성 또는 업데이트하기 위해 사용되는 HTTP 메서드입니다. 예를 들어, 사용자가 양식을 작성하고 제출할 때 사용됩니다.

데이터 전송 방식: 데이터는 요청 본문(body)에 포함되어 전송됩니다. 이는 URL에 데이터가 노출되지 않으므로 보안상 GET보다 안전합니다.

제한 사항: 데이터 양에 대한 제한이 없으며, 이진 데이터를 포함한 다양한 형태의 데이터를 전송할 수 있습니다.

캐싱: POST 요청은 기본적으로 캐싱되지 않습니다.
### GET과 POST의 주요 차이점
용도: GET은 주로 데이터를 요청하는 데 사용되며, POST는 데이터를 서버에 제출하는 데 사용됩니다.

데이터 전송 위치: GET은 URL을 통해 데이터를 전송하는 반면, POST는 요청 본문을 통해 데이터를 전송합니다.

보안: POST는 GET보다 보안이 더 좋습니다. GET은 URL에 데이터가 노출되어 민감한 정보에 대한 보안이 취약합니다.

데이터 크기: GET은 URL 길이에 제한이 있어 전송할 수 있는 데이터 양에 제한이 있습니다. POST는 이러한 제한이 없습니다.

캐싱과 이력: GET 요청은 캐싱될 수 있고, 브라우저 히스토리에 남지만, POST 요청은 보통 캐싱되지 않으멀로 브라우저 히스토리에 남지 않습니다.

GET과 POST는 HTTP 프로토콜에서 정의된 두 가지 기본적인 메서드로, 웹 개발에서 데이터를 전송하고 서버와 통신하는 데 있어 핵심적인 역할을 합니다.

#### -> GET방식과 POST방식의 가장 큰 차이점은 서버와 클라이언트가 데이터 통신을 할 때 데이터를 헤더에 담아 전달하느냐 바디에 담아 전달하느냐의 차이입니다. POST방식의 경우 데이터를 바디에 넣어 보내기 때문에 기본적으로 암호화해서 전달하지만 GET방식은 암호화하지 않습니다. 또한 POST방식은 GET방식보다 상대적으로 큰 데이터를 전송할 수 있어서 큰 데이터를 전송할 때에는 POST방식을 사용합니다.
