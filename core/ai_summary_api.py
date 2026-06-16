import os
import re
import fitz
from openai import OpenAI


def get_openai_client():
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        return None

    return OpenAI(api_key=api_key)


def extract_text_from_pdf(pdf_path):
    text = ""

    try:
        doc = fitz.open(pdf_path)

        for page in doc:
            page_text = page.get_text()
            if page_text:
                text += page_text + "\n"

        doc.close()

    except Exception:
        return ""

    text = re.sub(r"\s+", " ", text).strip()
    return text


def split_text(text, max_chars=9000):
    chunks = []

    for i in range(0, len(text), max_chars):
        chunk = text[i:i + max_chars].strip()

        if len(chunk) > 300:
            chunks.append(chunk)

    return chunks


def ask_openai_for_summary(text):
    client = get_openai_client()

    if client is None:
        return "OpenAI API key is missing. Add OPENAI_API_KEY in Render environment variables."

    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    response = client.responses.create(
        model=model,
        input=[
            {
                "role": "system",
                "content": (
                    "You are StudyMate, an assistant that creates clear study summaries. "
                    "Summarize the text in simple language. "
                    "Use bullet points, keep the most important concepts, and write in English."
                )
            },
            {
                "role": "user",
                "content": f"Create a study summary from this PDF text:\n\n{text}"
            }
        ]
    )

    return response.output_text.strip()


def generate_pdf_summary_with_api(pdf_path):
    text = extract_text_from_pdf(pdf_path)

    if not text:
        return "No readable text found in this PDF."

    chunks = split_text(text)

    if not chunks:
        return "The PDF text is too short to generate a summary."

    partial_summaries = []

    for chunk in chunks[:5]:
        summary = ask_openai_for_summary(chunk)
        partial_summaries.append(summary)

    if len(partial_summaries) == 1:
        return partial_summaries[0]

    final_text = "\n\n".join(partial_summaries)

    final_summary = ask_openai_for_summary(
        "Create one final clean summary from these partial summaries:\n\n" + final_text
    )

    return final_summary