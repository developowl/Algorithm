## Data Structures
### List

초기화: `[]` or `[0] * N`
요소 추가: `arr.append(x)`(맨 뒤에 추가), `arr.insert(i, x)`(인덱스 i에 삽입)
요소 제거: `arr.pop()`(맨 뒤 요소 반환 후 제거), `arr.remove(x)`(값 x를 찾아 제거)
슬라이싱: `arr[start:end:step]`(원본을 변경하지 않고, 새로운 리스트를 생성)
정렬: `arr.sort()`(원본 리스트를 정렬), `sorted(arr)`(정렬된 새 리스트 반환)
    - `arr.sort(reverse=True)`(내림차순)
List Comprehension: `squares = [i*i for i in range(10) if i % 2 == 0]`(리스트를 간결하게 생성)

### Dictionary

초기화: `{}`, `dict()`, `dict[key] = value` 형태로 사용
키 존재 확인: `key in dict`
키/값/쌍 얻기: `d.keys()`, `d.values()`, `d.items()`
값 얻기: `d.get(key, default,_value)` 키가 없어도 에러 대신 default_value 반환(기본값 None)

### Tuple
- List와 유사하지만 불변(Immutable) 객체.
- 한 번 생성되면 수정할 수 없음.

### Set
- 중복을 허용하지 않는 자료구조
초기화: `set()`, `{1,2,3}`
요소 추가/제거: `s.add(x)`, `s.remove(x)`
집합 연산: `&`(교집합), `|`(합집합), `-`(차집합)

---

## Built-in Functions & Modules
- `min()`, `max()`, `sum()`
- `abs()`: 절댓값
`enumerate()`: 반복 시 인덱스와 값을 얻을 때 사용
- `zip()`: 여러 시퀀스 요소를 묶음
- `Collections Module`: `deque`(큐/스택 구현), `Counter`(요소의 개수)
- `heapq Module`: `Heap`(힙 구현, 우선순위 큐 등에 활용)

## Lambda, Map, Filter
- `lambda`: 간결한 익명 함수를 정의
- `map()`: 시퀀스의 각 요소에 함수를 적용 (ex: `list(map(int, input().split()))`)
- `filter()`: 시퀀스에서 조건에 맞는 요소만 필터링 (ex: `list(filter(lambda x: x > 10, data1))`)

