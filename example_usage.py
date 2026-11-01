# -*- coding: utf-8 -*-
import json
from client import PersonalAgentSubscriptionZombiePruner

pruner = PersonalAgentSubscriptionZombiePruner()

print("=" * 64)
print("DEMO: Personal Subscription & Recurring SaaS Zombie Pruner")
print("=" * 64)

# 1. Audit personal subscriptions
subscriptions = [
    {"name": "Netflix 4K", "monthly_cost_usd": 22.99, "monthly_uses": 18, "days_since_last_use": 1},
    {"name": "Gym Membership", "monthly_cost_usd": 85.00, "monthly_uses": 1, "days_since_last_use": 28},
    {"name": "Design Tool Pro", "monthly_cost_usd": 35.00, "monthly_uses": 0, "days_since_last_use": 64},
    {"name": "Cloud Storage Extra", "monthly_cost_usd": 9.99, "monthly_uses": 25, "days_since_last_use": 2},
    {"name": "Language App Subscription", "monthly_cost_usd": 12.99, "monthly_uses": 0, "days_since_last_use": 90}
]

audit = pruner.audit_subscription_utilization_and_cost_per_use(subscriptions)
print(f"\n1. Subscription Audit ({audit['total_active_subscriptions']} Services | ${audit['total_monthly_subscription_burn_usd']}/month):")
for s in audit["subscription_audit"]:
    print(f"   [{s['fiduciary_action']}] {s['name']}: ${s['monthly_cost_usd']}/mo (CPU: ${s['cost_per_use_usd']}) -> {s['efficiency_verdict']}")

# 2. Identify zombie subscriptions
zombies = pruner.identify_zombie_subscriptions_and_cancellation_payoff(subscriptions, inactivity_threshold_days=45)
print(f"\n2. Zombie Drain Analysis:")
print(f"   Zombie Services Detected: {zombies['zombie_subscriptions_detected']} ({', '.join(zombies['zombie_services_list'])})")
print(f"   Immediate Annual Reclaimable Capital: ${zombies['annual_reclaimable_capital_usd']:,}/year")

# 3. Project compounded savings
growth = pruner.project_subscription_drag_and_compound_savings(monthly_savings_usd=zombies['monthly_reclaimable_capital_usd'], horizon_years=5)
print(f"\n3. 5-Year Compounded Reclaimed Wealth (at 7% ROI):")
print(f"   Raw Cash Saved: ${growth['raw_principal_saved_usd']:,}")
print(f"   Total Compounded Wealth Created: ${growth['total_reclaimed_wealth_future_value_usd']:,}")
