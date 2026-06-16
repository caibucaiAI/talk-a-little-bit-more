#!/usr/bin/env python3
"""Optional helper for reviewing a long transcript with an OpenAI-compatible API.

This script is intentionally generic. It reads the API key from the environment
and writes the review next to the input file. Do not commit real transcripts or
generated private reviews to a public repository.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from openai import OpenAI


MODEL = os.environ.get("CONVERSATION_REVIEW_MODEL", "gpt-4.1")


SYSTEM_PROMPT = """You are a conversation review assistant.
Find moments where the user could have stayed curious for one more turn.
Give concrete, natural follow-up questions. Do not diagnose people.
Write in second person, with specific references to the transcript."""


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python run_example.py transcript.txt")
        return 1

    transcript_path = Path(sys.argv[1])
    transcript = transcript_path.read_text(encoding="utf-8")

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": transcript},
        ],
    )

    review = response.choices[0].message.content or ""
    output_path = transcript_path.with_name(f"{transcript_path.stem}-review.md")
    output_path.write_text(review, encoding="utf-8")
    print(f"Review written to: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

