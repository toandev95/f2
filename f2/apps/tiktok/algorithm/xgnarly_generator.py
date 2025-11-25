import execjs
from pathlib import Path


class XGnarlyGenerator:
    def __init__(self, user_agent: str = None):
        self.user_agent = (
            user_agent
            if user_agent is not None and user_agent != ""
            else "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
        )

    def generate(
        self, query_string: str, body: str = "", user_agent: str = None
    ) -> str:
        js_path = Path(__file__) / "encode.js"

        if not js_path.exists():
            raise FileNotFoundError(f"Không tìm thấy file encode.js tại {js_path}")

        js_code = js_path.read_text(encoding="utf-8")

        ctx = execjs.compile(js_code)

        result = ctx.call(
            "encode",
            {"queryString": query_string, "body": body, "userAgent": user_agent},
        )

        return result
