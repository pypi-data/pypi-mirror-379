"""Main Telegram adapter for AgentryLab integration."""

from __future__ import annotations

import asyncio
import logging
import uuid
from typing import Any, AsyncIterator, Dict, List, Optional, Tuple

from agentrylab import init
from agentrylab.lab import Lab

from .exceptions import (
    ConversationAlreadyExistsError,
    ConversationNotFoundError,
    ConversationNotActiveError,
    InvalidPresetError,
    StreamingError,
)
from .models import (
    ConversationEvent,
    ConversationState,
    ConversationStatus,
    UserMessage,
)

logger = logging.getLogger(__name__)


def _validate_conversation_exists(adapter_instance, conversation_id: str) -> ConversationState:
    """Helper to validate conversation exists and return its state.
    
    Args:
        adapter_instance: The TelegramAdapter instance
        conversation_id: ID of the conversation
        
    Returns:
        The conversation state
        
    Raises:
        ConversationNotFoundError: If conversation is not found
    """
    if conversation_id not in adapter_instance._conversations:
        raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
    return adapter_instance._conversations[conversation_id]


def _validate_conversation_active(state: ConversationState) -> None:
    """Helper to validate conversation is active.
    
    Args:
        state: The conversation state
        
    Raises:
        ConversationNotActiveError: If conversation is not active
    """
    if state.status != ConversationStatus.ACTIVE:
        raise ConversationNotActiveError(f"Conversation {state.conversation_id} is not active")


