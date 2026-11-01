# -*- coding: utf-8 -*-
"""
Personal Agent Subscription Zombie Pruner FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentSubscriptionZombiePruner

mcp = FastMCP("genpark-personal-agent-subscription-zombie-pruner-skill")
pruner = PersonalAgentSubscriptionZombiePruner()

@mcp.tool()
def audit_subscription_utilization_and_cost_per_use(subscriptions_json: str) -> str:
    """
    Audits recurring subscriptions, calculating cost-per-use and value efficiency.
    """
    subs = json.loads(subscriptions_json)
    res = pruner.audit_subscription_utilization_and_cost_per_use(subs)
    return json.dumps(res, indent=2)

@mcp.tool()
def identify_zombie_subscriptions_and_cancellation_payoff(
    subscriptions_json: str,
    inactivity_threshold_days: int = 45
) -> str:
    """
    Identifies zero-utility zombie subscriptions and calculates annual cancellation savings.
    """
    subs = json.loads(subscriptions_json)
    res = pruner.identify_zombie_subscriptions_and_cancellation_payoff(subs, inactivity_threshold_days)
    return json.dumps(res, indent=2)

@mcp.tool()
def project_subscription_drag_and_compound_savings(
    monthly_savings_usd: float,
    investment_annual_rate: float = 0.07,
    horizon_years: int = 5
) -> str:
    """
    Projects 5-year compounded wealth created by investing canceled subscription savings.
    """
    res = pruner.project_subscription_drag_and_compound_savings(monthly_savings_usd, investment_annual_rate, horizon_years)
    return json.dumps(res, indent=2)

def main():
    print("Testing Subscription Zombie Pruner FastMCP Server:")
    s = [{"name": "Old App", "monthly_cost_usd": 15.0, "monthly_uses": 0, "days_since_last_use": 60}]
    print(identify_zombie_subscriptions_and_cancellation_payoff(json.dumps(s)))

if __name__ == "__main__":
    main()
