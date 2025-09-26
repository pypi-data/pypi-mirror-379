#!/usr/bin/env python3
"""
Financial Advisor MCP Server
Charlie Munger Investment Analysis Integration for Claude Code
"""

import asyncio
import json
from typing import Dict, Any, List, Optional
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool

from .data_provider import FinancialDataProvider
from .munger_persona import CharleMungerPersona


# Initialize MCP server
server = Server("financial-advisor")

# Initialize core components
data_provider = FinancialDataProvider()
munger = CharleMungerPersona()

# Conversation state management
conversation_state = {}


@server.list_tools()
async def handle_list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="analyze_stock_munger",
            description="Analyze a stock using Charlie Munger's investment framework",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock ticker symbol (e.g., 'AAPL', 'MSFT', 'BRK.A')"
                    }
                },
                "required": ["symbol"]
            }
        ),
        Tool(
            name="ask_munger_followup",
            description="Ask Charlie Munger follow-up questions about a previous analysis",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock ticker symbol from previous analysis"
                    },
                    "question_type": {
                        "type": "string",
                        "description": "Type of follow-up question",
                        "enum": ["explain_reasoning", "what_could_go_wrong", "historical_context", "peer_comparison", "price_sensitivity", "management_assessment"]
                    }
                },
                "required": ["symbol", "question_type"]
            }
        ),
        Tool(
            name="get_financial_data",
            description="Get comprehensive financial data for a stock",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock ticker symbol (e.g., 'AAPL', 'MSFT', 'BRK.A')"
                    }
                },
                "required": ["symbol"]
            }
        ),
        Tool(
            name="compare_stocks_munger",
            description="Compare multiple stocks using Munger's framework",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbols": {
                        "type": "string",
                        "description": "Comma-separated stock symbols (e.g., 'AAPL,MSFT,GOOGL')"
                    }
                },
                "required": ["symbols"]
            }
        ),
        Tool(
            name="clarify_company_identity",
            description="Get clarification on ambiguous company references before analysis",
            inputSchema={
                "type": "object",
                "properties": {
                    "company_reference": {
                        "type": "string",
                        "description": "Ambiguous company name or reference that needs clarification"
                    }
                },
                "required": ["company_reference"]
            }
        )
    ]


@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[dict]:
    """Handle tool calls."""

    if name == "analyze_stock_munger":
        result = analyze_stock_munger(arguments["symbol"])
    elif name == "ask_munger_followup":
        result = ask_munger_followup(arguments["symbol"], arguments["question_type"])
    elif name == "get_financial_data":
        result = get_financial_data(arguments["symbol"])
    elif name == "compare_stocks_munger":
        result = compare_stocks_munger(arguments["symbols"])
    elif name == "clarify_company_identity":
        result = clarify_company_identity(arguments["company_reference"])
    else:
        raise ValueError(f"Unknown tool: {name}")

    return [{"type": "text", "text": json.dumps(result, indent=2)}]


def analyze_stock_munger(symbol: str) -> dict:
    """
    Analyze a stock using Charlie Munger's investment framework.

    Provides comprehensive investment analysis including kill-switch checks,
    sophisticated scoring, and authentic Munger persona voice with follow-up suggestions.

    Args:
        symbol: Stock ticker symbol (e.g., 'AAPL', 'MSFT', 'BRK.A')

    Returns:
        Complete Munger-style investment analysis with recommendation
    """

    # Phase 0: Company Identification & Clarification
    symbol = symbol.upper().strip()

    # Basic symbol validation
    if not symbol or len(symbol) > 10:
        return {
            'success': False,
            'phase': 'clarification',
            'munger_response': "Hold on there. I need to be absolutely clear about which company you want me to analyze. Please provide the exact company name, ticker symbol, and primary exchange (e.g., 'Apple Inc. (AAPL, NASDAQ)' or 'Berkshire Hathaway (BRK.A, NYSE)'). At my age, I don't have time for guesswork.",
            'clarification_needed': True,
            'suggestion': 'Provide format: "Company Name (TICKER, Exchange)"'
        }

    # Get financial data
    financial_data = data_provider.get_financial_data(symbol)

    # Check if company was found and identified clearly
    if 'error' in financial_data:
        return {
            'success': False,
            'phase': 'clarification',
            'munger_response': f"I couldn't find reliable data for '{symbol}'. Before we waste any more time, please confirm: Are you asking about a publicly traded company? If so, provide the exact company name, ticker symbol, and exchange. I don't analyze what I can't understand.",
            'clarification_needed': True,
            'attempted_symbol': symbol,
            'suggestion': 'Verify ticker symbol and provide full company details'
        }

    # Verification step
    company_name = financial_data.get('company_name', 'Unknown Company')
    sector = financial_data.get('sector', 'Unknown')

    verification_response = f"Analyzing {company_name} ({symbol}) in the {sector} sector - is this the correct company you want me to evaluate?"

    # Apply Munger analysis
    analysis = munger.analyze_investment(financial_data)

    # Store conversation context
    conversation_state[symbol.upper()] = {
        'last_analysis': analysis,
        'timestamp': analysis['data_quality']['analysis_time_seconds']
    }

    return {
        'success': True,
        'phase': 'analysis_complete',
        'verification_step': verification_response,
        'analysis': analysis,
        'conversation_ready': True,
        'usage_note': 'Use ask_munger_followup() for deeper questions about this analysis'
    }


