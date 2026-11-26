#!/usr/bin/env python3
"""posts/**/index.qmd 의 book-chapter / book-section 메타데이터를 읽어
Quarto Book용 _quarto-book.yml 의 chapters 목록을 생성한다.

사용:  python scripts/build_book_toc.py > book/_quarto.yml
"""
import re, sys, pathlib, yaml

PARTS = {
    "1부. 개념": range(1, 4),
    "2부. 데이터": range(4, 7),
    "3부. 연구": range(7, 11),
    "4부. 확장": range(11, 13),
}
CHAPTER_TITLES = {
    1: "의료 데이터는 왜 서로 통하지 않는가", 2: "FHIR의 구조 — 리소스, 참조, 용어",
    3: "FHIR API — 검색, 대량 추출, 인증", 4: "연구용 FHIR 데이터 확보하기",
    5: "병원 데이터를 FHIR로 — 변환과 OMOP CDM", 6: "FHIR에서 분석 테이블로",
    7: "코호트와 표현형을 코드로 정의하기", 8: "연구 설계 — Target Trial Emulation을 FHIR 위에 얹기",
    9: "분석 — 인과추론과 예측", 10: "재현성과 다기관 확장",
    11: "근거를 진료로 — PICO 정형화, CDS Hooks, LLM", 12: "한국에서 FHIR 연구 시작하기",
}

def front_matter(p):
    txt = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    return yaml.safe_load(m.group(1)) if m else {}

posts = []
for p in sorted(pathlib.Path("posts").glob("ch*/index.qmd")):
    fm = front_matter(p)
    ch, sec = fm.get("book-chapter"), fm.get("book-section")
    if not ch or fm.get("draft"):
        continue
    posts.append((int(ch), int(sec or 0), str(p), fm.get("title", "")))
posts.sort()

chapters = ["index.qmd"]
for part, rng in PARTS.items():
    part_entry = {"part": part, "chapters": []}
    for ch in rng:
        files = [f for c, s, f, t in posts if c == ch]
        if files:
            part_entry["chapters"].append({"part": f"{ch}장. {CHAPTER_TITLES[ch]}", "chapters": files})
    if part_entry["chapters"]:
        chapters.append(part_entry)

book = {
    "project": {"type": "book"},
    "book": {
        "title": "연구자를 위한 FHIR",
        "subtitle": "병원 데이터에서 근거 생성까지",
        "author": "Chiwon Ahn",
        "chapters": chapters,
    },
    "bibliography": "../references.bib",
    "format": {"html": {"theme": "cosmo"}, "pdf": {"documentclass": "scrbook"}},
}
yaml.safe_dump(book, sys.stdout, allow_unicode=True, sort_keys=False)
