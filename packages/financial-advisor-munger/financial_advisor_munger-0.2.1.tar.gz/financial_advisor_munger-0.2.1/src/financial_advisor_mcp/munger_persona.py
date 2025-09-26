"""
Charlie Munger Investment Persona
Production-ready persona integration from validation testing
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import json


class CharleMungerPersona:
    """
    Charlie Munger's investment analysis persona with authentic voice
    and sophisticated analytical framework for MCP integration
    """

    def __init__(self):
        # Munger's analytical preferences (not hardcoded competence)
        self.persona_characteristics = {
            "voice_style": "sharp, direct, and blunt",
            "analytical_approach": "inversion and kill-switches first",
            "key_phrases": [
                "Show me the incentive and I'll show you the outcome",
                "Invert, always invert",
                "At my age, I've seen this movie before",
                "The first rule of compounding is never interrupt it unnecessarily"
            ],
            "focus_areas": ["avoiding losses", "quality businesses", "simple models", "aligned management"]
        }

    def analyze_investment(self, financial_data: Dict[str, Any]) -> Dict[str, Any]:
        """Complete Munger-style investment analysis"""

        if 'error' in financial_data:
            return self._handle_data_error(financial_data)

        analysis_start = datetime.now()

        # Phase 1: Kill Switch Analysis
        kill_switches = self._apply_kill_switches(financial_data)

        if kill_switches['any_triggered']:
            # Immediate rejection
            recommendation = self._generate_rejection(financial_data, kill_switches)
        else:
            # Full scoring analysis
            scoring = self._score_investment(financial_data)
            recommendation = self._generate_recommendation(financial_data, scoring, kill_switches)

        analysis_time = (datetime.now() - analysis_start).total_seconds()

        return {
            'symbol': financial_data['symbol'],
            'company_name': financial_data.get('company_name', 'Unknown'),
            'analysis_type': 'charlie_munger',
            'recommendation': recommendation['decision'],
            'confidence': recommendation['confidence'],
            'munger_score': recommendation.get('score', 0),
            'munger_voice': recommendation['voice'],
            'key_reasoning': recommendation['reasoning'],
            'kill_switches': kill_switches['triggered_switches'],
            'strengths_identified': recommendation.get('strengths', []),
            'concerns_identified': recommendation.get('concerns', []),
            'follow_up_suggestions': self._generate_follow_ups(recommendation),
            'inversion_analysis': self._generate_inversion_thinking(financial_data),
            'data_quality': {
                'completeness': financial_data.get('completeness_score', 0),
                'validation_flags': financial_data.get('validation_flags', []),
                'analysis_time_seconds': analysis_time
            },
            'conversation_context': self._prepare_conversation_context(recommendation, financial_data)
        }

    def _apply_kill_switches(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Apply Munger's kill-switch framework"""

        triggered = []

        # Kill Switch 1: Accounting Quality
        net_income = data.get('net_income', 0)
        operating_cf = data.get('operating_cash_flow', 0)
        if net_income > 0 and operating_cf > 0:
            cf_quality = operating_cf / net_income
            if cf_quality < 0.7:
                triggered.append({
                    'switch': 'accounting_quality',
                    'reason': f'Poor cash conversion: {cf_quality:.1f}x earnings to operating cash',
                    'munger_voice': "When earnings don't show up as cash, I get suspicious. Show me the cash, not accounting magic."
                })

        # Kill Switch 2: Excessive Debt
        debt_ratio = data.get('debt_to_equity', 0)
        if debt_ratio > 200:  # >2.0x
            triggered.append({
                'switch': 'debt_levels',
                'reason': f'Excessive leverage: {debt_ratio/100:.1f}x debt-to-equity',
                'munger_voice': f"At {debt_ratio/100:.1f}x debt-to-equity, this company is playing Russian roulette with shareholders' money."
            })

        # Kill Switch 3: Poor Unit Economics
        roe = data.get('roe', 0)
        if roe and roe < 8:
            triggered.append({
                'switch': 'unit_economics',
                'reason': f'Poor returns: {roe:.1f}% ROE',
                'munger_voice': f"An ROE of {roe:.1f}% tells me this business struggles to earn its cost of capital. We want wealth creators, not destroyers."
            })

        # Kill Switch 4: Valuation Insanity
        pe_ratio = data.get('pe_ratio', 0)
        if pe_ratio and pe_ratio > 50:
            triggered.append({
                'switch': 'valuation',
                'reason': f'Excessive valuation: {pe_ratio:.1f}x P/E',
                'munger_voice': f"At {pe_ratio:.1f}x earnings, the market expects miracles. We prefer to buy when others are pessimistic."
            })

        return {
            'any_triggered': len(triggered) > 0,
            'triggered_switches': triggered,
            'passed_switches': len(triggered) == 0
        }

    def _score_investment(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Score investment using Munger's framework (0-100 points)"""

        scores = {
            'business_quality': 0,    # max 40 points
            'financial_strength': 0, # max 30 points
            'management_alignment': 0, # max 15 points
            'valuation': 0,          # max 15 points
            'total': 0
        }

        reasoning = []

        # Business Quality (40 points)
        roe = data.get('roe', 0)
        if roe and roe >= 20:
            scores['business_quality'] += 20
            reasoning.append(f"Excellent ROE of {roe:.1f}% indicates superior business economics")
        elif roe and roe >= 15:
            scores['business_quality'] += 15
            reasoning.append(f"Strong ROE of {roe:.1f}% shows good business quality")
        elif roe and roe >= 10:
            scores['business_quality'] += 10
            reasoning.append(f"Adequate ROE of {roe:.1f}% meets minimum requirements")

        # Moat indicators
        gross_margin = data.get('gross_margin', 0)
        operating_margin = data.get('operating_margin', 0)
        if gross_margin and gross_margin > 40:
            scores['business_quality'] += 10
            reasoning.append(f"High gross margins ({gross_margin:.1f}%) suggest pricing power")
        elif gross_margin and gross_margin > 25:
            scores['business_quality'] += 5
            reasoning.append(f"Decent gross margins ({gross_margin:.1f}%) show some competitive advantage")

        # Scale advantages
        market_cap = data.get('market_cap', 0)
        if market_cap > 100_000_000_000:  # >$100B
            scores['business_quality'] += 10
            reasoning.append("Massive scale provides competitive advantages and stability")
        elif market_cap > 10_000_000_000:  # >$10B
            scores['business_quality'] += 5
            reasoning.append("Significant scale offers competitive positioning")

        # Financial Strength (30 points)
        current_ratio = data.get('current_ratio', 0)
        if current_ratio > 2:
            scores['financial_strength'] += 10
            reasoning.append(f"Strong liquidity: {current_ratio:.1f}x current ratio")
        elif current_ratio > 1.5:
            scores['financial_strength'] += 5
            reasoning.append(f"Adequate liquidity: {current_ratio:.1f}x current ratio")

        debt_ratio = data.get('debt_to_equity', 0) / 100
        if debt_ratio < 0.5:
            scores['financial_strength'] += 10
            reasoning.append(f"Conservative debt: {debt_ratio:.1f}x equity")
        elif debt_ratio < 1.0:
            scores['financial_strength'] += 5
            reasoning.append(f"Manageable debt: {debt_ratio:.1f}x equity")

        # Cash generation
        free_cf = data.get('free_cash_flow', 0)
        net_income = data.get('net_income', 0)
        if free_cf > 0 and net_income > 0:
            cf_conversion = free_cf / net_income
            if cf_conversion > 0.9:
                scores['financial_strength'] += 10
                reasoning.append(f"Excellent cash conversion: {cf_conversion:.1f}x earnings become cash")
            elif cf_conversion > 0.7:
                scores['financial_strength'] += 5
                reasoning.append(f"Good cash conversion: {cf_conversion:.1f}x")

        # Management Alignment (15 points) - proxies
        # Large established companies likely have better governance
        if market_cap > 50_000_000_000:
            scores['management_alignment'] += 10
            reasoning.append("Large established company typically has professional management")

        # Dividend policy as alignment indicator
        div_yield = data.get('dividend_yield', 0)
        payout_ratio = data.get('payout_ratio', 0)
        if div_yield and div_yield > 1 and payout_ratio and payout_ratio < 60:
            scores['management_alignment'] += 5
            reasoning.append(f"Reasonable dividend policy ({div_yield:.1f}% yield, {payout_ratio:.1f}% payout)")

        # Valuation (15 points)
        pe_ratio = data.get('pe_ratio', 0)
        if pe_ratio and pe_ratio < 15:
            scores['valuation'] += 15
            reasoning.append(f"Attractive valuation: {pe_ratio:.1f}x P/E")
        elif pe_ratio and pe_ratio < 20:
            scores['valuation'] += 10
            reasoning.append(f"Fair valuation: {pe_ratio:.1f}x P/E")
        elif pe_ratio and pe_ratio < 25:
            scores['valuation'] += 5
            reasoning.append(f"Acceptable valuation: {pe_ratio:.1f}x P/E")

        scores['total'] = sum(scores.values()) - scores['total']  # Subtract to avoid double counting

        return {
            'score_breakdown': scores,
            'detailed_reasoning': reasoning,
            'scoring_rationale': f"Scored {scores['total']}/100 across business quality, financial strength, management, and valuation"
        }

    def _generate_recommendation(self, data: Dict, scoring: Dict, kill_switches: Dict) -> Dict[str, Any]:
        """Generate final recommendation with Munger voice"""

        company = data.get('company_name', data['symbol'])
        total_score = scoring['score_breakdown']['total']

        if total_score >= 80:
            decision = 'BUY'
            confidence = 'HIGH'
            voice = f"{company} scores {total_score}/100 - this is a high-quality business at a reasonable price. When you find a great company that meets our criteria, you don't overthink it."
        elif total_score >= 65:
            decision = 'HOLD'
            confidence = 'MEDIUM'
            voice = f"{company} scores {total_score}/100 - it's a solid business but not a fat pitch. Sometimes patience pays better than action."
        elif total_score >= 50:
            decision = 'AVOID'
            confidence = 'MEDIUM'
            voice = f"{company} scores {total_score}/100 - it's not terrible, but we have better places for our capital. Life's too short to own mediocre businesses."
        else:
            decision = 'AVOID'
            confidence = 'HIGH'
            voice = f"{company} scores only {total_score}/100 - this doesn't meet our standards. We'd rather put money in Treasury bills than poor businesses."

        return {
            'decision': decision,
            'confidence': confidence,
            'score': total_score,
            'voice': voice,
            'reasoning': scoring['detailed_reasoning'][:3],  # Top 3 reasons
            'strengths': [r for r in scoring['detailed_reasoning'] if any(word in r.lower() for word in ['excellent', 'strong', 'high', 'good'])],
            'concerns': [r for r in scoring['detailed_reasoning'] if any(word in r.lower() for word in ['low', 'poor', 'weak', 'concerning'])]
        }

    def _generate_rejection(self, data: Dict, kill_switches: Dict) -> Dict[str, Any]:
        """Generate rejection due to kill switches"""

        company = data.get('company_name', data['symbol'])
        primary_switch = kill_switches['triggered_switches'][0]

        return {
            'decision': 'REJECT',
            'confidence': 'HIGH',
            'score': 0,
            'voice': f"I'm rejecting {company} immediately. {primary_switch['munger_voice']}",
            'reasoning': [switch['reason'] for switch in kill_switches['triggered_switches']],
            'strengths': [],
            'concerns': [switch['reason'] for switch in kill_switches['triggered_switches']]
        }

    def _generate_follow_ups(self, recommendation: Dict) -> List[str]:
        """Generate contextual follow-up questions"""

        follow_ups = [
            "What are the biggest risks I should watch for?",
            "How does this compare to its industry peers?",
            "What would change your mind about this investment?"
        ]

        if recommendation['decision'] in ['BUY', 'HOLD']:
            follow_ups.append("At what price would you be even more interested?")
            follow_ups.append("What could cause this business to lose its competitive advantage?")

        if recommendation['decision'] == 'AVOID':
            follow_ups.append("What would need to change for you to reconsider?")

        follow_ups.append("What does this remind you of from your investing history?")

        return follow_ups

    def _generate_inversion_thinking(self, data: Dict[str, Any]) -> str:
        """Generate Munger-style inversion analysis"""

        company = data.get('company_name', data['symbol'])
        sector = data.get('sector', '')

        problems = []

        # Financial risks
        debt_ratio = data.get('debt_to_equity', 0) / 100
        if debt_ratio > 1:
            problems.append(f"Debt at {debt_ratio:.1f}x equity could cause trouble in a recession")

        pe_ratio = data.get('pe_ratio', 0)
        if pe_ratio and pe_ratio > 25:
            problems.append(f"High expectations at {pe_ratio:.1f}x P/E - any disappointment hurts badly")

        # Business model risks
        if sector == 'Technology':
            problems.append("Technology disruption can happen overnight")
        elif sector == 'Consumer Cyclical':
            problems.append("Consumer spending disappears first in recessions")
        elif 'Cyclical' in sector:
            problems.append("Cyclical businesses suffer badly in downturns")

        # Market risks
        market_cap = data.get('market_cap', 0)
        if market_cap < 10_000_000_000:
            problems.append("Smaller companies have less staying power in crises")

        if problems:
            risk_text = "; ".join(problems[:3])
            return f"Inverting on {company}: {risk_text}. The key isn't avoiding all risks - it's avoiding risks that can kill you."
        else:
            return f"{company} has a reasonably defensive profile, but all businesses face risks in severe downturns."

    def _prepare_conversation_context(self, recommendation: Dict, data: Dict) -> Dict[str, Any]:
        """Prepare context for ongoing conversation"""

        return {
            'persona': 'charlie_munger',
            'analysis_summary': {
                'company': data.get('company_name'),
                'symbol': data['symbol'],
                'recommendation': recommendation['decision'],
                'key_points': recommendation['reasoning'][:2],
                'main_concerns': recommendation.get('concerns', [])[:2]
            },
            'conversation_hooks': [
                f"This {recommendation['decision']} on {data.get('company_name', data['symbol'])} is based on",
                "The key factors that drove my analysis were",
                "What worries me most about this business is",
                "From my decades of experience, this reminds me of"
            ]
        }

    def _handle_data_error(self, financial_data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle cases where financial data couldn't be retrieved"""

        symbol = financial_data['symbol']
        error_msg = financial_data.get('error', 'Unknown error')

        return {
            'symbol': symbol,
            'analysis_type': 'charlie_munger',
            'recommendation': 'NO_ANALYSIS',
            'confidence': 'N/A',
            'munger_score': 0,
            'munger_voice': f"I can't analyze {symbol} without reliable data. {error_msg}. Show me the numbers, or I can't give you a proper assessment.",
            'key_reasoning': [f"Data retrieval failed: {error_msg}"],
            'kill_switches': [],
            'error_details': financial_data,
            'follow_up_suggestions': [
                "Please verify the stock symbol is correct",
                "Try again - sometimes data sources are temporarily unavailable",
                "Check if this is a recently IPO'd or delisted company"
            ]
        }