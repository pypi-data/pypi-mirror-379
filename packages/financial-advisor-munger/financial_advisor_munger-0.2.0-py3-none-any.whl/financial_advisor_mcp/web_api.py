#!/usr/bin/env python3
"""
Charlie Munger Investment Analysis - Web API
Universal HTTP REST API wrapper for the MCP server functionality
"""

import asyncio
import json
from typing import Dict, Any, Optional, List
from contextlib import asynccontextmanager

try:
    from fastapi import FastAPI, HTTPException, BackgroundTasks
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.responses import JSONResponse
    from pydantic import BaseModel, Field
    import uvicorn
except ImportError:
    raise ImportError("Web API dependencies not installed. Run: pip install 'financial-advisor-munger[web]'")

from .data_provider import FinancialDataProvider
from .munger_persona import CharleMungerPersona

# Global instances
data_provider = None
munger_persona = None
conversation_state = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    global data_provider, munger_persona
    data_provider = FinancialDataProvider()
    munger_persona = CharleMungerPersona()
    yield
    # Shutdown
    data_provider = None
    munger_persona = None

# Initialize FastAPI app
app = FastAPI(
    title="Charlie Munger Investment Analysis API",
    description="AI-powered investment analysis using Charlie Munger's framework and wisdom",
    version="0.2.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Add CORS middleware for web apps
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class StockAnalysisRequest(BaseModel):
    symbol: str = Field(..., description="Stock ticker symbol (e.g., AAPL, MSFT, PNDORA.CO)")

class FollowupRequest(BaseModel):
    symbol: str = Field(..., description="Stock ticker symbol from previous analysis")
    question_type: str = Field(
        ...,
        description="Type of follow-up question",
        pattern="^(explain_reasoning|what_could_go_wrong|historical_context|peer_comparison|price_sensitivity|management_assessment)$"
    )

class CompareStocksRequest(BaseModel):
    symbols: str = Field(..., description="Comma-separated ticker symbols (e.g., 'AAPL,MSFT,GOOGL')")

class CompanySearchRequest(BaseModel):
    query: str = Field(..., description="Company name or partial name to search")
    max_results: int = Field(5, ge=1, le=20, description="Maximum number of results")

class HealthResponse(BaseModel):
    status: str = "healthy"
    version: str = "0.2.0"
    services: Dict[str, str] = {}

# API Endpoints
@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint with API information"""
    return {
        "name": "Charlie Munger Investment Analysis API",
        "version": "0.2.0",
        "description": "AI-powered investment analysis using Charlie Munger's framework",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""

    services = {}

    # Test data provider
    try:
        test_data = data_provider.get_financial_data("AAPL")
        services["data_provider"] = "healthy" if 'error' not in test_data else "degraded"
    except Exception:
        services["data_provider"] = "unhealthy"

    # Test search
    try:
        search_results = data_provider.search_companies("Apple", max_results=1)
        services["search"] = "healthy" if search_results and 'error' not in search_results[0] else "degraded"
    except Exception:
        services["search"] = "unhealthy"

    return HealthResponse(services=services)

@app.post("/analyze", response_model=Dict[str, Any])
async def analyze_stock(request: StockAnalysisRequest):
    """
    Analyze a stock using Charlie Munger's investment framework

    Returns comprehensive analysis including kill-switch checks, scoring, and Munger's authentic voice.
    """

    try:
        symbol = request.symbol.upper().strip()

        # Basic validation
        if not symbol or len(symbol) > 10:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "error": "Invalid ticker symbol",
                    "munger_response": "Hold on there. I need a proper ticker symbol, not whatever that was. Give me something like 'AAPL' or 'BRK.A'."
                }
            )

        # Get financial data
        financial_data = data_provider.get_financial_data(symbol)

        if 'error' in financial_data:
            return JSONResponse(
                status_code=404,
                content={
                    "success": False,
                    "error": f"Could not find data for {symbol}",
                    "munger_response": f"I couldn't find reliable data for '{symbol}'. Are you sure that's a real ticker symbol? Double-check it and try again."
                }
            )

        # Apply Munger analysis
        analysis = munger_persona.analyze_investment(financial_data)

        # Store conversation context
        conversation_state[symbol] = {
            'last_analysis': analysis,
            'timestamp': analysis['data_quality']['analysis_time_seconds']
        }

        return {
            "success": True,
            "symbol": symbol,
            "company": financial_data.get('company_name', 'Unknown'),
            "analysis": analysis,
            "conversation_ready": True,
            "api_note": "Use /followup endpoint for deeper questions about this analysis"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.post("/followup", response_model=Dict[str, Any])
async def ask_followup(request: FollowupRequest):
    """
    Ask Charlie Munger follow-up questions about a previous analysis

    Provides deeper insights using Munger's mental models and experience.
    Must be used after /analyze endpoint.
    """

    try:
        symbol = request.symbol.upper()

        # Check if we have prior analysis
        if symbol not in conversation_state:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "error": f"No previous analysis found for {symbol}",
                    "munger_response": f"I haven't analyzed {symbol} yet. Run the analysis first, then come back with your follow-up questions."
                }
            )

        prior_analysis = conversation_state[symbol]['last_analysis']

        # Generate contextual follow-up response (reuse server logic)
        from .server import _generate_followup_response
        response = _generate_followup_response(request.question_type, prior_analysis)

        return {
            "success": True,
            "symbol": symbol,
            "question_type": request.question_type,
            "munger_response": response,
            "conversation_context": prior_analysis.get('conversation_context', {}),
            "available_followups": prior_analysis.get('follow_up_suggestions', [])
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Follow-up failed: {str(e)}")

@app.post("/compare", response_model=Dict[str, Any])
async def compare_stocks(request: CompareStocksRequest):
    """
    Compare multiple stocks using Munger's framework

    Analyzes up to 5 stocks simultaneously and ranks them according to Munger's criteria.
    """

    try:
        # Parse symbols
        symbol_list = [s.strip().upper() for s in request.symbols.split(',') if s.strip()]

        if len(symbol_list) > 5:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "error": "Maximum 5 stocks supported",
                    "munger_response": "I'm not running a factory here. Give me 5 stocks or fewer - quality over quantity."
                }
            )

        if len(symbol_list) < 2:
            return JSONResponse(
                status_code=400,
                content={
                    "success": False,
                    "error": "Minimum 2 stocks required",
                    "munger_response": "You need at least 2 stocks to compare. What am I supposed to compare one stock against - thin air?"
                }
            )

        # Analyze each stock
        analyses = []
        for symbol in symbol_list:
            financial_data = data_provider.get_financial_data(symbol)
            if 'error' not in financial_data:
                analysis = munger_persona.analyze_investment(financial_data)
                analyses.append(analysis)

        if not analyses:
            return JSONResponse(
                status_code=404,
                content={
                    "success": False,
                    "error": "Could not retrieve data for any symbols",
                    "munger_response": f"None of these symbols worked: {', '.join(symbol_list)}. Check your ticker symbols and try again."
                }
            )

        # Rank and compare (reuse server logic)
        ranked_analyses = sorted(analyses, key=lambda x: x['munger_score'], reverse=True)
        from .server import _generate_comparison_insights
        comparison_insights = _generate_comparison_insights(ranked_analyses)

        return {
            "success": True,
            "symbols_compared": [a['symbol'] for a in ranked_analyses],
            "munger_ranking": [
                {
                    "rank": i + 1,
                    "symbol": analysis['symbol'],
                    "company": analysis['company_name'],
                    "recommendation": analysis['recommendation'],
                    "score": analysis['munger_score'],
                    "key_strength": analysis['key_reasoning'][0] if analysis['key_reasoning'] else 'N/A'
                }
                for i, analysis in enumerate(ranked_analyses)
            ],
            "comparison_insights": comparison_insights,
            "detailed_analyses": ranked_analyses
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Comparison failed: {str(e)}")

@app.post("/search", response_model=Dict[str, Any])
async def search_companies(request: CompanySearchRequest):
    """
    Search for companies by name or ticker symbol

    Uses Yahoo Finance search API for fast, comprehensive results.
    """

    try:
        results = data_provider.search_companies(request.query, max_results=request.max_results)

        return {
            "success": True,
            "query": request.query,
            "results": results,
            "count": len(results)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")

@app.get("/data/{symbol}", response_model=Dict[str, Any])
async def get_financial_data(symbol: str):
    """
    Get raw financial data for a stock

    Provides comprehensive financial metrics without Munger analysis.
    """

    try:
        symbol = symbol.upper()
        data = data_provider.get_financial_data(symbol)

        if 'error' in data:
            return JSONResponse(
                status_code=404,
                content={
                    "success": False,
                    "error": data['error'],
                    "symbol": symbol
                }
            )

        return {
            "success": True,
            "symbol": symbol,
            "financial_data": data,
            "data_summary": {
                "company": data.get('company_name', 'Unknown'),
                "sector": data.get('sector', 'Unknown'),
                "market_cap_billions": round(data.get('market_cap', 0) / 1_000_000_000, 1),
                "completeness_score": data.get('completeness_score', 0)
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Data retrieval failed: {str(e)}")

# CLI entry point
def main():
    """Main entry point for web API server"""
    import argparse

    parser = argparse.ArgumentParser(description="Charlie Munger Investment Analysis Web API")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind to")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload for development")

    args = parser.parse_args()

    print("🎯 Starting Charlie Munger Investment Analysis Web API")
    print(f"📡 Server: http://{args.host}:{args.port}")
    print(f"📖 Docs: http://{args.host}:{args.port}/docs")
    print("💡 Tip: Try POST /analyze with {'symbol': 'AAPL'}")

    uvicorn.run(
        "financial_advisor_mcp.web_api:app",
        host=args.host,
        port=args.port,
        reload=args.reload
    )

if __name__ == "__main__":
    main()