def ask_munger_followup(symbol: str, question_type: str) -> dict:
    """
    Ask Charlie Munger follow-up questions about a previous analysis.

    Provides deeper insights using Munger's mental models and experience.
    Must be used after analyze_stock_munger().

    Args:
        symbol: Stock ticker symbol from previous analysis
        question_type: Type of follow-up question:
            - "explain_reasoning": Detailed explanation of the analysis
            - "what_could_go_wrong": Inversion thinking - potential problems
            - "historical_context": What this reminds Munger of historically
            - "peer_comparison": How this compares to industry peers
            - "price_sensitivity": At what price would recommendation change
            - "management_assessment": Thoughts on company leadership

    Returns:
        Munger's response to the specific follow-up question
    """

    symbol = symbol.upper()

    # Check if we have prior analysis
    if symbol not in conversation_state:
        return {
            'success': False,
            'error': f'No previous analysis found for {symbol}. Please run analyze_stock_munger() first.',
            'suggestion': f'Try: analyze_stock_munger("{symbol}")'
        }

    prior_analysis = conversation_state[symbol]['last_analysis']

    # Generate contextual follow-up response
    response = _generate_followup_response(question_type, prior_analysis)

    return {
        'success': True,
        'symbol': symbol,
        'question_type': question_type,
        'munger_response': response,
        'conversation_context': prior_analysis.get('conversation_context', {}),
        'available_followups': prior_analysis.get('follow_up_suggestions', [])
    }


def get_financial_data(symbol: str) -> dict:
    """
    Get comprehensive financial data for a stock.

    Provides raw financial metrics, ratios, and business information
    without investment analysis. Useful for custom analysis or data exploration.

    Args:
        symbol: Stock ticker symbol (e.g., 'AAPL', 'MSFT', 'BRK.A')

    Returns:
        Comprehensive financial data with quality metrics
    """

    data = data_provider.get_financial_data(symbol.upper())

    if 'error' in data:
        return {
            'success': False,
            'symbol': symbol.upper(),
            'error': data['error'],
            'attempted_symbols': data.get('attempted_symbols', []),
            'suggestion': 'Verify the ticker symbol is correct and the company is publicly traded'
        }

    return {
        'success': True,
        'symbol': symbol.upper(),
        'financial_data': data,
        'data_summary': {
            'company': data.get('company_name', 'Unknown'),
            'sector': data.get('sector', 'Unknown'),
            'market_cap_billions': round(data.get('market_cap', 0) / 1_000_000_000, 1),
            'completeness_score': data.get('completeness_score', 0),
            'data_freshness': data.get('data_freshness', 'unknown')
        }
    }


