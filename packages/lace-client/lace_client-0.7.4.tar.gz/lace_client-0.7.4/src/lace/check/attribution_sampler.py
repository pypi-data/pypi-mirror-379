"""
Budget-aware attribution sampler with priority scoring.
Maximizes domain coverage within GPT attribution budget.
"""

import heapq
import logging
from collections import defaultdict
from typing import Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


class AttributionSampler:
    """Smart sampling for GPT attribution within budget constraints."""

    def __init__(self, budget: int = 50):
        """
        Initialize attribution sampler.

        Args:
            budget: Maximum number of GPT attribution calls
        """
        self.budget = budget
        self.calls_made = 0
        self.domain_coverage = set()

    def calculate_priority(
        self,
        item: Dict[str, Any],
        offline_score: float = 0.0,
        policy_score: float = 0.0,
    ) -> float:
        """
        Calculate priority score for an item.

        Args:
            item: Item to score
            offline_score: Offline copyright detection score (0-1)
            policy_score: Policy opt-out score (0-1)

        Returns:
            Priority score (higher = more important to attribute)
        """
        # Base priority calculation
        # 0.6 * offline copyright signal
        # 0.3 * policy opt-out signal
        # 0.1 * novelty (first time seeing domain)

        # Extract domain from item
        domain = None
        if "attribution" in item and "domains" in item["attribution"]:
            domains = item["attribution"]["domains"]
            if domains:
                domain = domains[0]
        elif "top_sources" in item:
            for source in item["top_sources"]:
                if "domain" in source:
                    domain = source["domain"]
                    break

        # Novelty bonus if we haven't seen this domain
        novelty_score = 0.0
        if domain and domain not in self.domain_coverage:
            novelty_score = 1.0

        # Calculate weighted priority
        priority = 0.6 * offline_score + 0.3 * policy_score + 0.1 * novelty_score

        # Boost priority for high-confidence copyright/opt-out
        if offline_score > 0.8 or policy_score > 0.8:
            priority *= 1.2

        return min(priority, 1.0)

    def select_for_attribution(
        self,
        items: List[Dict[str, Any]],
        offline_scores: Optional[Dict[str, float]] = None,
        policy_scores: Optional[Dict[str, float]] = None,
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """
        Select items for GPT attribution within budget.

        Args:
            items: All items to consider
            offline_scores: Pre-calculated offline scores by item ID
            policy_scores: Pre-calculated policy scores by item ID

        Returns:
            Tuple of (selected_items, skipped_items)
        """
        if not items:
            return [], []

        offline_scores = offline_scores or {}
        policy_scores = policy_scores or {}

        # Build priority queue (negative priority for max heap)
        priority_queue = []

        # Group items by domain for deduplication
        domain_items = defaultdict(list)

        for item in items:
            # Get item ID
            item_id = item.get("id", item.get("sha256", ""))

            # Get scores
            offline = offline_scores.get(item_id, 0.0)
            policy = policy_scores.get(item_id, 0.0)

            # Calculate priority
            priority = self.calculate_priority(item, offline, policy)

            # Extract domain
            domain = self._extract_domain(item)

            # Add to domain group with priority
            domain_items[domain].append((priority, item))

        # Select top item per domain first (domain diversity)
        selected = []
        remaining = []

        for domain, items_with_priority in domain_items.items():
            if not items_with_priority:
                continue

            # Sort by priority descending
            items_with_priority.sort(key=lambda x: x[0], reverse=True)

            # Take the top item for this domain if budget allows
            if len(selected) < self.budget:
                priority, item = items_with_priority[0]
                selected.append(item)
                self.domain_coverage.add(domain)

                # Add rest to remaining pool
                for priority, item in items_with_priority[1:]:
                    tie_breaker = item.get("sha256", item.get("id", str(id(item))))[:12]
                    heapq.heappush(priority_queue, (-priority, tie_breaker, item))
            else:
                # Add all to remaining pool
                for priority, item in items_with_priority:
                    tie_breaker = item.get("sha256", item.get("id", str(id(item))))[:12]
                    heapq.heappush(priority_queue, (-priority, tie_breaker, item))

        # Fill remaining budget with highest priority items
        while len(selected) < self.budget and priority_queue:
            neg_priority, tie_breaker, item = heapq.heappop(priority_queue)
            selected.append(item)

        # Mark remaining as skipped
        skipped = []
        rank = 1
        while priority_queue:
            neg_priority, tie_breaker, item = heapq.heappop(priority_queue)
            item["gpt_skipped"] = True
            item["skip_reason"] = "budget_exhausted"
            item["priority_rank"] = rank
            skipped.append(item)
            rank += 1

        self.calls_made = len(selected)

        logger.info(
            f"Attribution sampling: {len(selected)} selected, "
            f"{len(skipped)} skipped, {len(self.domain_coverage)} unique domains"
        )

        return selected, skipped

    def _extract_domain(self, item: Dict[str, Any]) -> str:
        """Extract primary domain from item."""
        # Try various fields
        if "attribution" in item and "domains" in item["attribution"]:
            domains = item["attribution"]["domains"]
            if domains:
                return domains[0]

        if "top_sources" in item:
            for source in item["top_sources"]:
                if "domain" in source:
                    return source["domain"]

        if "policy_signals" in item and "domain" in item["policy_signals"]:
            return item["policy_signals"]["domain"]

        return "unknown"

    def get_summary(self) -> Dict[str, Any]:
        """Get sampling summary statistics."""
        return {
            "budget": self.budget,
            "calls_made": self.calls_made,
            "calls_remaining": self.budget - self.calls_made,
            "unique_domains": len(self.domain_coverage),
            "domain_coverage": list(self.domain_coverage)[:20],  # Top 20 for summary
        }
