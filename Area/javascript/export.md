
1. **`export`**
    
    - `export` 키워드는 모듈 파일에서 여러 개의 변수, 함수, 클래스 등을 내보낼 때 사용됩니다.
    - 하나의 모듈 파일에서 여러 `export` 문을 사용하여 여러 개의 이름이 있는 export를 정의할 수 있습니다.
    - 내보내는 변수, 함수, 클래스 등을 다른 파일에서 가져올 때, 가져올 때에도 동일한 이름을 사용해야 합니다.
    
```js
// 모듈 파일에서의 사용 
export const variable1 = "Value 1"; export function myFunction() { /* ... */ }  
// 다른 파일에서 가져올 때 
import { variable1, myFunction } from './moduleFile';
```
    
2. **`export default`**
    
    - `export default` 키워드는 모듈 파일에서 하나의 기본 값을 내보낼 때 사용됩니다.
    - 모듈에서 기본으로 내보낸 값은 이름이 없는데, 가져올 때 다른 이름으로 사용할 수 있습니다.
    - 한 모듈 파일에서 `export default`는 한 번만 사용할 수 있습니다.
    
```js
// 모듈 파일에서의 사용 
const defaultExport = "Default Value"; export default defaultExport;  
// 다른 파일에서 가져올 때 
import myDefault from './moduleFile';
```