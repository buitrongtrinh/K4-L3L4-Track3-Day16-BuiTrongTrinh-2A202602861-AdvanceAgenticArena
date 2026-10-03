"""Helper dùng chung cho các layer: so khớp trích dẫn theo cùng cách scorer so.

Chỉ ĐỌC và SO SÁNH — không bao giờ dùng để viết lại `claim["text"]`.
"""

from __future__ import annotations

import re
import unicodedata

_WS = re.compile(r"\s+")


def norm(text) -> str:
    """NFC + casefold + gộp khoảng trắng (giống `arena.scorer._norm`)."""
    if not isinstance(text, str):
        return ""
    return _WS.sub(" ", unicodedata.normalize("NFC", text).casefold()).strip()


def in_one_line(doc, text: str) -> bool:
    """`text` có nằm gọn trong MỘT dòng của `doc.body` không?"""
    needle = norm(text)
    if not needle:
        return False
    return any(needle in norm(line) for line in doc.body.splitlines())


def claim_text(claim) -> str:
    if isinstance(claim, dict) and isinstance(claim.get("text"), str):
        return claim["text"]
    return ""
