state는 컴포넌트 내부에서 관리하는 상태라면
props는 컴포넌트 외부에서 들어와 내부 UI에 영향을 미침

```jsx
const Hello = ({name}) => <> Hello {name} </>

<Hello name="world" /> 
```