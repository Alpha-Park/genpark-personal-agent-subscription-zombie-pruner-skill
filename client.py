# -*- coding: utf-8 -*-
"""
Personal Agent Subscription Zombie Pruner Client
Zero-dependency cost-per-use recurring expense auditor, dormant zombie subscription
detector, and 5-year opportunity cost compound savings forecaster.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentSubscriptionZombiePruner:
    """
    Audits recurring software, media, and membership subscriptions.
    Identifies zero-utility zombie subscriptions and projects compounded wealth reclamation.
    """

    def audit_subscription_utilization_and_cost_per_use(
        self,
        subscriptions: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Calculates Cost-Per-Use (CPU) and value efficiency for all active subscriptions.
        Subscription format: {"name": "Streaming App", "monthly_cost_usd": 19.99, "monthly_uses": 2, "days_since_last_use": 20}
        """
        if not subscriptions:
            raise ValueError("Subscriptions list cannot be empty.")

        total_monthly_burn = 0.0
        audited = []

        for sub in subscriptions:
            name = sub.get("name", "Unknown Service")
            cost = max(0.0, float(sub.get("monthly_cost_usd", 10.0)))
            uses = max(0, int(sub.get("monthly_uses", 0)))
            days_inactive = max(0, int(sub.get("days_since_last_use", 0)))

            total_monthly_burn += cost
            cpu = round(cost / max(1, uses), 2)

            if uses == 0 or days_inactive >= 45:
                verdict = "ZOMBIE_DRAIN (Zero recent utility)"
                action = "CANCEL_IMMEDIATELY"
            elif cpu >= 15.0 and cost >= 25.0:
                verdict = "POOR_VALUE_UNDERUTILIZED"
                action = "PAUSE_OR_DOWNGRADE"
            elif uses >= 8:
                verdict = "HIGH_VALUE_ESSENTIAL"
                action = "MAINTAIN"
            else:
                verdict = "MODERATE_UTILITY"
                action = "MONITOR"

            audited.append({
                "name": name,
                "monthly_cost_usd": cost,
                "monthly_uses": uses,
                "days_since_last_use": days_inactive,
                "cost_per_use_usd": cpu,
                "efficiency_verdict": verdict,
                "fiduciary_action": action
            })

        audited.sort(key=lambda x: x["cost_per_use_usd"], reverse=True)

        return {
            "total_active_subscriptions": len(subscriptions),
            "total_monthly_subscription_burn_usd": round(total_monthly_burn, 2),
            "total_annual_subscription_burn_usd": round(total_monthly_burn * 12.0, 2),
            "subscription_audit": audited
        }

    def identify_zombie_subscriptions_and_cancellation_payoff(
        self,
        subscriptions: List[Dict[str, Any]],
        inactivity_threshold_days: int = 45
    ) -> Dict[str, Any]:
        """
        Filters and aggregates zombie subscriptions that should be canceled immediately.
        """
        audit = self.audit_subscription_utilization_and_cost_per_use(subscriptions)
        cutoff = max(14, int(inactivity_threshold_days))

        zombies = []
        monthly_reclaimable = 0.0

        for item in audit["subscription_audit"]:
            if item["days_since_last_use"] >= cutoff or item["monthly_uses"] == 0:
                zombies.append(item)
                monthly_reclaimable += item["monthly_cost_usd"]

        annual_reclaimable = round(monthly_reclaimable * 12.0, 2)

        return {
            "inactivity_threshold_days": cutoff,
            "zombie_subscriptions_detected": len(zombies),
            "monthly_reclaimable_capital_usd": round(monthly_reclaimable, 2),
            "annual_reclaimable_capital_usd": annual_reclaimable,
            "zombie_services_list": [z["name"] for z in zombies],
            "fiduciary_priority": "CRITICAL_WASTE_REDUCTION" if monthly_reclaimable >= 50.0 else "ROUTINE_HYGIENE"
        }

    def project_subscription_drag_and_compound_savings(
        self,
        monthly_savings_usd: float,
        investment_annual_rate: float = 0.07,
        horizon_years: int = 5
    ) -> Dict[str, Any]:
        """
        Projects compounded future value of canceling zombie subscriptions:
        FV = PMT * ((1 + r/12)^n - 1) / (r/12).
        """
        pmt = max(0.0, float(monthly_savings_usd))
        r = max(0.01, min(0.20, float(investment_annual_rate)))
        years = max(1, min(30, int(horizon_years)))

        n = years * 12
        r_monthly = r / 12.0

        future_value = pmt * (math.pow(1.0 + r_monthly, n) - 1.0) / r_monthly
        cumulative_principal_saved = pmt * n
        compound_interest_gained = future_value - cumulative_principal_saved

        return {
            "monthly_canceled_subscriptions_usd": pmt,
            "horizon_years": years,
            "investment_annual_rate_pct": round(r * 100.0, 1),
            "raw_principal_saved_usd": round(cumulative_principal_saved, 2),
            "compound_investment_growth_usd": round(compound_interest_gained, 2),
            "total_reclaimed_wealth_future_value_usd": round(future_value, 2)
        }
