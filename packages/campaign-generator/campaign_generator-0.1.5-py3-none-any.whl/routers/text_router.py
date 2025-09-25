from fastapi import APIRouter, HTTPException
from datetime import datetime

# local imports
from clickup_utils import fetch_clickup_task, update_clickup_task
from schemas import TextRequest
from settings import LocalSettings
from utils import (
    get_ollama_content_generation,
    get_ollama_models,
    get_ollama_summary,
    get_ollama_questions,
    get_ollama_transcript_cleanup,
    scrape_website_content,
    upload_file_from_bytes,
)

router = APIRouter(prefix="/text", tags=["text"])

@router.get("/models")
async def get_models():
    try:
        models = get_ollama_models()
        return {"models": [model.get("name") for model in models]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/summarize")
async def summarize_text(request: TextRequest):
    try:
        summary = get_ollama_summary(text=request.text, model=request.model)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.post("/questions")
# async def generate_questions(request: TextRequest):
#     try:
#         updated_file_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{request.file_name or 'uploaded_file'}.md"
#         questions = get_ollama_questions(text=request.text, model=request.model)
#         upload_file_from_bytes(
#             filename=updated_file_name,
#             data=questions.encode("utf-8"),
#         )
#         return {"questions": questions}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


@router.post("/transcript-cleanup")
async def cleanup_transcript(request: TextRequest):
    try:
        task = fetch_clickup_task(task_id="869akcv3p")
        system_prompt = task.get("text_content", "") if task else ""
    except Exception as e:
        system_prompt = ""
        print(f"Warning: Failed to fetch system prompt from ClickUp task: {e}")
    try:
        print(f"Chosen model: {request.model}")
        cleaned_text = get_ollama_transcript_cleanup(
            text=request.text, model=request.model, system_prompt=system_prompt
        )
        if request.task_id:
            try:
                update_clickup_task(
                    task_id=request.task_id,
                    status="phase 6. transcript clean",
                    description=cleaned_text,
                )
            except Exception as e:
                print(f"Warning: Failed to update ClickUp task {request.task_id}: {e}")

            try:
                file_name = f"{LocalSettings().transcripts_output_dir}/{request.task_id or 'unknown_task'}.txt"
                upload_file_from_bytes(
                    filename=file_name,
                    data=cleaned_text.encode("utf-8"),
                )
            except Exception as e:
                print(
                    f"Warning: Failed to upload cleaned transcript for task {request.task_id}: {e}"
                )
        return {"cleaned_text": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate-content")
async def generate_content(request: TextRequest):
    try:
        task = fetch_clickup_task(task_id="869akcv6d")
        system_prompt = task.get("text_content", "") if task else ""
    except Exception as e:
        system_prompt = ""
        print(f"Warning: Failed to fetch system prompt from ClickUp task: {e}")

    try:
        content = get_ollama_content_generation(
            prompt=request.text, model=request.model, system_prompt=system_prompt
        )

        if request.task_id:
            try:
                update_clickup_task(
                    task_id=request.task_id,
                    status="phase 7. challenge",
                    description=content,
                )
            except Exception as e:
                print(f"Warning: Failed to update ClickUp task {request.task_id}: {e}")

            try:
                file_name = f"{LocalSettings().content_generation_dir}/{request.task_id or 'unknown_task'}.txt"
                upload_file_from_bytes(
                    filename=file_name,
                    data=content.encode("utf-8"),
                )
            except Exception as e:
                print(
                    f"Warning: Failed to upload generated content for task {request.task_id}: {e}"
                )

        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.get("/scrape")
# async def scrape_website(url: str):
#     try:
#         content, final_url = await scrape_website_content(url)
#         content_to_upload = f"Source URL: {final_url}\n\n{content}"
#         upload_file_from_bytes(
#             filename=f"{final_url.split('//')[-1].replace('/', '_')}.txt",
#             data=content_to_upload.encode("utf-8"),
#         )
#         return {"content": content}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
