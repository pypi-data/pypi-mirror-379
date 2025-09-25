"""
Kerberos Backend Server - FastAPI application for session management
"""
from __future__ import annotations
import os
from pathlib import Path
from typing import List, Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from .sessions import Session, AgentType, load_sessions, save_sessions
from .tmux_agent import TmuxProtocol
from .logger import get_logger

logger = get_logger(__name__)


# Pydantic models for API
class SessionCreate(BaseModel):
    session_id: str
    source_path: Optional[str] = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown logic"""
    # Initialize app state
    app.state.agent = TmuxProtocol(default_command="claude")

    # Load existing sessions on startup
    logger.info("Loading existing sessions")
    app.state.sessions = load_sessions(protocol=app.state.agent)

    yield

    # Save sessions on shutdown
    logger.info("Saving sessions on shutdown")
    save_sessions(app.state.sessions)


# Create FastAPI app
app = FastAPI(lifespan=lifespan)


@app.post("/sessions")
async def create_session(request: SessionCreate):
    """Create a new session"""
    # Check if session already exists
    if any(s.session_id == request.session_id for s in state.sessions):
        raise HTTPException(status_code=400, detail=f"Session {request.session_id} already exists")

    # Use current directory if source_path not provided
    source_path = request.source_path or str(Path.cwd())

    # Create session
    new_session = Session(
        session_id=request.session_id,
        agent_type=AgentType.DESIGNER,
        protocol=state.agent,
        source_path=source_path,
        active=False
    )

    try:
        # Prepare git worktree
        logger.info(f"Preparing worktree for session {request.session_id}")
        new_session.prepare()
        logger.info(f"Worktree prepared at: {new_session.work_path}")

        # Start tmux session
        logger.info(f"Starting session {request.session_id}")
        result = new_session.start()

        if not result:
            raise HTTPException(status_code=500, detail="Failed to start tmux session")

        # Add to sessions list
        state.sessions.append(new_session)
        save_sessions(state.sessions)

        return {
            "session_id": new_session.session_id,
            "work_path": new_session.work_path,
            "success": True
        }

    except Exception as e:
        logger.error(f"Failed to create session: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/sessions")
async def list_sessions():
    """List all sessions"""
    # Update active status from tmux
    for session in state.sessions:
        status = state.agent.get_status(session.session_id)
        session.active = status.get("attached", False)

    save_sessions(state.sessions)

    return [
        {
            "session_id": s.session_id,
            "active": s.active,
            "work_path": s.work_path
        }
        for s in state.sessions
    ]


def run_server(host: str = "127.0.0.1", port: int = 8765):
    """Run the FastAPI server"""
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run_server()
