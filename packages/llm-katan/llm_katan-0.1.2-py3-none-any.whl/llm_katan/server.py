"""
FastAPI server implementation for yLLM

Provides OpenAI-compatible endpoints for lightweight LLM serving.

Signed-off-by: Yossi Ovadia <yovadia@redhat.com>
"""

import asyncio
import json
import logging
from contextlib import asynccontextmanager
from typing import Dict, List, Optional, Union

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from .config import ServerConfig
from .model import ModelBackend, create_backend

logger = logging.getLogger(__name__)


# Pydantic models for request/response
class ChatMessage(BaseModel):
    role: str
    content: str


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    max_tokens: Optional[int] = None
    temperature: Optional[float] = None
    stream: Optional[bool] = False


class ChatCompletionResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[Dict]
    usage: Optional[Dict] = None


class ModelInfo(BaseModel):
    id: str
    object: str
    created: int
    owned_by: str


class ModelsResponse(BaseModel):
    object: str = "list"
    data: List[ModelInfo]


class HealthResponse(BaseModel):
    status: str
    model: str
    backend: str


# Global backend instance
backend: Optional[ModelBackend] = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    global backend
    config = app.state.config

    logger.info(f"Starting yLLM server with model: {config.model_name}")
    logger.info(f"Backend: {config.backend}")
    logger.info(f"Served model name: {config.served_model_name}")

    # Create and load model backend
    backend = create_backend(config)
    await backend.load_model()

    logger.info("yLLM server started successfully")
    yield

    logger.info("Shutting down yLLM server")
    backend = None


def create_app(config: ServerConfig) -> FastAPI:
    """Create FastAPI application"""
    app = FastAPI(
        title="yLLM - Lightweight LLM Server",
        description="A lightweight LLM serving package for testing and development",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    # Store config in app state
    app.state.config = config

    @app.get("/health", response_model=HealthResponse)
    async def health():
        """Health check endpoint"""
        return HealthResponse(
            status="ok",
            model=config.served_model_name,
            backend=config.backend,
        )

    @app.get("/v1/models", response_model=ModelsResponse)
    async def list_models():
        """List available models"""
        if backend is None:
            raise HTTPException(status_code=503, detail="Model not loaded")

        model_info = backend.get_model_info()
        return ModelsResponse(data=[ModelInfo(**model_info)])

    @app.post("/v1/chat/completions")
    async def chat_completions(request: ChatCompletionRequest):
        """Chat completions endpoint (OpenAI compatible)"""
        if backend is None:
            raise HTTPException(status_code=503, detail="Model not loaded")

        try:
            # Convert messages to dict format
            messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]

            if request.stream:
                # Streaming response
                async def generate_stream():
                    async for chunk in backend.generate(
                        messages=messages,
                        max_tokens=request.max_tokens,
                        temperature=request.temperature,
                        stream=True,
                    ):
                        yield f"data: {json.dumps(chunk)}\n\n"
                    yield "data: [DONE]\n\n"

                return StreamingResponse(
                    generate_stream(),
                    media_type="text/plain",
                    headers={"Cache-Control": "no-cache", "Connection": "keep-alive"},
                )
            else:
                # Non-streaming response
                response_generator = backend.generate(
                    messages=messages,
                    max_tokens=request.max_tokens,
                    temperature=request.temperature,
                    stream=False,
                )
                response = await response_generator.__anext__()
                return response

        except Exception as e:
            logger.error(f"Error in chat completions: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))

    @app.get("/")
    async def root():
        """Root endpoint"""
        return {
            "message": "yLLM - Lightweight LLM Server",
            "version": "0.1.0",
            "model": config.served_model_name,
            "backend": config.backend,
            "docs": "/docs",
        }

    return app


async def run_server(config: ServerConfig):
    """Run the server with uvicorn"""
    import uvicorn

    app = create_app(config)

    uvicorn_config = uvicorn.Config(
        app,
        host=config.host,
        port=config.port,
        log_level="info",
        access_log=True,
    )

    server = uvicorn.Server(uvicorn_config)
    await server.serve()