class TelegramAdapter:
    """Adapter for integrating AgentryLab with external interfaces like Telegram.
    
    This class provides a clean API for managing conversations, streaming events,
    and handling user input in real-time.
    """
    
    def __init__(self, *, max_concurrent_conversations: int = 100):
        """Initialize the Telegram adapter.
        
        Args:
            max_concurrent_conversations: Maximum number of concurrent conversations
        """
        self.max_concurrent_conversations = max_concurrent_conversations
        self._conversations: Dict[str, ConversationState] = {}
        self._event_streams: Dict[str, asyncio.Queue] = {}
        self._user_message_queues: Dict[str, asyncio.Queue] = {}
        self._running_tasks: Dict[str, asyncio.Task] = {}
        
    def start_conversation(
        self, 
        preset_id: str, 
        topic: str, 
        user_id: str,
        conversation_id: Optional[str] = None,
        resume: bool = True,
        user_params: Optional[Dict[str, Any]] = None,
    ) -> str:
        """Start a new conversation.
        
        Args:
            preset_id: ID of the preset to use
            topic: Topic for the conversation
            user_id: ID of the user starting the conversation
            conversation_id: Optional custom conversation ID
            resume: Whether to resume from existing checkpoint if available
            
        Returns:
            The conversation ID
            
        Raises:
            ConversationAlreadyExistsError: If conversation ID already exists
            InvalidPresetError: If preset is not found or invalid
        """
        if conversation_id is None:
            conversation_id = str(uuid.uuid4())
            
        if conversation_id in self._conversations:
            raise ConversationAlreadyExistsError(f"Conversation {conversation_id} already exists")
            
        if len(self._conversations) >= self.max_concurrent_conversations:
            raise RuntimeError("Maximum concurrent conversations reached")
            
        try:
            # Attempt to initialize; if preset declares user_inputs and not satisfied,
            # defer to collecting state. The init() will load YAML; we pass through
            # user_params by formatting a minimal override when provided.
            from pathlib import Path
            import yaml as _yaml
            preset_path = Path(preset_id)
            raw = _yaml.safe_load(preset_path.read_text(encoding="utf-8")) if preset_path.exists() else {}
            user_inputs = raw.get("user_inputs") if isinstance(raw, dict) else None

            # Helper to substitute ${user_inputs.key}
            def _subst(obj: Any, vals: Dict[str, Any]) -> Any:
                if isinstance(obj, str):
                    for k, v in vals.items():
                        token = f"${{user_inputs.{k}}}"
                        if token in obj:
                            obj = obj.replace(token, str(v))
                    return obj
                if isinstance(obj, list):
                    return [_subst(x, vals) for x in obj]
                if isinstance(obj, dict):
                    return {kk: _subst(vv, vals) for kk, vv in obj.items()}
                return obj

            collected: Dict[str, Any] = dict(user_params or {})
            missing: List[str] = []
            if isinstance(user_inputs, dict):
                for k, spec in user_inputs.items():
                    if k in collected:
                        continue
                    if (spec or {}).get("required", False) and (spec or {}).get("default") is None:
                        missing.append(k)

            if missing:
                # Create conversation in COLLECTING state
                state = ConversationState(
                    conversation_id=conversation_id,
                    preset_id=preset_id,
                    topic=topic,
                    user_id=user_id,
                    status=ConversationStatus.COLLECTING,
                    lab_instance=None,
                    metadata={"user_inputs_missing": missing, "collected": collected},
                )
                self._conversations[conversation_id] = state
                self._event_streams[conversation_id] = asyncio.Queue()
                self._user_message_queues[conversation_id] = asyncio.Queue()
                logger.info(
                    f"Conversation {conversation_id} awaiting params: {', '.join(missing)}"
                )
                return conversation_id

            # If nothing missing, substitute and init Lab
            if isinstance(raw, dict) and collected:
                raw = _subst(raw, collected)
            lab = init(
                raw if isinstance(raw, dict) else preset_id,
                experiment_id=conversation_id,
                prompt=topic,
                resume=resume,
            )
            
            # Create conversation state
            state = ConversationState(
                conversation_id=conversation_id,
                preset_id=preset_id,
                topic=topic,
                user_id=user_id,
                status=ConversationStatus.ACTIVE,
                lab_instance=lab,
            )
            
            # Store conversation
            self._conversations[conversation_id] = state
            
            # Create event stream and user message queue
            self._event_streams[conversation_id] = asyncio.Queue()
            self._user_message_queues[conversation_id] = asyncio.Queue()
            
            # Note: Conversation task will be started when first accessed via async methods
            
            logger.info(f"Started conversation {conversation_id} with preset {preset_id}")
            return conversation_id
            
        except Exception as e:
            logger.error(f"Failed to start conversation {conversation_id}: {e}")
            raise InvalidPresetError(f"Failed to initialize preset {preset_id}: {e}")

    def provide_user_param(self, conversation_id: str, key: str, value: Any) -> List[str]:
        """Provide one user_input parameter for a COLLECTING conversation.

        Returns the list of remaining missing keys after applying this value.
        """
        state = _validate_conversation_exists(self, conversation_id)
        if state.status != ConversationStatus.COLLECTING:
            return []
        meta = state.metadata or {}
        collected = meta.get("collected", {})
        collected[key] = value
        meta["collected"] = collected
        missing = [k for k in (meta.get("user_inputs_missing") or []) if k != key]
        meta["user_inputs_missing"] = missing
        state.metadata = meta
        return missing

    def finalize_params_and_start(self, conversation_id: str) -> None:
        """When all params are provided, initialize the Lab and switch to ACTIVE."""
        state = _validate_conversation_exists(self, conversation_id)
        if state.status != ConversationStatus.COLLECTING:
            return
        try:
            import yaml as _yaml
            from pathlib import Path
            preset_path = Path(state.preset_id)
            raw = _yaml.safe_load(preset_path.read_text(encoding="utf-8")) if preset_path.exists() else {}
            collected = (state.metadata or {}).get("collected", {})

            # Substitute
            def _subst(obj: Any, vals: Dict[str, Any]) -> Any:
                if isinstance(obj, str):
                    for k, v in vals.items():
                        token = f"${{user_inputs.{k}}}"
                        if token in obj:
                            obj = obj.replace(token, str(v))
                    return obj
                if isinstance(obj, list):
                    return [_subst(x, vals) for x in obj]
                if isinstance(obj, dict):
                    return {kk: _subst(vv, vals) for kk, vv in obj.items()}
                return obj

            if isinstance(raw, dict) and collected:
                raw = _subst(raw, collected)

            lab = init(
                raw if isinstance(raw, dict) else state.preset_id,
                experiment_id=conversation_id,
                prompt=state.topic,
                resume=True,
            )
            state.lab_instance = lab
            state.status = ConversationStatus.ACTIVE
            # ensure queues exist
            if conversation_id not in self._event_streams:
                self._event_streams[conversation_id] = asyncio.Queue()
            if conversation_id not in self._user_message_queues:
                self._user_message_queues[conversation_id] = asyncio.Queue()
        except Exception as e:
            logger.error(f"Failed to finalize params for conversation {conversation_id}: {e}")
            state.status = ConversationStatus.ERROR
    
    def get_conversation_state(self, conversation_id: str) -> ConversationState:
        """Get the state of a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            The conversation state
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        return _validate_conversation_exists(self, conversation_id)
    
    def can_resume_conversation(self, conversation_id: str) -> bool:
        """Check if a conversation can be resumed from checkpoint.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            True if conversation can be resumed, False otherwise
        """
        try:
            # Try to load checkpoint to see if it exists
            from agentrylab.persistence.store import Store
            store = Store()
            snapshot = store.load_checkpoint(conversation_id)
            return isinstance(snapshot, dict) and snapshot and "_pickled" not in snapshot
        except Exception:
            return False
    
    def post_user_message(self, conversation_id: str, message: str, user_id: str) -> None:
        """Post a user message to a conversation.
        
        Args:
            conversation_id: ID of the conversation
            message: The user message
            user_id: ID of the user
            
        Raises:
            ConversationNotFoundError: If conversation is not found
            ConversationNotActiveError: If conversation is not active
        """
        state = _validate_conversation_exists(self, conversation_id)
        _validate_conversation_active(state)
            
        # Create user message
        user_msg = UserMessage(
            conversation_id=conversation_id,
            user_id=user_id,
            content=message,
        )
        
        # Ensure conversation task is started
        self._ensure_conversation_task_started(conversation_id)
        
        # Add to queue
        try:
            self._user_message_queues[conversation_id].put_nowait(user_msg)
            logger.info(f"Posted user message to conversation {conversation_id}")
        except asyncio.QueueFull:
            logger.warning(f"User message queue full for conversation {conversation_id}")
            raise RuntimeError("User message queue is full")
    
    def _ensure_conversation_task_started(self, conversation_id: str) -> None:
        """Ensure the conversation task is started.
        
        Args:
            conversation_id: ID of the conversation
        """
        if conversation_id not in self._running_tasks:
            try:
                # Check if we're in an async context
                loop = asyncio.get_running_loop()
                task = loop.create_task(self._run_conversation(conversation_id))
                self._running_tasks[conversation_id] = task
            except RuntimeError:
                # No event loop running, task will be started later
                pass

    async def stream_events(self, conversation_id: str) -> AsyncIterator[ConversationEvent]:
        """Stream events from a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Yields:
            Conversation events
            
        Raises:
            ConversationNotFoundError: If conversation is not found
            StreamingError: If streaming fails
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        if conversation_id not in self._event_streams:
            raise StreamingError(f"No event stream for conversation {conversation_id}")
            
        # Ensure conversation task is started
        self._ensure_conversation_task_started(conversation_id)
            
        event_queue = self._event_streams[conversation_id]
        
        try:
            while True:
                # Check if conversation is still active
                state = self._conversations.get(conversation_id)
                if not state or state.status in [ConversationStatus.STOPPED, ConversationStatus.ERROR]:
                    break
                    
                try:
                    # Wait for next event with timeout
                    event = await asyncio.wait_for(event_queue.get(), timeout=1.0)
                    yield event
                    
                    # Mark task as done
                    event_queue.task_done()
                    
                except asyncio.TimeoutError:
                    # Send heartbeat to keep connection alive
                    continue
                    
        except Exception as e:
            logger.error(f"Error streaming events for conversation {conversation_id}: {e}")
            raise StreamingError(f"Failed to stream events: {e}")
    
    def pause_conversation(self, conversation_id: str) -> None:
        """Pause a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        if state.status == ConversationStatus.ACTIVE:
            state.status = ConversationStatus.PAUSED
            logger.info(f"Paused conversation {conversation_id}")
    
    def resume_conversation(self, conversation_id: str) -> None:
        """Resume a paused conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        if state.status == ConversationStatus.PAUSED:
            state.status = ConversationStatus.ACTIVE
            logger.info(f"Resumed conversation {conversation_id}")
    
    def stop_conversation(self, conversation_id: str) -> None:
        """Stop a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        state.status = ConversationStatus.STOPPED
        
        # Cancel running task
        if conversation_id in self._running_tasks:
            task = self._running_tasks[conversation_id]
            if not task.done():
                task.cancel()
            del self._running_tasks[conversation_id]
            
        logger.info(f"Stopped conversation {conversation_id}")
    
    def list_user_conversations(self, user_id: str) -> List[ConversationState]:
        """List all conversations for a user.
        
        Args:
            user_id: ID of the user
            
        Returns:
            List of conversation states
        """
        return [
            state for state in self._conversations.values()
            if state.user_id == user_id
        ]
    
    def get_conversation_history(self, conversation_id: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Get conversation history from the lab instance.
        
        Args:
            conversation_id: ID of the conversation
            limit: Maximum number of history entries to return
            
        Returns:
            List of conversation history entries
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        lab = state.lab_instance
        
        # Get history from lab state
        history = getattr(lab.state, 'history', [])
        return history[-limit:] if limit > 0 else history
    
    def get_conversation_transcript(self, conversation_id: str, limit: int = 100) -> List[Dict[str, Any]]:
        """Get conversation transcript from persistence store.
        
        Args:
            conversation_id: ID of the conversation
            limit: Maximum number of transcript entries to return
            
        Returns:
            List of transcript entries
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        try:
            # Get transcript from store
            from agentrylab.persistence.store import Store
            store = Store()
            transcript = store.read_transcript(conversation_id, limit=limit)
            return transcript
        except Exception as e:
            logger.error(f"Failed to read transcript for conversation {conversation_id}: {e}")
            return []
    
    def get_conversation_summary(self, conversation_id: str) -> Optional[str]:
        """Get conversation summary if available.
        
        Note: This method returns the running summary from the lab state.
        For presets with run_on_last=true (like debates), the final comprehensive
        summary is stored in the transcript with role='summarizer' and should be
        accessed via get_conversation_transcript() or by reading the transcript
        directly from the lab store.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Running conversation summary or None if not available
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        lab = state.lab_instance
        
        # Get running summary from lab state
        return getattr(lab.state, 'running_summary', None)
    
    def get_final_summary(self, conversation_id: str) -> Optional[str]:
        """Get the final comprehensive summary from the summarizer agent.
        
        This method is specifically designed for presets with run_on_last=true
        (like debates) where a summarizer agent generates a comprehensive final
        summary after the conversation completes.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Final summarizer output or None if not available
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        try:
            state = self._conversations[conversation_id]
            lab = state.lab_instance
            transcript = lab.store.read_transcript(lab.state.thread_id)
            
            # Find the final summarizer message (last one with role='summarizer')
            for entry in reversed(transcript):
                if entry.get('role') == 'summarizer':
                    return entry.get('content', '')
            
            return None
            
        except Exception as e:
            logger.error(f"Failed to get final summary for conversation {conversation_id}: {e}")
            return None
    
    def get_conversation_budgets(self, conversation_id: str) -> Dict[str, Any]:
        """Get tool budgets for a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Dictionary with budget information
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        lab = state.lab_instance
        
        # Get tool budgets from lab state
        if hasattr(lab.state, 'get_tool_budgets'):
            return lab.state.get_tool_budgets()
        else:
            return {}
    
    def get_tool_usage_stats(self, conversation_id: str) -> Dict[str, Any]:
        """Get tool usage statistics for a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Dictionary with tool usage statistics
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        lab = state.lab_instance
        
        # Get tool usage stats from lab state
        stats = {}
        if hasattr(lab.state, '_tool_calls_run_total'):
            stats['total_tool_calls'] = lab.state._tool_calls_run_total
        if hasattr(lab.state, '_tool_calls_iteration'):
            stats['iteration_tool_calls'] = lab.state._tool_calls_iteration
        if hasattr(lab.state, '_tool_calls_run_by_id'):
            stats['tool_calls_by_id'] = dict(lab.state._tool_calls_run_by_id)
        if hasattr(lab.state, '_tool_calls_iter_by_id'):
            stats['iteration_tool_calls_by_id'] = dict(lab.state._tool_calls_iter_by_id)
        
        return stats
    
    def can_call_tool(self, conversation_id: str, tool_id: str) -> Tuple[bool, str]:
        """Check if a tool can be called for a conversation.
        
        Args:
            conversation_id: ID of the conversation
            tool_id: ID of the tool to check
            
        Returns:
            Tuple of (can_call, reason)
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        lab = state.lab_instance
        
        # Check if tool can be called
        if hasattr(lab.state, 'can_call_tool'):
            return lab.state.can_call_tool(tool_id)
        else:
            return True, "No budget restrictions"
    
    def get_budget_status(self, conversation_id: str) -> Dict[str, Any]:
        """Get comprehensive budget status for a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Dictionary with comprehensive budget status
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        lab = state.lab_instance
        
        status = {
            'conversation_id': conversation_id,
            'iteration': getattr(lab.state, 'iter', 0),
            'budgets': self.get_conversation_budgets(conversation_id),
            'usage_stats': self.get_tool_usage_stats(conversation_id),
        }
        
        # Add tool-specific status
        tool_status = {}
        if hasattr(lab.cfg, 'tools') and lab.cfg.tools:
            for tool in lab.cfg.tools:
                tool_id = tool.id
                can_call, reason = self.can_call_tool(conversation_id, tool_id)
                tool_status[tool_id] = {
                    'can_call': can_call,
                    'reason': reason,
                    'budget': self.get_conversation_budgets(conversation_id).get(tool_id, {}),
                }
        
        status['tool_status'] = tool_status
        return status
    
    def set_conversation_rounds(self, conversation_id: str, rounds: int) -> None:
        """Set the number of rounds for a conversation.
        
        Args:
            conversation_id: ID of the conversation
            rounds: Number of rounds to run
            
        Raises:
            ConversationNotFoundError: If conversation is not found
            ConversationNotActiveError: If conversation is not active
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        if state.status != ConversationStatus.ACTIVE:
            raise ConversationNotActiveError(f"Conversation {conversation_id} is not active")
            
        # Store rounds in conversation metadata
        state.metadata['max_rounds'] = rounds
        logger.info(f"Set conversation {conversation_id} to {rounds} rounds")
    
    def change_conversation_topic(self, conversation_id: str, new_topic: str) -> None:
        """Change the topic of an active conversation.
        
        Args:
            conversation_id: ID of the conversation
            new_topic: New topic for the conversation
            
        Raises:
            ConversationNotFoundError: If conversation is not found
            ConversationNotActiveError: If conversation is not active
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        if state.status != ConversationStatus.ACTIVE:
            raise ConversationNotActiveError(f"Conversation {conversation_id} is not active")
            
        # Update topic in state
        state.topic = new_topic
        
        # Update objective in lab if possible
        lab = state.lab_instance
        if hasattr(lab.cfg, 'objective'):
            try:
                lab.cfg.objective = new_topic
            except Exception:
                pass  # Best effort
                
        logger.info(f"Changed conversation {conversation_id} topic to: {new_topic}")
    
    def get_lab_status(self, conversation_id: str) -> Dict[str, Any]:
        """Get the current lab status for a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Dictionary with lab status information
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        lab = state.lab_instance
        
        status = {
            'conversation_id': conversation_id,
            'status': state.status.value,
            'iteration': getattr(lab.state, 'iter', 0),
            'stop_flag': getattr(lab.state, 'stop_flag', False),
            'active': getattr(lab, '_active', False),
            'last_ts': getattr(lab, '_last_ts', None),
            'topic': state.topic,
            'preset_id': state.preset_id,
            'user_id': state.user_id,
            'created_at': state.created_at.isoformat(),
            'last_activity': state.last_activity.isoformat(),
        }
        
        # Add metadata
        if state.metadata:
            status['metadata'] = state.metadata
            
        return status
    
    def get_conversation_progress(self, conversation_id: str) -> Dict[str, Any]:
        """Get conversation progress information.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Dictionary with progress information
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        lab = state.lab_instance
        
        # Get current iteration
        current_iter = getattr(lab.state, 'iter', 0)
        
        # Get max rounds from metadata or default
        max_rounds = state.metadata.get('max_rounds', 10)
        
        # Calculate progress
        progress_percent = (current_iter / max_rounds * 100) if max_rounds > 0 else 0
        
        progress = {
            'conversation_id': conversation_id,
            'current_iteration': current_iter,
            'max_rounds': max_rounds,
            'progress_percent': min(progress_percent, 100),
            'remaining_rounds': max(0, max_rounds - current_iter),
            'is_complete': current_iter >= max_rounds,
            'status': state.status.value,
        }
        
        return progress
    
    def get_provider_status(self, conversation_id: str) -> Dict[str, Any]:
        """Get provider status for a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Dictionary with provider status information
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        lab = state.lab_instance
        
        provider_status = {}
        
        # Get provider information from lab config
        if hasattr(lab.cfg, 'providers') and lab.cfg.providers:
            for provider in lab.cfg.providers:
                provider_id = getattr(provider, 'id', 'unknown')
                provider_status[provider_id] = {
                    'id': provider_id,
                    'impl': getattr(provider, 'impl', 'unknown'),
                    'model': getattr(provider, 'model', 'unknown'),
                    'api_key_configured': bool(getattr(provider, 'api_key', None)),
                    'extra_config': getattr(provider, 'extra', {}),
                }
        
        return {
            'conversation_id': conversation_id,
            'providers': provider_status,
            'total_providers': len(provider_status),
        }
    
    def get_tool_status(self, conversation_id: str) -> Dict[str, Any]:
        """Get tool status for a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Dictionary with tool status information
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        lab = state.lab_instance
        
        tool_status = {}
        
        # Get tool information from lab config
        if hasattr(lab.cfg, 'tools') and lab.cfg.tools:
            for tool in lab.cfg.tools:
                tool_id = getattr(tool, 'id', 'unknown')
                tool_status[tool_id] = {
                    'id': tool_id,
                    'impl': getattr(tool, 'impl', 'unknown'),
                    'budget': getattr(tool, 'budget', {}),
                    'enabled': True,  # Tools in config are enabled
                }
        
        return {
            'conversation_id': conversation_id,
            'tools': tool_status,
            'total_tools': len(tool_status),
        }
    
    def get_system_health(self, conversation_id: str) -> Dict[str, Any]:
        """Get comprehensive system health for a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Dictionary with system health information
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        lab = state.lab_instance
        
        health = {
            'conversation_id': conversation_id,
            'status': state.status.value,
            'iteration': getattr(lab.state, 'iter', 0),
            'stop_flag': getattr(lab.state, 'stop_flag', False),
            'active': getattr(lab, '_active', False),
            'providers': self.get_provider_status(conversation_id),
            'tools': self.get_tool_status(conversation_id),
            'budgets': self.get_conversation_budgets(conversation_id),
            'usage_stats': self.get_tool_usage_stats(conversation_id),
        }
        
        # Calculate overall health score
        health_score = 100
        
        # Deduct points for issues
        if state.status != ConversationStatus.ACTIVE:
            health_score -= 20
        if getattr(lab.state, 'stop_flag', False):
            health_score -= 30
        if not getattr(lab, '_active', False):
            health_score -= 10
        
        # Check for budget issues
        usage_stats = health['usage_stats']
        if usage_stats.get('total_tool_calls', 0) > 100:  # High usage
            health_score -= 10
        
        health['health_score'] = max(0, health_score)
        health['health_status'] = (
            'excellent' if health_score >= 90 else
            'good' if health_score >= 70 else
            'warning' if health_score >= 50 else
            'critical'
        )
        
        return health
    
    def get_conversation_analytics(self, conversation_id: str) -> Dict[str, Any]:
        """Get conversation analytics and metrics.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Dictionary with conversation analytics
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        state = self._conversations[conversation_id]
        lab = state.lab_instance
        
        # Get basic conversation info
        analytics = {
            'conversation_id': conversation_id,
            'preset_id': state.preset_id,
            'topic': state.topic,
            'user_id': state.user_id,
            'status': state.status.value,
            'created_at': state.created_at.isoformat(),
            'last_activity': state.last_activity.isoformat(),
            'duration_seconds': (state.last_activity - state.created_at).total_seconds(),
        }
        
        # Get iteration and progress info
        current_iter = getattr(lab.state, 'iter', 0)
        max_rounds = state.metadata.get('max_rounds', 10)
        analytics.update({
            'current_iteration': current_iter,
            'max_rounds': max_rounds,
            'progress_percent': min((current_iter / max_rounds * 100) if max_rounds > 0 else 0, 100),
            'is_complete': current_iter >= max_rounds,
        })
        
        # Get history statistics
        history = getattr(lab.state, 'history', [])
        analytics.update({
            'total_messages': len(history),
            'agent_messages': len([h for h in history if h.get('role') == 'agent']),
            'user_messages': len([h for h in history if h.get('role') == 'user']),
            'moderator_messages': len([h for h in history if h.get('role') == 'moderator']),
        })
        
        # Get tool usage statistics
        usage_stats = self.get_tool_usage_stats(conversation_id)
        analytics.update({
            'total_tool_calls': usage_stats.get('total_tool_calls', 0),
            'iteration_tool_calls': usage_stats.get('iteration_tool_calls', 0),
            'tool_calls_by_id': usage_stats.get('tool_calls_by_id', {}),
        })
        
        # Get budget information
        budgets = self.get_conversation_budgets(conversation_id)
        analytics.update({
            'budget_info': budgets,
        })
        
        # Calculate efficiency metrics
        if current_iter > 0:
            analytics.update({
                'messages_per_iteration': len(history) / current_iter,
                'tool_calls_per_iteration': usage_stats.get('total_tool_calls', 0) / current_iter,
            })
        else:
            analytics.update({
                'messages_per_iteration': 0,
                'tool_calls_per_iteration': 0,
            })
        
        return analytics
    
    def export_conversation_data(self, conversation_id: str, format: str = "json") -> str:
        """Export conversation data in specified format.
        
        Args:
            conversation_id: ID of the conversation
            format: Export format ("json", "yaml", "csv")
            
        Returns:
            Exported data as string
            
        Raises:
            ConversationNotFoundError: If conversation is not found
            ValueError: If format is not supported
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        if format not in ["json", "yaml", "csv"]:
            raise ValueError(f"Unsupported format: {format}. Supported formats: json, yaml, csv")
        
        # Collect all conversation data
        data = {
            'conversation_info': {
                'conversation_id': conversation_id,
                'preset_id': self._conversations[conversation_id].preset_id,
                'topic': self._conversations[conversation_id].topic,
                'user_id': self._conversations[conversation_id].user_id,
                'status': self._conversations[conversation_id].status.value,
                'created_at': self._conversations[conversation_id].created_at.isoformat(),
                'last_activity': self._conversations[conversation_id].last_activity.isoformat(),
            },
            'analytics': self.get_conversation_analytics(conversation_id),
            'history': self.get_conversation_history(conversation_id, limit=0),  # Get all history
            'transcript': self.get_conversation_transcript(conversation_id, limit=0),  # Get all transcript
            'budgets': self.get_conversation_budgets(conversation_id),
            'usage_stats': self.get_tool_usage_stats(conversation_id),
            'provider_status': self.get_provider_status(conversation_id),
            'tool_status': self.get_tool_status(conversation_id),
            'system_health': self.get_system_health(conversation_id),
        }
        
        # Export in requested format
        if format == "json":
            import json
            return json.dumps(data, indent=2, default=str)
        elif format == "yaml":
            import yaml
            # Convert to JSON first to avoid YAML serialization issues
            import json
            json_str = json.dumps(data, default=str)
            json_data = json.loads(json_str)
            return yaml.dump(json_data, default_flow_style=False)
        elif format == "csv":
            # For CSV, we'll export the history as a table
            import csv
            import io
            
            output = io.StringIO()
            if data['history']:
                fieldnames = data['history'][0].keys()
                writer = csv.DictWriter(output, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data['history'])
            return output.getvalue()
    
    def get_conversation_summary_report(self, conversation_id: str) -> str:
        """Generate a human-readable summary report for a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Human-readable summary report
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        if conversation_id not in self._conversations:
            raise ConversationNotFoundError(f"Conversation {conversation_id} not found")
            
        analytics = self.get_conversation_analytics(conversation_id)
        health = self.get_system_health(conversation_id)
        
        report = f"""
# Conversation Summary Report

## Basic Information
- **Conversation ID**: {analytics['conversation_id']}
- **Preset**: {analytics['preset_id']}
- **Topic**: {analytics['topic']}
- **User**: {analytics['user_id']}
- **Status**: {analytics['status']}
- **Created**: {analytics['created_at']}
- **Last Activity**: {analytics['last_activity']}
- **Duration**: {analytics['duration_seconds']:.1f} seconds

## Progress
- **Current Iteration**: {analytics['current_iteration']} / {analytics['max_rounds']}
- **Progress**: {analytics['progress_percent']:.1f}%
- **Complete**: {'Yes' if analytics['is_complete'] else 'No'}

## Message Statistics
- **Total Messages**: {analytics['total_messages']}
- **Agent Messages**: {analytics['agent_messages']}
- **User Messages**: {analytics['user_messages']}
- **Moderator Messages**: {analytics['moderator_messages']}
- **Messages per Iteration**: {analytics['messages_per_iteration']:.1f}

## Tool Usage
- **Total Tool Calls**: {analytics['total_tool_calls']}
- **Tool Calls per Iteration**: {analytics['tool_calls_per_iteration']:.1f}
- **Tools Used**: {', '.join(analytics['tool_calls_by_id'].keys()) if analytics['tool_calls_by_id'] else 'None'}

## System Health
- **Health Score**: {health['health_score']}/100
- **Health Status**: {health['health_status']}
- **Providers**: {health['providers']['total_providers']}
- **Tools**: {health['tools']['total_tools']}

## Summary
This conversation ran for {analytics['duration_seconds']:.1f} seconds with {analytics['total_messages']} messages across {analytics['current_iteration']} iterations. 
The system health is {health['health_status']} with a score of {health['health_score']}/100.
"""
        
        return report.strip()
    
    def get_available_presets(self) -> List[str]:
        """Get list of available preset IDs.
        
        Returns:
            List of available preset IDs
        """
        try:
            import os
            import glob
            preset_dir = os.path.join(os.path.dirname(__file__), '..', 'presets')
            preset_files = glob.glob(os.path.join(preset_dir, '*.yaml'))
            return [os.path.basename(f).replace('.yaml', '') for f in preset_files]
        except Exception as e:
            logger.warning(f"Failed to list presets: {e}")
            return []
    
    def get_preset_info(self, preset_id: str) -> Dict[str, Any]:
        """Get information about a specific preset.
        
        Args:
            preset_id: ID of the preset
            
        Returns:
            Dictionary with preset information
            
        Raises:
            InvalidPresetError: If preset is not found
        """
        try:
            import os
            import yaml
            preset_path = os.path.join(
                os.path.dirname(__file__), '..', 'presets', f'{preset_id}.yaml'
            )
            if not os.path.exists(preset_path):
                raise InvalidPresetError(f"Preset {preset_id} not found")
                
            with open(preset_path, 'r') as f:
                preset_data = yaml.safe_load(f)
                
            return {
                'preset_id': preset_id,
                'name': preset_data.get('name', preset_id),
                'description': preset_data.get('description', ''),
                'agents': [agent.get('id', 'unknown') for agent in preset_data.get('agents', [])],
                'tools': [tool.get('id', 'unknown') for tool in preset_data.get('tools', [])],
                'providers': [provider.get('id', 'unknown') for provider in preset_data.get('providers', [])],
                'schedule': preset_data.get('schedule', {}),
            }
        except Exception as e:
            logger.error(f"Failed to get preset info for {preset_id}: {e}")
            raise InvalidPresetError(f"Failed to load preset {preset_id}: {e}")
    
    def get_conversation_nodes(self, conversation_id: str) -> Dict[str, Any]:
        """Get information about nodes in a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Dictionary with node information
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        state = _validate_conversation_exists(self, conversation_id)
        lab = state.lab_instance
        
        nodes_info = {}
        if hasattr(lab, 'nodes') and lab.nodes:
            for node_id, node in lab.nodes.items():
                nodes_info[node_id] = {
                    'id': node_id,
                    'role': getattr(node, 'role_name', 'unknown'),
                    'type': type(node).__name__,
                    'active': True,  # Nodes in the lab are active
                }
        
        return {
            'conversation_id': conversation_id,
            'nodes': nodes_info,
            'total_nodes': len(nodes_info),
        }
    
    def get_conversation_scheduler_info(self, conversation_id: str) -> Dict[str, Any]:
        """Get information about the scheduler for a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Dictionary with scheduler information
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        state = _validate_conversation_exists(self, conversation_id)
        lab = state.lab_instance
        
        scheduler_info = {}
        if hasattr(lab, 'scheduler') and lab.scheduler:
            scheduler = lab.scheduler
            scheduler_info = {
                'type': type(scheduler).__name__,
                'params': getattr(scheduler, 'params', {}),
                'agents': getattr(scheduler, '_agents', []),
            }
        
        return {
            'conversation_id': conversation_id,
            'scheduler': scheduler_info,
        }
    
    def send_engine_action(self, conversation_id: str, action: str, **kwargs) -> None:
        """Send an engine action to control conversation flow.
        
        Args:
            conversation_id: ID of the conversation
            action: Action type ("CONTINUE", "STOP", "STEP_BACK")
            **kwargs: Additional action parameters
            
        Raises:
            ConversationNotFoundError: If conversation is not found
            ConversationNotActiveError: If conversation is not active
            ValueError: If action is not supported
        """
        state = _validate_conversation_exists(self, conversation_id)
        _validate_conversation_active(state)
        
        if action not in ["CONTINUE", "STOP", "STEP_BACK"]:
            raise ValueError(f"Unsupported action: {action}")
        
        # Set appropriate state flags based on action
        if action == "STOP":
            state.lab_instance.state.stop_flag = True
        elif action == "STEP_BACK":
            # This would require more complex state management
            logger.warning("STEP_BACK action not fully implemented")
        # CONTINUE is implicit (no action needed)
        
        logger.info(f"Sent engine action {action} to conversation {conversation_id}")
    
    def get_conversation_engine_status(self, conversation_id: str) -> Dict[str, Any]:
        """Get detailed engine status for a conversation.
        
        Args:
            conversation_id: ID of the conversation
            
        Returns:
            Dictionary with engine status information
            
        Raises:
            ConversationNotFoundError: If conversation is not found
        """
        state = _validate_conversation_exists(self, conversation_id)
        lab = state.lab_instance
        
        engine_status = {
            'conversation_id': conversation_id,
            'iteration': getattr(lab.state, 'iter', 0),
            'stop_flag': getattr(lab.state, 'stop_flag', False),
            'active': getattr(lab, '_active', False),
            'has_transcript_writer': hasattr(lab, '_has_append') and lab._has_append,
            'has_checkpoint_saver': hasattr(lab, '_has_checkpoint') and lab._has_checkpoint,
        }
        
        # Add scheduler info
        if hasattr(lab, 'scheduler'):
            engine_status['scheduler_type'] = type(lab.scheduler).__name__
        
        # Add node info
        if hasattr(lab, 'nodes'):
            engine_status['node_count'] = len(lab.nodes)
            engine_status['node_types'] = [type(node).__name__ for node in lab.nodes.values()]
        
        return engine_status
    
    async def _run_conversation(self, conversation_id: str) -> None:
        """Run a conversation in the background.
        
        Args:
            conversation_id: ID of the conversation
        """
        try:
            state = self._conversations[conversation_id]
            lab = state.lab_instance
            event_queue = self._event_streams[conversation_id]
            user_queue = self._user_message_queues[conversation_id]
            
            # Send conversation started event
            await self._emit_event(conversation_id, "conversation_started", "Conversation started")
            
            # Get max rounds from metadata or default to 10
            max_rounds = state.metadata.get('max_rounds', 10)
            
            # Run the lab with streaming
            for event in lab.stream(rounds=max_rounds):
                # Check if conversation is still active
                if state.status != ConversationStatus.ACTIVE:
                    break
                    
                # Convert lab event to conversation event with better type detection
                event_type = event.get("event", "agent_message")
                if event_type == "agent_message":
                    # Determine if it's actually a user message
                    role = event.get("role", "")
                    if role == "user":
                        event_type = "user_message"
                    elif role == "moderator":
                        event_type = "moderator_action"
                    elif role == "summarizer":
                        event_type = "summary_update"
                
                conv_event = ConversationEvent(
                    conversation_id=conversation_id,
                    event_type=event_type,
                    content=str(event.get("content", "")),
                    metadata=event.get("metadata", {}),
                    iteration=event.get("iter", 0),
                    agent_id=event.get("agent_id"),
                    role=event.get("role"),
                )
                
                await event_queue.put(conv_event)
                
                # Check for user input
                try:
                    user_msg = user_queue.get_nowait()
                    if not user_msg.processed:
                        # Post user message to lab
                        lab.post_user_message(user_msg.content, user_id=user_msg.user_id)
                        user_msg.processed = True
                        
                        # Emit user message event
                        await self._emit_event(
                            conversation_id, 
                            "user_message", 
                            user_msg.content,
                            metadata={"user_id": user_msg.user_id}
                        )
                except asyncio.QueueEmpty:
                    pass
                    
            # Send conversation completed event
            await self._emit_event(conversation_id, "conversation_completed", "Conversation completed")
            state.status = ConversationStatus.COMPLETED
            
        except asyncio.CancelledError:
            logger.info(f"Conversation {conversation_id} was cancelled")
            state.status = ConversationStatus.STOPPED
        except Exception as e:
            logger.error(f"Error running conversation {conversation_id}: {e}")
            state.status = ConversationStatus.ERROR
            await self._emit_event(conversation_id, "error", f"Error: {e}")
        finally:
            # Cleanup
            if conversation_id in self._running_tasks:
                del self._running_tasks[conversation_id]
    
    async def _emit_event(
        self, 
        conversation_id: str, 
        event_type: str, 
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """Emit an event to a conversation's event stream.
        
        Args:
            conversation_id: ID of the conversation
            event_type: Type of the event
            content: Event content
            metadata: Optional event metadata
        """
        if conversation_id not in self._event_streams:
            return
            
        event = ConversationEvent(
            conversation_id=conversation_id,
            event_type=event_type,
            content=content,
            metadata=metadata or {},
        )
        
        try:
            await self._event_streams[conversation_id].put(event)
        except Exception as e:
            logger.error(f"Failed to emit event for conversation {conversation_id}: {e}")
    
    def cleanup_conversation(self, conversation_id: str) -> None:
        """Clean up resources for a conversation.
        
        Args:
            conversation_id: ID of the conversation
        """
        # Stop conversation if still running
        if conversation_id in self._conversations:
            self.stop_conversation(conversation_id)
            
        # Clean up queues
        if conversation_id in self._event_streams:
            del self._event_streams[conversation_id]
        if conversation_id in self._user_message_queues:
            del self._user_message_queues[conversation_id]
        if conversation_id in self._conversations:
            del self._conversations[conversation_id]
            
        logger.info(f"Cleaned up conversation {conversation_id}")
    
    def get_stats(self) -> Dict[str, Any]:
        """Get adapter statistics.
        
        Returns:
            Dictionary with adapter statistics
        """
        active_conversations = sum(
            1 for state in self._conversations.values()
            if state.status == ConversationStatus.ACTIVE
        )
        
        return {
            "total_conversations": len(self._conversations),
            "active_conversations": active_conversations,
            "paused_conversations": sum(
                1 for state in self._conversations.values()
                if state.status == ConversationStatus.PAUSED
            ),
            "stopped_conversations": sum(
                1 for state in self._conversations.values()
                if state.status == ConversationStatus.STOPPED
            ),
            "error_conversations": sum(
                1 for state in self._conversations.values()
                if state.status == ConversationStatus.ERROR
            ),
            "max_concurrent": self.max_concurrent_conversations,
        }
