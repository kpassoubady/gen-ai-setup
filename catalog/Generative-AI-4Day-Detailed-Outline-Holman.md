# Generative AI: Prompt Engineering for Software Developers
## Detailed 4-Day Training Outline

### Daily Schedule Template

| Block | Duration | Notes |
| :---- | :---- | :---- |
| Session 1 (Morning - Part 1) | ~1 hr 45 min | |
| **Morning Break** | **15 min** | |
| Session 2 (Morning - Part 2) | ~1 hr 45 min | |
| **Lunch Break** | **45 min** | |
| Session 3 (Afternoon - Part 1) | ~1 hr 45 min | |
| **Evening Break** | **15 min** | |
| Session 4 (Afternoon - Part 2) | ~1 hr 30 min | Wrap-up + Q&A |

Total instructional time per day: ~6 hr 45 min

## DAY 1: Foundations of LLMs, NLP & OpenAI

Theme: Build a strong conceptual base. By end of day, every learner can call the OpenAI API and reason about model capabilities.

### Session 1: Introduction to Generative AI & LLMs (1 hr 45 min)
- Welcome, learner introductions, course objectives, lab environment check
- Evolution of AI → Machine Learning → Deep Learning → Generative AI
- What are Large Language Models (LLMs)? Transformer architecture (high-level)
- Tokenization, embeddings, context window, attention (intuitive overview)
- Landscape of models: GPT-4/4o, Claude, Gemini, Llama, Mistral (open vs closed)
- NLP refresher: classification, NER, summarization, generation
- **Demo:** Tokenizer visualization using `tiktoken`

### Session 2: Working with LLM APIs: Hands-on Setup (1 hr 45 min)
- LLM provider accounts (OpenAI / Gemini / Claude), API keys, billing & rate limits
- Installing `litellm` and the provider-agnostic SDK setup
- First API call via `shared/llm_client.py` (works with any provider)
- Anatomy of a request: `model`, `messages`, `role` (system/user/assistant)
- Anatomy of a response: choices, usage, finish_reason
- **Lab 1.1:** "Hello LLM", make 5 API calls with different prompts and log responses
- **Lab 1.2:** Build a simple Q&A script that takes user input from the CLI

### Session 3: Model Capabilities, Limitations & Input Preparation (1 hr 45 min)
- What LLMs do well: summarization, code generation, classification, rewriting
- Where LLMs fail: hallucinations, math, recent events, deterministic logic
- Knowledge cutoff and context window limits
- Input data preprocessing: cleaning text, removing PII, chunking long inputs
- Token counting and cost estimation with `tiktoken`
- Choosing the right model for the task (capability vs cost tradeoff)
- **Demo:** Same prompt across mini vs default tier, compare quality and cost across providers

### Session 4: Hands-on Lab + Day 1 Wrap-up (1 hr 30 min)
- **Lab 1.3:** Build a "Code Explainer", paste a Python function, get a plain-English explanation
- **Lab 1.4:** Build a "Bug Triager", given an error log, classify severity
- Code walkthrough and peer review
- Day 1 recap, Q&A, preview of Day 2

## DAY 2: Prompt Engineering Deep Dive

Theme: Move from "it works" to "it works reliably." Master the craft of writing, structuring, and iterating on prompts.

### Session 1: Prompt Engineering Fundamentals (1 hr 45 min)
- What makes a prompt "good"? Clarity, specificity, context, constraints
- The 4 building blocks: Instruction, Context, Input Data, Output Format
- Defining clear goals and expected outputs before writing the prompt
- Common anti-patterns: vague instructions, leading questions, conflicting constraints
- The role of the `system` message vs `user` message
- **Demo:** Rewriting a bad prompt into a strong prompt, 5 iterations live

### Session 2: Prompting Techniques (1 hr 45 min)
- **Zero-shot** prompting: direct instruction
- **Few-shot** prompting: guiding with examples
- **Chain-of-Thought (CoT):** "think step by step"
- **Role prompting:** "You are an expert Python reviewer..."
- **Structured output:** JSON mode, function/tool calling basics
- Delimiters, headers, and formatting to reduce ambiguity
- **Lab 2.1:** Build a sentiment classifier with zero-shot, then improve with few-shot
- **Lab 2.2:** Force JSON output for a "resume parser" use case

### Session 3: API Parameters & Controlling Output (1 hr 45 min)
- `temperature`: creativity vs determinism
- `top_p`, `frequency_penalty`, `presence_penalty`
- `max_tokens`: controlling response length
- `stop` sequences for clean termination
- `seed` for reproducibility
- Streaming responses for better UX
- **Lab 2.3:** Generate marketing taglines at temperature 0.2, 0.7, and 1.2, then compare
- **Lab 2.4:** Build a streaming chat loop in the terminal

### Session 4: Iteration, Refinement & Lab (1 hr 30 min)
- Prompt iteration loop: write → test → analyze → refine
- Evaluating outputs: manual rubrics, golden datasets, LLM-as-judge (intro)
- Versioning prompts in code (prompt templates, configuration files)
- **Lab 2.5:** "Refactor Assistant", given messy Python code, return clean refactored code with explanation. Iterate the prompt 3 times based on observed failures.
- Day 2 recap, Q&A

