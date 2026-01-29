---
title: Article Writing Crew
emoji: ✍️
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 5.12.0
app_file: app.py
pinned: false
---

# Article Writing Crew

[![Live Demo](https://img.shields.io/badge/Live%20Demo-HuggingFace%20Spaces-blue)](https://huggingface.co/spaces/davidleocadio94DLAI/multi-ai-agent-systems-with-crewai_article-writing-crew)
[![Python](https://img.shields.io/badge/Python-3.10+-green)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.28.8-orange)](https://crewai.com)

A multi-agent AI system that collaborates to create professional blog articles. Three specialized agents work together: a Content Planner researches trends, a Content Writer crafts the article, and an Editor polishes the final piece.

## Features

- **Multi-Agent Collaboration** - Three AI agents with distinct roles working together
- **Research-Driven Content** - Content Planner identifies trends and key information
- **SEO Optimization** - Articles include relevant keywords and structure
- **Professional Editing** - Final review for quality and style consistency

## Tech Stack

![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--Turbo-412991)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-FF6B6B)
![Gradio](https://img.shields.io/badge/Gradio-UI-F97316)

## Getting Started

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation

```bash
# Clone the repository
git clone https://github.com/davidleocadio94/multi-ai-agent-systems-with-crewai_article-writing-crew.git
cd multi-ai-agent-systems-with-crewai_article-writing-crew

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### Run Locally

```bash
# Set your API key
export OPENAI_API_KEY=your-api-key

# Run the app
python app.py
```

Open http://localhost:7860 in your browser.

### Run with Docker

```bash
# Build the image
docker build -t article-writing-crew .

# Run the container
docker run -p 7860:7860 -e OPENAI_API_KEY=your-api-key article-writing-crew
```

Open http://localhost:7860 in your browser.

## How It Works

1. **Content Planner Agent** - Researches the topic, identifies target audience, creates outline with SEO keywords
2. **Content Writer Agent** - Uses the plan to craft a compelling blog post with engaging structure
3. **Editor Agent** - Reviews for grammar, style consistency, and journalistic best practices

## Example Topics

- "Artificial Intelligence in Healthcare"
- "The Future of Remote Work"
- "Sustainable Technology Trends"
- "Cybersecurity Best Practices"

---

Built as part of the [Multi AI Agent Systems with CrewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) course on DeepLearning.AI
