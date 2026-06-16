import re
import fitz
from transformers import pipeline


summarizer = None


def get_summarizer():
    global summarizer

    if summarizer is None:
        summarizer = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6"
        )

    return summarizer


def extract_text_from_pdf(pdf_path):
    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:
        page_text = page.get_text()
        if page_text:
            text += page_text + "\n"

    doc.close()

    text = re.sub(r"\s+", " ", text).strip()
    return text


def split_text(text, max_chars=2500):
    chunks = []

    for i in range(0, len(text), max_chars):
        chunk = text[i:i + max_chars]
        if len(chunk.strip()) > 300:
            chunks.append(chunk.strip())

    return chunks


def generate_pdf_summary(pdf_path):
    text = extract_text_from_pdf(pdf_path)

    if not text:
        return "No readable text found in this PDF."

    chunks = split_text(text)

    ai = get_summarizer()
    summaries = []

    for chunk in chunks[:6]:
        result = ai(
            chunk,
            max_length=140,
            min_length=40,
            do_sample=False
        )

        summaries.append(result[0]["summary_text"])

    final_summary = " ".join(summaries)

    if len(final_summary) > 3000:
        final_summary = final_summary[:3000] + "..."

    return final_summary