from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from ai_reviewer import ai_review_pr
from storage.s3_client import save_text, save_json
from storage.s3_client import read_json, s3, BUCKET_NAME
from fastapi import HTTPException
from fastapi.responses import StreamingResponse

app = FastAPI(title="AI PR Reviewer")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# ✅ Request body schema
class PRPayload(BaseModel):
    title: str
    description: str
    diff: str


@app.get("/")
def health_check():
    return {"status": "AI PR Reviewer running"}


@app.post("/review")
def review_pr(payload: PRPayload):
    # 1️⃣ Run AI review (existing logic – untouched)
    result = ai_review_pr(
        payload.title,
        payload.description,
        payload.diff
    )

@app.get("/reviews/{timestamp}")
def get_review(timestamp: str):
    key = f"ai-pr-reviewer/prs/ai-pr-reviewer/{timestamp}/ai_review.json"

    try:
        data = read_json(key)
        return {
            "timestamp": timestamp,
            "review": data
        }
    except Exception:
        raise HTTPException(status_code=404, detail="Review not found")
@app.get("/reviews/{timestamp}/diff")
def download_diff(timestamp: str):
    key = f"ai-pr-reviewer/prs/ai-pr-reviewer/{timestamp}/diff.txt"

    try:
        response = s3.get_object(
            Bucket=BUCKET_NAME,
            Key=key
        )

        return StreamingResponse(
            response["Body"],
            media_type="text/plain",
            headers={
                "Content-Disposition": f"attachment; filename=diff-{timestamp}.txt"
            }
        )

    except Exception:
        raise HTTPException(status_code=404, detail="Diff file not found")

@app.get("/health")
def health():
    return {"status": "ok"}



    # 2️⃣ Save to S3 (new functionality – non-blocking)
    try:
        repo = "ai-pr-reviewer"
        pr_id = int(datetime.utcnow().timestamp())

        base_path = f"ai-pr-reviewer/prs/{repo}/{pr_id}"

        # Save diff
        save_text(
            f"{base_path}/diff.txt",
            payload.diff
        )

        # Save metadata
        save_json(
            f"{base_path}/metadata.json",
            {
                "title": payload.title,
                "description": payload.description,
                "reviewed_at": datetime.utcnow().isoformat()
            }
        )

        # Save AI review result
        save_json(
            f"{base_path}/ai_review.json",
            result
        )

    except Exception as e:
        # App must NOT crash if S3 fails
        print("⚠️ S3 upload failed:", e)

    # 3️⃣ Return response as usual
    return result