def clarify_company_identity(company_reference: str) -> dict:
    """
    Handle ambiguous company references by searching for possible matches.

    Args:
        company_reference: Unclear or ambiguous company name/reference

    Returns:
        Munger-style clarification with search results
    """

    # Try to get basic financial data to see if it's already a valid ticker
    potential_symbol = company_reference.upper().strip()
    financial_data = data_provider.get_financial_data(potential_symbol)

    if 'error' not in financial_data:
        # Found a match - return verification
        company_name = financial_data.get('company_name', 'Unknown')
        sector = financial_data.get('sector', 'Unknown')
        return {
            'success': True,
            'phase': 'verification',
            'munger_response': f"I found {company_name} ({potential_symbol}) in the {sector} sector. Is this the company you want me to analyze? If so, I can proceed with the full Munger framework analysis.",
            'found_company': {
                'name': company_name,
                'symbol': potential_symbol,
                'sector': sector
            },
            'next_step': f"If correct, use analyze_stock_munger('{potential_symbol}') to proceed"
        }

    # If not found directly, try searching for matches
    search_results = data_provider.search_companies(company_reference, max_results=5)

    if search_results and 'error' not in search_results[0]:
        # Found potential matches
        munger_response = f"You mentioned '{company_reference}', and I found several possible matches. "
        munger_response += "At my age, I don't like ambiguity. Here are the companies I found:\n\n"

        matches = []
        for i, result in enumerate(search_results[:3], 1):
            munger_response += f"{i}. {result['name']} ({result['symbol']}) - {result['sector']}\n"
            matches.append({
                'rank': i,
                'name': result['name'],
                'symbol': result['symbol'],
                'sector': result['sector'],
                'match_type': result.get('match_type', 'unknown')
            })

        munger_response += f"\nPlease specify which one you want analyzed by providing the exact ticker symbol (e.g., '{search_results[0]['symbol']}')."

        return {
            'success': True,
            'phase': 'multiple_matches',
            'munger_response': munger_response,
            'search_results': matches,
            'clarification_needed': True,
            'next_step': 'Use analyze_stock_munger() with the specific ticker symbol you want'
        }

    # No matches found
    munger_response = f"You mentioned '{company_reference}', but I couldn't find any matches in my data. "

    # Check if it might be a partial company name
    if len(company_reference) > 4 and not company_reference.isupper():
        munger_response += "It looks like you might have given me a company name rather than a ticker symbol. "

    munger_response += "At 99 years old, I've learned not to guess. Please provide the exact ticker symbol for the publicly traded company you want analyzed. "
    munger_response += "For international stocks, remember to include the exchange suffix (e.g., 'PNDORA.CO' for Pandora on Copenhagen Exchange)."

    return {
        'success': False,
        'phase': 'not_found',
        'munger_response': munger_response,
        'clarification_needed': True,
        'attempted_reference': company_reference,
        'guidance': 'Provide the exact ticker symbol with exchange suffix if needed (e.g., AAPL, MSFT, PNDORA.CO)',
        'next_step': 'Once you have the ticker symbol, use analyze_stock_munger() with that symbol'
    }


def compare_stocks_munger(symbols: str) -> dict:
    """
    Compare multiple stocks using Munger's framework.

    Analyzes up to 5 stocks simultaneously and ranks them according to
    Munger's investment criteria with comparative insights.

    Args:
        symbols: Comma-separated stock symbols (e.g., 'AAPL,MSFT,GOOGL')

    Returns:
        Comparative analysis with Munger's rankings and insights
    """

    # Parse and validate symbols
    symbols = symbols.strip()
    if not symbols:
        return {
            'success': False,
            'phase': 'clarification',
            'munger_response': "You asked me to compare stocks but didn't specify which ones. Give me a comma-separated list of ticker symbols like 'AAPL,MSFT,GOOGL'. I can't analyze thin air.",
            'clarification_needed': True,
            'expected_format': 'AAPL,MSFT,GOOGL'
        }

    symbol_list = [s.strip().upper() for s in symbols.split(',') if s.strip()]

    if len(symbol_list) > 5:
        return {
            'success': False,
            'error': 'Maximum 5 stocks supported for comparison',
            'provided_count': len(symbol_list)
        }

    if len(symbol_list) < 2:
        return {
            'success': False,
            'error': 'Minimum 2 stocks required for comparison',
            'suggestion': 'Provide comma-separated symbols like: AAPL,MSFT,GOOGL'
        }

    # Analyze each stock
    analyses = []
    for symbol in symbol_list:
        financial_data = data_provider.get_financial_data(symbol)
        if 'error' not in financial_data:
            analysis = munger.analyze_investment(financial_data)
            analyses.append(analysis)

    if not analyses:
        return {
            'success': False,
            'error': 'Could not retrieve data for any of the provided symbols',
            'symbols_attempted': symbol_list
        }

    # Rank and compare
    ranked_analyses = sorted(analyses, key=lambda x: x['munger_score'], reverse=True)

    # Generate comparative insights
    comparison_insights = _generate_comparison_insights(ranked_analyses)

    return {
        'success': True,
        'symbols_compared': [a['symbol'] for a in ranked_analyses],
        'munger_ranking': [
            {
                'rank': i + 1,
                'symbol': analysis['symbol'],
                'company': analysis['company_name'],
                'recommendation': analysis['recommendation'],
                'score': analysis['munger_score'],
                'key_strength': analysis['key_reasoning'][0] if analysis['key_reasoning'] else 'N/A'
            }
            for i, analysis in enumerate(ranked_analyses)
        ],
        'comparison_insights': comparison_insights,
        'detailed_analyses': ranked_analyses
    }


