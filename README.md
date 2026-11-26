# FHIR for Research — 블로그 겸 책 원고 저장소

『연구자를 위한 FHIR』(12장)의 프리퀄 블로그. 글 1편 = 책의 절 1개.

## 구조
```
_quarto.yml            사이트 설정
index.qmd              최신 글 목록
series.qmd             책 목차 순 목록(1~12장 + Paper Notes)
about.qmd
posts/
  _metadata.yml        모든 글 공통 메타데이터
  _templates/          해설·실습·리뷰·Technical Note 템플릿
  chXX-YY-slug/        책 XX장 YY절에 해당하는 글
  notes-YYYYMMDD-slug/ Paper Notes
references.bib         공용 참고문헌(글별 bib 금지)
scripts/
  new_post.sh          템플릿에서 새 글 생성
  build_book_toc.py    메타데이터로 Quarto Book 목차 생성
assets/                스타일, CSL, 그림
.github/workflows/     GitHub Pages 자동 배포
```

## 시작
```bash
quarto preview                                   # 로컬 미리보기
scripts/new_post.sh tutorial 6 1 install-first-query
python scripts/build_book_toc.py > book/_quarto.yml   # 책으로 묶을 때
```

## 발행 규칙
- 트랙 A(해설, 격주): 1장부터 순서대로
- 트랙 B(실습·Technical Note, 격주): 현재 연구에서 나오는 것부터
- 분량 1,500–2,500자, 그림 1–2개. 길어지면 절을 나눈다
- 머리말(핵심 요약 3줄)·꼬리말(한계와 비판적 검토·참고문헌·수정 이력) 필수
- 본문 한국어, YAML `abstract-en` 3줄
- Technical Note는 `disclosure-check` 채운 뒤 게시

## 책으로 전환
`book-chapter`/`book-section` 메타데이터가 목차를 결정한다. `draft: true`인 글은 제외된다.
```
