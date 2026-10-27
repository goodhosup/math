"""docs/ 의 마크다운을 위키독스 책으로 발행하는 스크립트.

위키독스 MCP 서버(https://wikidocs.net/mcp)를 JSON-RPC로 직접 호출합니다.
가이드: https://wikidocs.net/289752

사용법 (저장소 루트에서):
    export WIKIDOCS_TOKEN=발급받은토큰
    python3 tools/publish_wikidocs.py            # 발행
    python3 tools/publish_wikidocs.py --dry-run  # 서버 호출 없이 순서만 확인

- 같은 제목의 책이 이미 있으면 그 책을 다시 씁니다.
- 만든 페이지 번호는 .wikidocs-state.json 에 저장해서, 다시 실행하면 새로 만들지 않고 내용만 갱신합니다.
- 페이지 사이 링크(*.md)는 위키독스 페이지 주소로, 그림(../images/*.svg)은 위키독스에 업로드한 주소로 바꿉니다.
- 표준 라이브러리만 씁니다.
"""
import base64
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS = os.path.join(ROOT, "docs")
STATE = os.path.join(ROOT, ".wikidocs-state.json")
ENDPOINT = "https://wikidocs.net/mcp"
BOOK_SUBJECT = "수포자를 위한 고등수학"
BOOK_SUMMARY = "수학을 포기했던 사람도 처음부터 다시 시작할 수 있는 쉬운 고등학교 수학 안내서"
FIRST_SECTION = "처음 오셨나요?"


def read_nav():
    """mkdocs.yml 의 nav 를 [(섹션 제목, [(페이지 제목, 경로), ...]), ...] 로 읽는다."""
    lines = open(os.path.join(ROOT, "mkdocs.yml"), encoding="utf-8").read().split("\nnav:\n", 1)[1].splitlines()
    unq = lambda s: s.strip().strip('"')
    nav = []
    for line in lines:
        m = re.match(r"^  - (.+):\s*$", line)
        if m:
            nav.append((unq(m.group(1)), []))
            continue
        m = re.match(r'^      - ("[^"]+"|[^:]+): (\S+\.md)\s*$', line)
        if m:
            nav[-1][1].append((unq(m.group(1)), m.group(2)))
    return nav


class Client:
    def __init__(self, token, dry):
        self.token, self.dry, self.session, self.n = token, dry, None, 0
        self.fake = 1000

    def _post(self, payload):
        headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream",
                   "Authorization": f"Token {self.token}"}
        if self.session:
            headers["Mcp-Session-Id"] = self.session
        req = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode(), headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=120) as r:
            self.session = r.headers.get("Mcp-Session-Id") or self.session
            body = r.read().decode("utf-8")
        if not body.strip():
            return None
        if body.lstrip().startswith("{"):
            return json.loads(body)
        msgs = [json.loads(l[5:]) for l in body.splitlines() if l.startswith("data:") and l[5:].strip()]
        return msgs[-1] if msgs else None

    def start(self):
        if self.dry:
            return
        self._post({"jsonrpc": "2.0", "id": 0, "method": "initialize", "params": {
            "protocolVersion": "2025-03-26", "capabilities": {},
            "clientInfo": {"name": "publish_wikidocs", "version": "1"}}})
        self._post({"jsonrpc": "2.0", "method": "notifications/initialized"})

    def call(self, name, **args):
        if self.dry:
            self.fake += 1
            print(f"  [dry-run] {name} {({k: (v[:40] + '…' if isinstance(v, str) and len(v) > 40 else v) for k, v in args.items()})}")
            return {"id": self.fake, "url": f"https://wikidocs.net/{self.fake}", "markdown": f"![]({args.get('filename', '')})"}
        self.n += 1
        res = self._post({"jsonrpc": "2.0", "id": self.n, "method": "tools/call",
                          "params": {"name": name, "arguments": args}})
        if res is None or "error" in res:
            raise RuntimeError(f"{name} 실패: {res}")
        result = res["result"]
        text = "\n".join(c.get("text", "") for c in result.get("content", []) if c.get("type") == "text")
        if result.get("isError"):
            raise RuntimeError(f"{name} 실패: {text}")
        if result.get("structuredContent"):
            return result["structuredContent"]
        try:
            return json.loads(text)
        except ValueError:
            return {"text": text}


def find_id(obj, keys=("id", "page_id", "book_id")):
    """도구 응답에서 숫자 id 를 찾는다."""
    if isinstance(obj, dict):
        for k in keys:
            if isinstance(obj.get(k), int):
                return obj[k]
            if isinstance(obj.get(k), str) and obj[k].isdigit():
                return int(obj[k])
        for v in obj.values():
            r = find_id(v, keys)
            if r:
                return r
    if isinstance(obj, list):
        for v in obj:
            r = find_id(v, keys)
            if r:
                return r
    if isinstance(obj, str):
        m = re.search(r'"?(?:page_id|book_id|id)"?\s*[:=]\s*(\d+)', obj) or re.search(r"wikidocs\.net/(\d+)", obj)
        return int(m.group(1)) if m else None
    return None


