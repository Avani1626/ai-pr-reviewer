from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from ai_reviewer import ai_review_pr
from storage.s3_client import save_text, save_json
from storage.s3_client import read_json, s3, BUCKET_NAME
from fastapi import HTTPException
from fastapi.responses import StreamingResponse

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger("ai-pr-reviewer")


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


@app.get("/health")
def health():
    logger.info("Health check endpoint called")
    return {"status": "ok"}



@app.post("/review")
def review_pr(payload: PRPayload):
    logger.info("PR review request received")

    # 1️⃣ Run AI review
    try:
        result = ai_review_pr(
            payload.title,
            payload.description,
            payload.diff
        )
        logger.info("AI review completed successfully")
    except Exception as e:
        logger.error(f"AI review failed: {str(e)}")
        raise HTTPException(status_code=500, detail="AI review failed")

    # 2️⃣ Save results to S3
    try:
        repo = "ai-pr-reviewer"
        pr_id = int(datetime.utcnow().timestamp())

        base_path = f"ai-pr-reviewer/prs/{repo}/{pr_id}"

        logger.info(f"Uploading PR data to S3 at path: {base_path}")

        save_text(
            f"{base_path}/diff.txt",
            payload.diff
        )

        save_json(
            f"{base_path}/metadata.json",
            {
                "title": payload.title,
                "description": payload.description,
                "reviewed_at": datetime.utcnow().isoformat()
            }
        )

        save_json(
            f"{base_path}/ai_review.json",
            result
        )

        logger.info("S3 upload completed successfully")

    except Exception as e:
        logger.error(f"S3 upload failed: {str(e)}")

    # 3️⃣ Return response
    return result
