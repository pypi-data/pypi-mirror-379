from enum import Enum
from typing import List, Dict, Any, Optional
from pathlib import Path
import json
import subprocess

SESSIONS_FILE = Path.home() / ".kerberos" / "sessions.json"


class AgentType(Enum):
    DESIGNER = "designer"
    EXECUTOR = "executor"


class Session:
    def __init__(
        self,
        session_id: str,
        agent_type: AgentType,
        protocol=None,  # AgentProtocol instance
        source_path: str = "",
        work_path: Optional[str] = None,
        active: bool = False,
    ):
        self.session_id = session_id
        self.agent_type = agent_type
        self.protocol = protocol
        self.source_path = source_path
        self.work_path = work_path
        self.active = active
        self.children: List[Session] = []

    def start(self) -> bool:
        """Start the agent using the configured protocol"""
        if not self.protocol:
            return False
        return self.protocol.start(self)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize session to dictionary for JSON storage"""
        return {
            "session_id": self.session_id,
            "agent_type": self.agent_type.value,
            "source_path": self.source_path,
            "work_path": self.work_path,
            "children": [child.to_dict() for child in self.children],
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any], protocol=None) -> "Session":
        """Deserialize session from dictionary"""
        session = cls(
            session_id=data["session_id"],
            agent_type=AgentType(data["agent_type"]),
            protocol=protocol,
            source_path=data.get("source_path", ""),
            work_path=data.get("work_path"),
            active=data.get("active", False),
        )
        # Recursively load children (they inherit the same protocol)
        session.children = [
            cls.from_dict(child_data, protocol) for child_data in data.get("children", [])
        ]
        return session

    def prepare(self):
        """
        Uses git worktree. If worktree exists, use it. Otherwise create a new one on branch session_id.
        """
        if not self.source_path:
            raise ValueError("Source path is not set")

        # Set work_path in ~/.kerberos/worktrees/source_dir_name/session_id
        source_dir_name = Path(self.source_path).name
        worktree_base = Path.home() / ".kerberos" / "worktrees" / source_dir_name
        self.work_path = str(worktree_base / self.session_id)

        # Check if worktree already exists
        if Path(self.work_path).exists():
            return

        # Ensure worktree base directory exists
        worktree_base.mkdir(parents=True, exist_ok=True)

        # Create new worktree on a new branch
        try:
            # Check if branch exists
            result = subprocess.run(
                ["git", "rev-parse", "--verify", f"refs/heads/{self.session_id}"],
                cwd=self.source_path,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                # Branch exists, use it
                subprocess.run(
                    ["git", "worktree", "add", self.work_path, self.session_id],
                    cwd=self.source_path,
                    check=True,
                    capture_output=True,
                    text=True
                )
            else:
                # Create new branch
                subprocess.run(
                    ["git", "worktree", "add", "-b", self.session_id, self.work_path],
                    cwd=self.source_path,
                    check=True,
                    capture_output=True,
                    text=True
                )
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to create worktree: {e.stderr}")

    def spawn_executor(self, instructions: str, session_id: str) -> "Session":
        """Spawn an executor session as a child of this session"""
        if not self.work_path:
            raise ValueError("Work path is not set")

        new_session = Session(
            session_id=session_id,
            agent_type=AgentType.EXECUTOR,
            source_path=self.work_path,
        )

        self.children.append(new_session)
        return new_session

    @property
    def display_name(self) -> str:
        """Get display name for UI"""
        status = "●" if self.active else "○"
        return f"{status} {self.session_id}"


def load_sessions(protocol=None) -> List[Session]:
    """Load all sessions from JSON file"""
    if not SESSIONS_FILE.exists():
        return []

    try:
        with open(SESSIONS_FILE, "r") as f:
            data = json.load(f)
            return [Session.from_dict(session_data, protocol) for session_data in data]
    except (json.JSONDecodeError, KeyError):
        return []


def save_sessions(sessions: List[Session]) -> None:
    """Save all sessions to JSON file"""
    # Ensure directory exists
    SESSIONS_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(SESSIONS_FILE, "w") as f:
        json.dump([session.to_dict() for session in sessions], f, indent=2)


def find_session(sessions: List[Session], session_id: str) -> Optional[Session]:
    """Find a session by ID (searches recursively through children)"""
    for session in sessions:
        if session.session_id == session_id:
            return session
        # Search in children
        child_result = find_session(session.children, session_id)
        if child_result:
            return child_result
    return None