def find_book(books, subject):
    items = books
    if isinstance(books, dict):
        items = next((v for v in books.values() if isinstance(v, list)), [])
    for b in items if isinstance(items, list) else []:
        if isinstance(b, dict) and b.get("subject") == subject:
            return find_id(b)
    if isinstance(books, dict) and "text" in books:
        m = re.search(r"(\d+)\D{0,40}" + re.escape(subject), books["text"]) or \
            re.search(re.escape(subject) + r"\D{0,40}?(\d+)", books["text"])
        return int(m.group(1)) if m else None
    return None


def stage_intro(title, pages):
    lines = [f"# {title}", "", "이 단계의 단원입니다. 순서대로 공부하세요.", ""]
    lines += [f"- [{t}]({p})" for t, p in pages]
    return "\n".join(lines) + "\n"


def main():
    dry = "--dry-run" in sys.argv
    token = os.environ.get("WIKIDOCS_TOKEN", "")
    if not token and not dry:
        sys.exit("WIKIDOCS_TOKEN 환경변수에 위키독스 API 토큰을 넣어 주세요.")
    state = {} if dry or not os.path.exists(STATE) else json.load(open(STATE, encoding="utf-8"))
    save = lambda: None if dry else json.dump(state, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    c = Client(token, dry)
    c.start()

    # 1. 책
    book_id = state.get("book_id")
    if not book_id:
        book_id = None if dry else find_book(c.call("list_books"), BOOK_SUBJECT)
        if not book_id:
            book_id = find_id(c.call("create_book", subject=BOOK_SUBJECT, summary=BOOK_SUMMARY, open_yn="Y"))
        if not book_id:
            sys.exit("책 id 를 응답에서 찾지 못했습니다.")
        state["book_id"] = book_id
        save()
    print(f"책: https://wikidocs.net/book/{book_id}")

    # 2. 페이지 만들기 (nav 순서, 처음엔 원문 그대로)
    nav = read_nav()
    order = []  # (경로, 제목, 부모 경로 또는 None, 본문)
    for section, pages in nav:
        if section == FIRST_SECTION:
            for t, p in pages:
                order.append((p, t, None, open(os.path.join(DOCS, p), encoding="utf-8").read()))
        else:
            key = "stage:" + section
            order.append((key, section, None, stage_intro(section, pages)))
            for t, p in pages:
                order.append((p, t, key, open(os.path.join(DOCS, p), encoding="utf-8").read()))
    pages_state = state.setdefault("pages", {})
    for path, title, parent, body in order:
        if path in pages_state:
            continue
        args = dict(book_id=book_id, subject=title, content=body, open_yn="Y")
        if parent:
            args["parent_id"] = pages_state[parent]
        pid = find_id(c.call("create_page", **args))
        if not pid:
            sys.exit(f"'{title}' 페이지 id 를 응답에서 찾지 못했습니다.")
        pages_state[path] = pid
        save()
        print(f"  만듦: {title} → https://wikidocs.net/{pid}")

    # 3. 링크와 그림 고치기
    images = state.setdefault("images", {})
    for path, title, parent, body in order:
        pid = pages_state[path]

        def fix_link(m):
            text, target = m.group(1), m.group(2)
            if re.match(r"^[a-z]+://", target) or not target.split("#")[0].endswith(".md"):
                return m.group(0)
            rel = target.split("#")[0]
            src_dir = os.path.dirname(path) if not path.startswith("stage:") else ""
            norm = os.path.normpath(os.path.join(src_dir, rel)) if not path.startswith("stage:") else rel
            if norm in pages_state:
                return f"[{text}](https://wikidocs.net/{pages_state[norm]})"
            return text

        def fix_image(m):
            alt, target = m.group(1), m.group(2)
            if re.match(r"^[a-z]+://", target):
                return m.group(0)
            name = os.path.basename(target)
            key = f"{pid}:{name}"
            if key not in images:
                data = base64.b64encode(open(os.path.join(DOCS, "images", name), "rb").read()).decode()
                try:
                    r = c.call("upload_page_image", page_id=pid, filename=name, data=data)
                    md = r.get("markdown") if isinstance(r, dict) else None
                    if not md:
                        text = json.dumps(r, ensure_ascii=False)
                        mm = re.search(r"!\[[^\]]*\]\(([^)]+)\)", text) or re.search(r"(https?://[^\s\"']+)", text)
                        md = f"![]({mm.group(1)})" if mm else f"![]({name})"
                    url = re.search(r"\(([^)]+)\)", md).group(1)
                    images[key] = url
                    save()
                except Exception as e:  # 그림 하나가 실패해도 나머지는 계속
                    print(f"  그림 업로드 실패 ({title}, {name}): {e}")
                    return f"*(그림: {alt})*"
            return f"![{alt}]({images[key]})"

        new = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", fix_image, body)
        new = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)", fix_link, new)
        c.call("update_page", page_id=pid, content=new)
        print(f"  링크·그림 반영: {title}")
    print(f"완료: 페이지 {len(pages_state)}개")


if __name__ == "__main__":
    main()