## DAY 3: Building Custom Chatbots & RAG

Theme: Move from single-shot prompts to conversational, knowledge-grounded applications.

### Session 1: Conversation Context & Multi-turn Design (1 hr 45 min)
- Stateless API + stateful conversations: how to bridge the gap
- Maintaining conversation history (message list management)
- Context window limits: truncation, summarization, sliding window strategies
- Defining chatbot purpose, persona, and audience
- Conversation flow design: intents, fallbacks, escalation
- **Lab 3.1:** Build a multi-turn chatbot that remembers user name and preferences across turns

### Session 2: Retrieval-Augmented Generation (RAG) Fundamentals (1 hr 45 min)
- The hallucination problem and why RAG helps
- RAG architecture: ingestion → embedding → vector store → retrieval → generation
- Embedding models (OpenAI `text-embedding-3-small`, Gemini `embedding-001`, etc.)
- Vector databases: FAISS (local), Chroma, Pinecone (cloud). When to use which
- Chunking strategies: fixed size, semantic, overlap considerations
- Similarity search: cosine similarity, top-k retrieval
- **Demo:** Embed 5 sentences, query with a related question, visualize distance scores

### Session 3: Building a RAG-powered Chatbot (1 hr 45 min)
- **Lab 3.2:** End-to-end RAG mini-project
  - Ingest a small knowledge base (PDF/markdown docs)
  - Chunk and embed using OpenAI embeddings
  - Store in a local FAISS or Chroma index
  - Build a query loop: retrieve top-k chunks, inject into prompt, generate answer
  - Cite sources in the response
- Discussion: when RAG is the right answer vs fine-tuning vs prompt engineering only

### Session 4: Integration, Channels & Lab (1 hr 30 min)
- Integration patterns: REST API wrappers, web frontends (brief), Slack/Teams bots (concept)
- Handling common queries: FAQ caching, deterministic shortcuts
- Error handling: API failures, rate limits, malformed responses
- **Lab 3.3:** Wrap the RAG chatbot from Lab 3.2 in a simple Flask/FastAPI endpoint
- Day 3 recap, Q&A

## DAY 4: Production Best Practices, Ethics & Capstone

Theme: Make it production-ready. Security, cost, ethics, observability, and a capstone tying it all together.

### Session 1: Security & Responsible LLM Application Design (1 hr 45 min)
- API key management: secrets, env vars, vaults. Never commit keys
- Prompt injection attacks: what they are, examples, defenses
- Data privacy: PII, GDPR, data retention with OpenAI APIs
- Output validation and sanitization (especially when LLM output drives actions)
- Guardrails: input filters, output filters, content moderation API
- **Demo:** A live prompt injection attempt and how to defend against it
- **Lab 4.1:** Add an input/output moderation layer to the Day 3 chatbot

### Session 2: Cost, Latency & Error Handling (1 hr 45 min)
- Token economics: input vs output token cost, model price tiers
- Cost optimization patterns: caching, smaller models for simple tasks, response truncation
- Latency strategies: streaming, parallel calls, model selection
- Retry logic, exponential backoff, handling 429/500 errors
- Monitoring API usage and setting spending alerts
- **Lab 4.2:** Add caching (in-memory or Redis-style) for repeated queries; measure savings

### Session 3: Ethics, Bias Mitigation & Monitoring (1 hr 45 min)
- Sources of bias in LLM outputs and real-world consequences
- Bias detection techniques and mitigation prompts
- Ethical guidelines: when not to use LLMs (high-stakes decisions, legal/medical advice)
- Human-in-the-loop design patterns
- Monitoring model performance over time: logging, evaluations, drift detection
- Setting up an evaluation harness (golden dataset + automated scoring)
- **Lab 4.3:** Build a small eval script, run 10 test prompts, compare outputs to expected, log pass/fail

### Session 4: Capstone Project + Course Wrap-up (1 hr 30 min)
- **Capstone Lab:** Each learner builds (or extends) a small AI-powered developer assistant of their choice:
  - Option A: Code review assistant with RAG over team coding standards
  - Option B: Documentation Q&A bot
  - Option C: Bug-report triager that classifies and routes issues
  - Must demonstrate: prompt engineering, conversation context OR RAG, error handling, basic eval
- Brief learner demos (5 min each)
- Course recap: what was learned, where to go next
- Resources: papers, blogs, communities, certifications
- Final Q&A and feedback

## Materials & Setup Checklist

For instructor to send before Day 1:
- Python 3.11+ installed (3.12 recommended)
- VS Code with AI coding assistant extension (Copilot, Cursor, Windsurf, or Claude Code)
- At least one LLM API key: OpenAI, Google Gemini, or Anthropic Claude (with ~$5 credit)
- Git installed
- Required packages: `litellm`, `openai`, `tiktoken`, `python-dotenv`, `google-generativeai`, `anthropic`, `faiss-cpu` or `chromadb`, `flask` or `fastapi`, `numpy`, `requests`, `jupyter`
- See `install/install.md` for OS-specific guides and `requirements.txt` for versions
