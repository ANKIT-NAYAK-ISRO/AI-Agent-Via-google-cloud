from __future__ import annotations

import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

load_dotenv()


class TextAnalysisResult(BaseModel):
    short_summary: str = Field(description="A short summary of the input text.")
    key_points: list[str] = Field(
        min_length=3,
        max_length=3,
        description="Exactly 3 key points from the input text.",
    )
    questions: list[str] = Field(
        min_length=2,
        max_length=2,
        description="Exactly 2 follow-up questions about the input text.",
    )


def _create_client() -> genai.Client:
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing API key. Set GOOGLE_API_KEY or GEMINI_API_KEY in your .env file."
        )
    return genai.Client(api_key=api_key)


def analyze_text(
    text: str,
    model: str = "gemini-2.5-flash",
    client: genai.Client | None = None,
) -> TextAnalysisResult:
    """Analyze text and return a short summary, 3 key points, and 2 questions."""
    if not text or not text.strip():
        raise ValueError("Input text cannot be empty.")

    active_client = client or _create_client()
    response = active_client.models.generate_content(
        model=model,
        contents=f"Analyze the following text:\n\n{text.strip()}",
        config=types.GenerateContentConfig(
            system_instruction=(
                "Analyze the provided text and respond using the schema only. "
                "Return a concise short summary, exactly 3 key points, and exactly "
                "2 relevant follow-up questions."
            ),
            response_mime_type="application/json",
            response_schema=TextAnalysisResult,
            temperature=0.2,
        ),
    )

    if response.parsed is None:
        raise ValueError("The model did not return a structured response.")

    return response.parsed


def process_text(
    text: str,
    model: str = "gemini-2.5-flash",
    client: genai.Client | None = None,
) -> TextAnalysisResult:
    """Compatibility wrapper for API usage."""
    return analyze_text(text=text, model=model, client=client)


if __name__ == "__main__":
    sample_text = (
        "Artificial intelligence helps computers perform tasks such as language "
        "understanding, image recognition, and decision support. It is used in "
        "healthcare, education, finance, and software development."
    )
    result = analyze_text(sample_text)
    print(result.model_dump_json(indent=2))
