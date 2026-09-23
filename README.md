# Zoology MCQ Generator

An LLM-powered pipeline that converts Zoology textbook chapters into
high-quality, exam-ready multiple-choice questions using Google's Gemini API.

## What It Does

- **Reads** a cleaned Markdown version of a textbook chapter
- **Splits** it into semantically meaningful chunks (Markdown-aware)
- **Generates** up to 5 MCQs per chunk using Gemini 3.5 Flash-Lite
- **Structures** output with Pydantic schemas (guaranteed valid JSON)
- **Retries** transient errors (503, rate limits) with exponential backoff
- **Saves** results in both JSON (grouped by chunk) and JSONL (one MCQ per line)

## Key Features

- **Strict grounding** — questions are generated ONLY from the provided
  chunk text; no outside knowledge is used
- **Schema-enforced output** — Pydantic models guarantee 4 options (A–D),
  one correct answer, and a brief explanation per question
- **Distractor quality rules** — the prompt forces wrong options to come
  from the same conceptual category as the correct answer
- **Difficulty labeling** — each question is tagged EASY / MEDIUM / HARD
- **Traceability** — every question is linked back to its source chunk
- **Free-tier friendly** — designed to work within Gemini's free API limits

## Tech Stack

| Layer | Tool |
|-------|------|
| LLM | Google Gemini 3.5 Flash-Lite |
| SDK | `google-genai` |
| Schema | Pydantic |
| Chunking | LangChain `MarkdownTextSplitter` |
| Environment | Jupyter Notebook / Python 3.10+ |

