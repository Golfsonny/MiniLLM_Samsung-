1. 🔧 Structured Data (구조화된 데이터)
edge.json → 이미 정제된 사양 정보 (예: CPU, 해상도 등)
보통 사람이 만든 JSON 형식
2. 🧾 Unstructured Data (비구조 데이터)
edge.html → 삼성 공식 홈페이지에서 실시간으로 받아온 HTML
이 HTML 안에는 프로모션 정보 (혜택, 사은품, 이벤트 등) 이 들어있음
웹페이지를 파싱해서 텍스트 추출 (BeautifulSoup 사용)


💡 왜 edge.html을 로컬에 저장하는가?
네트워크 요청 최소화
매번 삼성 홈페이지에 요청하면 느리고 비효율적
한 번 저장해두면 캐시처럼 사용 가능
오프라인 테스트 가능
서버 없이도 HTML 분석 테스트 가능
재현성 보장
예전 데이터를 기반으로 결과를 재현할 수 있음 (예: 테스트할 때 유리)


```bash
git config --global --list
git config --global user.name "yourname"
git config --global user.email youremail.@gmail.com
```
