# 글 템플릿 사용법

1. 유형에 맞는 템플릿을 `posts/chXX-YY-slug/index.qmd`로 복사한다.
   - XX: 책 장 번호(두 자리), YY: 절 번호(두 자리). Paper Notes는 `posts/notes-YYYYMMDD-slug/`.
2. YAML의 `book-chapter`, `book-section`, `post-type`, `series`를 채운다.
3. 본문 틀의 머리말(핵심 요약 3줄·대상 독자·선수지식)과 꼬리말(한계와 비판적 검토·참고문헌·수정 이력)은 지우지 않는다.
4. 참고문헌은 글에 넣지 말고 루트 `references.bib`에 추가한 뒤 `[@key]`로 인용한다.
5. 코드는 복사하지 말고 저장소 패키지에서 import한다.
6. 공개 전 체크: 논문 투고 상태, 특허 출원 상태, 이해상충.

`post-type` 값: 해설 | 실습 | 리뷰 | technical-note | 관점
`series` 값: FHIR 기초 | FHIR for Research | 연구 설계·분석 | CDSS 설계 | 국내 FHIR 현황 | Paper Notes