def _generate_followup_response(question_type: str, analysis: Dict[str, Any]) -> str:
    """Generate contextual follow-up responses in Munger's voice"""

    company = analysis['company_name']
    symbol = analysis['symbol']
    recommendation = analysis['recommendation']

    if question_type == "explain_reasoning":
        response = f"You want to understand my thinking on {company}? Fair enough. "
        if analysis.get('kill_switches'):
            response += f"First, this triggered my kill switches: {analysis['kill_switches'][0]['reason']}. "
        response += "Here's what I analyzed: " + "; ".join(analysis['key_reasoning'][:3]) + ". "
        response += "At my age, I've learned to focus on what can go wrong before getting excited about what might go right."

    elif question_type == "what_could_go_wrong":
        response = analysis.get('inversion_analysis', f"Let me think about what could hurt {company} shareholders...")

    elif question_type == "historical_context":
        if recommendation == 'BUY':
            response = f"{company} reminds me of the great businesses we found decades ago - not flashy, but reliable wealth creators. "
        elif recommendation in ['REJECT', 'AVOID']:
            response = f"{company} has the hallmarks of investments that have burned shareholders throughout history. "
        else:
            response = f"{company} is like many decent businesses I've seen - not bad enough to avoid, not good enough to get excited about. "
        response += "The patterns repeat because human nature doesn't change."

    elif question_type == "peer_comparison":
        response = f"You're asking how {company} compares to its peers. Here's what I think: "
        response += "I don't really care about being the best of a mediocre bunch. "
        response += "If the whole industry is overpriced or structurally challenged, that doesn't make one company attractive. "
        response += "We look for businesses that would be compelling even if they were the only game in town."

    elif question_type == "price_sensitivity":
        score = analysis['munger_score']
        if score > 70:
            response = f"Even with {company}'s quality, price matters enormously. "
            response += "A 20-30% lower price would make this much more compelling. "
        elif score < 50:
            response = f"For {company}, even a big price drop wouldn't fix the fundamental issues. "
            response += "Some businesses aren't worth owning at any price."
        else:
            response = f"{company} might become interesting at a significantly lower valuation. "
            response += "Quality businesses occasionally get marked down to bargain prices."
        response += "We'd rather buy wonderful companies at fair prices than fair companies at wonderful prices."

    elif question_type == "management_assessment":
        response = f"Judging {company}'s management from the outside is tricky. "
        response += "I look at capital allocation, compensation structures, and whether they're building long-term value or playing short-term games. "
        response += "Show me the incentive and I'll show you the outcome - that's how you evaluate management."

    else:
        response = f"That's an interesting question about {company}. Let me think through that using my framework..."

    return response


def _generate_comparison_insights(ranked_analyses: List[Dict[str, Any]]) -> str:
    """Generate Munger-style insights from stock comparison"""

    if not ranked_analyses:
        return "No valid analyses to compare."

    best = ranked_analyses[0]
    worst = ranked_analyses[-1]

    insights = f"Looking at this group, {best['company_name']} stands out with a score of {best['munger_score']}/100. "

    if best['recommendation'] == 'BUY':
        insights += "It's the only one I'd consider putting significant capital into. "
    else:
        insights += "But even the best of this bunch isn't compelling enough for a strong recommendation. "

    if len(ranked_analyses) > 2:
        insights += f"The spread from {best['munger_score']} to {worst['munger_score']} shows you the difference between "
        insights += "quality businesses and mediocre ones. "

    insights += "Remember: it's better to own a piece of a wonderful company than a whole mediocre one."

    return insights


async def main():
    """Main entry point for the MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())