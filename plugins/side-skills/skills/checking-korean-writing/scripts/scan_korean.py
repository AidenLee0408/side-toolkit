#!/usr/bin/env python3
"""Flag awkward Korean prose patterns in a Markdown or text file.

Evidence only: every hit is a candidate a person (or Claude) must read in
context. There is no score and no pass/fail verdict.

Usage:
  python3 scan_korean.py FILE [FILE ...]
  python3 scan_korean.py --json FILE
"""
import json
import re
import sys

HANGUL = re.compile(r"[가-힣]")
# Endings that close a Korean sentence properly (합니다체, 한다체, 해요체, questions).
GOOD_END = re.compile(r"(다|요|죠|까|오|라|자|네|지|어|야|세요|니다)[.!?…)\"'”’]*$")
PARTICLE_END = re.compile(r"(은|는|이|가|을|를|에|에서|의|로|으로|와|과|도|만|께|한테|부터|까지|처럼|보다|이나|나|고|며|면|서|게|지만|는데|니까)$")

TRANSLATIONESE = [
    (r"되어지|되어진|되어질", "이중 피동", "되다·하다로 줄인다"),
    (r"에 있어서|에 있어", "번역투 (in ~)", "'에서', '할 때'로 바꾼다"),
    (r"[을를] 통해(서)?", "번역투 (through)", "'로', '해서'로 바꿀 수 있는지 본다"),
    (r"것이 가능하|것이 필요하|것이 중요하", "명사화 (it is ~ to)", "'할 수 있다', '해야 한다'로 쓴다"),
    (r"에 의해(서)?", "피동 번역투 (by)", "능동문으로 바꿀 수 있는지 본다"),
    (r"을 가지고 있|를 가지고 있", "번역투 (have)", "'있다', '갖췄다'로 쓴다"),
    (r"하고 있는 중", "중복 진행형", "'하는 중' 또는 '하고 있다'"),
    (r"\b(그|이) (것|점)은 [^.]{0,20}(이다|입니다)", "강조 구문 (It is ~ that)", "주어를 바로 쓴다"),
]
CALQUES = ["처음 판", "미적 지시", "최종 판", "다관점", "동시 발동"]
NOUN_SUFFIX = re.compile(r"(방지|기록용|점검용|확인용|잡기|정리|관리|처리|적용|지정|개선|확인|검토|설치|사용|진행)$")


def is_prose(line):
    s = line.strip()
    if not s or not HANGUL.search(s):
        return False
    if s.startswith(("#", "|", "```", "---", ">", "<!--")):
        return False
    return True


def strip_list(s):
    return re.sub(r"^([-*+]|\d+\.)\s+", "", s.strip())


def sentences(text):
    text = re.sub(r"`[^`]*`", "CODE", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\*\*|__", "", text)
    for part in re.split(r"(?<=[.!?])\s+", text):
        part = part.strip()
        if part:
            yield part


def scan(path):
    hits = []
    in_code = False
    for no, raw in enumerate(open(path, encoding="utf-8"), 1):
        if raw.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        line = raw.rstrip("\n")
        cells = []
        if line.strip().startswith("|") and not re.match(r"^\|[\s:|-]+\|$", line.strip()):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
        body = strip_list(line) if is_prose(line) else ""
        targets = ([body] if body else []) + [c for c in cells if HANGUL.search(c)]
        for t in targets:
            clean = re.sub(r"`[^`]*`", "CODE", t)
            for pat, cat, tip in TRANSLATIONESE:
                for m in re.finditer(pat, clean):
                    hits.append((no, cat, m.group(0), tip))
            for c in CALQUES:
                if c in clean:
                    hits.append((no, "영어 직역", c, "한국어로 풀어 쓴다"))
            for m in re.finditer(r"[가-힣]+\s?/\s?[가-힣]+(\s?/\s?[가-힣]+)*", clean):
                if t is body:
                    hits.append((no, "빗금으로 잇기", m.group(0), "쉼표나 '또는'으로 쓴다"))
            if clean.count("—") >= 1:
                hits.append((no, "줄표", "—", "쉼표나 문장 나누기로 바꾼다"))
            for m in re.finditer(r"(?:[가-힣0-9]*[가-힣][가-힣0-9]*\s){3,}[가-힣]{2,}", clean):
                words = m.group(0).split()
                if not any(PARTICLE_END.search(w) or GOOD_END.search(w) for w in words[:-1]):
                    hits.append((no, "명사 이어 붙이기", m.group(0), "조사와 동사를 넣어 풀어 쓴다"))
        if body:
            for s in sentences(body):
                if not HANGUL.search(s) or len(s) < 12:
                    continue
                last = re.sub(r"[.!?…)\"'”’:]+$", "", s).split()[-1] if s.split() else ""
                if NOUN_SUFFIX.search(last) or (not GOOD_END.search(s) and re.search(r"[가-힣]$", last)):
                    hits.append((no, "명사로 끝나는 문장", s[-30:], "동사로 끝낸다 (~한다, ~합니다)"))
        for c in cells:
            last = c.split()[-1] if c.split() else ""
            if len(c) >= 8 and NOUN_SUFFIX.search(last):
                hits.append((no, "표 칸 명사 나열", c[-30:], "무엇을 하는지 동사로 쓴다 (표 칸은 짧아도 됨)"))
    return hits


def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    files = [a for a in args if a != "--json"]
    if not files:
        print(__doc__)
        return 2
    out = {}
    for f in files:
        out[f] = scan(f)
    if as_json:
        print(json.dumps({f: [dict(line=n, kind=k, text=t, tip=p) for n, k, t, p in h] for f, h in out.items()}, ensure_ascii=False, indent=1))
        return 0
    for f, hits in out.items():
        counts = {}
        for _, k, _, _ in hits:
            counts[k] = counts.get(k, 0) + 1
        print(f"# {f}: 후보 {len(hits)}건 " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items(), key=lambda x: -x[1])))
        for n, k, t, p in hits:
            print(f"  {n}: [{k}] {t}  → {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
