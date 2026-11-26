# 웹 시안 원본

[`../../web-concept-v4.md`](../../web-concept-v4.md)의 시안 v4. 발행본: https://claude.ai/artifact/FBwWKj9Jxavz52zkwMe2t5

- `src.html` — 시안 원본. 로고는 `brand/logo/` 원본 패스를 그대로 넣었고, 서체 자리는 `/* FONTS */`.
- 다시 뽑기: `python3 tools/build-web-prototype.py channels/web/prototype/src.html <out.html>` — Pretendard를 쓰인 글자만 잘라 넣은 한 장짜리 HTML이 나온다 (`pip install fonttools brotli` 필요).
- 운영 코드가 아니다. 운영 코드의 위치는 `decisions.md` Q10.
