from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from agent import TextAnalysisResult, process_text

app = FastAPI(title="Text Analysis API")


class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1, description="The text to analyze.")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Text Analysis API is running."}


@app.post("/analyze", response_model=TextAnalysisResult)
def analyze(request: AnalyzeRequest) -> TextAnalysisResult:
    try:
        return process_text(request.text)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Failed to analyze text.") from exc
