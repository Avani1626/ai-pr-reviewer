from storage.s3_client import save_text

save_text(
    "ai-pr-reviewer/test.txt",
    "S3 integration works from Python!"
)

print("Uploaded successfully")
