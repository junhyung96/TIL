
### 어노테이션
### JPA 관련 어노테이션:

#### @Entity
- 클래스가 JPA 엔티티임을 나타냅니다. 이 어노테이션이 붙은 클래스는 데이터베이스 테이블과 매핑됩니다.

#### @Table
- 엔티티 클래스가 매핑될 데이터베이스 테이블의 정보를 제공합니다. `name` 속성을 통해 테이블 이름을 지정할 수 있습니다. 속성을 생략하면 클래스 이름이 테이블 이름으로 사용됩니다.

#### @Id
- 해당 필드가 엔티티의 기본 키(Primary Key)임을 나타냅니다.

#### @GeneratedValue
- 기본 키의 값을 자동으로 생성하는 전략을 지정합니다. `strategy = GenerationType.IDENTITY`는 데이터베이스의 identity 컬럼을 이용하여 기본 키 값을 생성합니다.

#### @Column
- 필드가 매핑될 데이터베이스 테이블의 컬럼 정보를 제공합니다. `name` 속성을 통해 컬럼 이름을 지정할 수 있습니다. 생략할 경우 필드 이름이 컬럼 이름으로 사용됩니다.

### Lombok 관련 어노테이션:

#### @Data
- 클래스의 모든 필드에 대해 게터(getter), 세터(setter), `toString()`, `equals()`, `hashCode()` 메서드를 자동으로 생성합니다.

#### @Builder
- 빌더 패턴을 구현한 클래스를 자동으로 생성합니다. 이를 통해 불변 객체의 생성이나 선택적 매개변수를 가진 객체의 생성을 쉽게 할 수 있습니다.

#### @AllArgsConstructor
- 클래스의 모든 필드를 매개변수로 받는 전체 생성자를 자동으로 생성합니다.

#### @NoArgsConstructor
- 파라미터가 없는 기본 생성자를 자동으로 생성합니다.