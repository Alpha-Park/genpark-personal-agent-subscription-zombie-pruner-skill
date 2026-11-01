---
name: genpark-personal-agent-subscription-zombie-pruner-skill
description: Personal Agent Subscription Zombie Pruner. Audits recurring subscriptions by cost-per-use, detects zero-utility zombie SaaS/memberships, and calculates 5-year compounded wealth recovery.
license: MIT
version: 1.0.0
tools:
  - audit_subscription_utilization_and_cost_per_use
  - identify_zombie_subscriptions_and_cancellation_payoff
  - project_subscription_drag_and_compound_savings
---

# Personal Agent Subscription Zombie Pruner

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent recurring expense fiduciary. Your objective is to eradicate financial leakage from neglected subscriptions, gym memberships, and SaaS platforms by computing cost-per-use economics and projecting compounded reinvestment returns.

## When to Activate This Skill
- When an agent or user audits credit card statements, bank recurring expenses, or SaaS tools.
- When identifying dormant services with zero usage over $>45$ days.
- When evaluating the long-term wealth impact of canceling low-utility recurring charges.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentSubscriptionZombiePruner

pruner = PersonalAgentSubscriptionZombiePruner()
res = pruner.project_subscription_drag_and_compound_savings(monthly_savings_usd=50.0, horizon_years=5)
print("5-Year Reclaimed Wealth:", res["total_reclaimed_wealth_future_value_usd"])
```

### Option 2: FastMCP Tool Calling
- `audit_subscription_utilization_and_cost_per_use(subscriptions_json)`
- `identify_zombie_subscriptions_and_cancellation_payoff(subscriptions_json, inactivity_threshold_days=45)`
- `project_subscription_drag_and_compound_savings(monthly_savings_usd, investment_annual_rate=0.07, horizon_years=5)`

## Core Mathematical Principles
1. **Cost-Per-Use (CPU)**: $	ext{CPU} = rac{	ext{Monthly Cost}}{\max(1, 	ext{Uses})}$. Identifies nominally inexpensive services with astronomical per-use costs.
2. **Compound Opportunity Cost**: Canceling $50/mo of zombie services invested at 7% recovers $pprox \$3,600$ over 5 years.
