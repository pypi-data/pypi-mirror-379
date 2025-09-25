"""
Core memory - always-accessible foundational facts (MemGPT/Letta pattern).
"""

from typing import Dict, Optional, List
from datetime import datetime
from dataclasses import dataclass

from abstractmemory.core.interfaces import IMemoryComponent, MemoryItem


@dataclass
class CoreMemoryBlock:
    """A block of core memory (always in context)"""
    block_id: str
    label: str           # "persona" or "user_info"
    content: str         # Max ~200 tokens
    last_updated: datetime
    edit_count: int = 0

    def update(self, new_content: str, agent_reasoning: str):
        """Agent can self-edit this block"""
        self.content = new_content
        self.last_updated = datetime.now()
        self.edit_count += 1


class CoreMemory(IMemoryComponent):
    """
    Always-accessible core memory for fundamental facts.
    Based on MemGPT/Letta research - stores agent persona + user information.
    """

    def __init__(self, max_blocks: int = 10, max_tokens_per_block: int = 200):
        self.blocks: Dict[str, CoreMemoryBlock] = {}
        self.max_blocks = max_blocks
        self.max_tokens_per_block = max_tokens_per_block

        # Initialize default blocks (MemGPT pattern)
        self.blocks["persona"] = CoreMemoryBlock(
            block_id="persona",
            label="persona",
            content="I am an AI assistant with persistent memory capabilities.",
            last_updated=datetime.now()
        )
        self.blocks["user_info"] = CoreMemoryBlock(
            block_id="user_info",
            label="user_info",
            content="User information will be learned over time.",
            last_updated=datetime.now()
        )

    def get_context(self) -> str:
        """Get all core memory as context string (always included in prompts)"""
        context_parts = []
        for block in self.blocks.values():
            context_parts.append(f"[{block.label}] {block.content}")
        return "\n".join(context_parts)

    def update_block(self, block_id: str, content: str, reasoning: str = "") -> bool:
        """Agent updates a core memory block (self-editing capability)"""
        if block_id in self.blocks:
            if len(content) <= self.max_tokens_per_block * 4:  # Rough token estimate
                self.blocks[block_id].update(content, reasoning)
                return True
        return False

    def add_block(self, label: str, content: str) -> Optional[str]:
        """Add new core memory block if space available"""
        if len(self.blocks) < self.max_blocks:
            block_id = f"core_{len(self.blocks)}"
            self.blocks[block_id] = CoreMemoryBlock(
                block_id=block_id,
                label=label,
                content=content,
                last_updated=datetime.now()
            )
            return block_id
        return None

    # IMemoryComponent interface implementation
    def add(self, item: MemoryItem) -> str:
        """Add important fact to core memory"""
        # Convert MemoryItem to core memory block
        content = str(item.content)
        if "user" in content.lower():
            return self.update_block("user_info", content) and "user_info" or ""
        elif "persona" in content.lower() or "agent" in content.lower():
            return self.update_block("persona", content) and "persona" or ""
        else:
            return self.add_block("general", content) or ""

    def retrieve(self, query: str, limit: int = 10) -> List[MemoryItem]:
        """Retrieve core memory blocks matching query"""
        results = []
        query_lower = query.lower()

        for block in self.blocks.values():
            if query_lower in block.content.lower() or query_lower in block.label.lower():
                results.append(MemoryItem(
                    content={"label": block.label, "content": block.content},
                    event_time=block.last_updated,
                    ingestion_time=block.last_updated,
                    confidence=1.0,  # Core memory is always high confidence
                    metadata={"block_id": block.block_id, "edit_count": block.edit_count}
                ))

        return results[:limit]

    def consolidate(self) -> int:
        """Core memory doesn't consolidate - it's manually curated"""
        return 0