# LLM Katan - Lightweight LLM Server for Testing

A lightweight LLM serving package using FastAPI and HuggingFace transformers, designed for testing and development with real tiny models.

## Features

- 🚀 **FastAPI-based**: High-performance async web server
- 🤗 **HuggingFace Integration**: Real model inference with transformers
- ⚡ **Tiny Models**: Ultra-lightweight models for fast testing (Qwen3-0.6B, etc.)
- 🔄 **Multi-Instance**: Run same model on different ports with different names
- 🎯 **OpenAI Compatible**: Drop-in replacement for OpenAI API endpoints
- 📦 **PyPI Ready**: Easy installation and distribution
- 🛠️ **vLLM Support**: Optional vLLM backend for production-like performance

## Quick Start

### Installation

```bash
pip install llm-katan
```

### Basic Usage

```bash
# Start server with a tiny model
llm-katan --model Qwen/Qwen3-0.6B --port 8000

# Start with custom served model name
llm-katan --model Qwen/Qwen3-0.6B --port 8001 --served-model-name "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# With vLLM backend (optional)
llm-katan --model Qwen/Qwen3-0.6B --port 8000 --backend vllm
```

### Multi-Instance Testing

```bash
# Terminal 1: Qwen endpoint
llm-katan --model Qwen/Qwen3-0.6B --port 8000 --served-model-name "Qwen/Qwen2-0.5B-Instruct"

# Terminal 2: Same model, different name
llm-katan --model Qwen/Qwen3-0.6B --port 8001 --served-model-name "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
```

## API Endpoints

- `GET /health` - Health check
- `GET /v1/models` - List available models
- `POST /v1/chat/completions` - Chat completions (OpenAI compatible)

## Use Cases

- **Testing**: Lightweight alternative to full LLM deployments
- **Development**: Fast iteration with real model behavior
- **CI/CD**: Automated testing with actual inference
- **Prototyping**: Quick setup for AI application development

## Configuration

### Command Line Options

```bash
llm-katan --help
```

### Environment Variables

- `LLM_KATAN_MODEL`: Default model to load
- `LLM_KATAN_PORT`: Default port (8000)
- `LLM_KATAN_BACKEND`: Backend type (transformers|vllm)

## Development

```bash
# Clone and install in development mode
git clone <repo>
cd e2e-tests/llm-katan
pip install -e .

# Run with development dependencies
pip install -e ".[dev]"
```

## License

MIT License

## Contributing

Contributions welcome! Please see the main repository for guidelines.

---

*Part of the semantic-router project ecosystem*