"""
Financial Data Provider
Enhanced version from validation testing with robust error handling
"""

import yfinance as yf
import pandas as pd
import requests
from datetime import datetime
from typing import Dict, Any, Optional, List
import warnings
warnings.filterwarnings('ignore')


class FinancialDataProvider:
    """Provides reliable financial data with validation and error handling"""

    def __init__(self):
        self.cache = {}  # Simple in-memory cache
        self.cache_duration = 300  # 5 minutes in seconds
        self.search_cache = {}  # Cache for search results
        self.failed_tickers = set()  # Cache failed ticker lookups

    def get_financial_data(self, symbol: str) -> Dict[str, Any]:
        """Get comprehensive financial data with validation"""

        # Check cache first
        cache_key = f"{symbol}_{int(datetime.now().timestamp() // self.cache_duration)}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        # Handle special symbols (like BRK.A)
        symbols_to_try = self._get_symbol_variations(symbol)

        for test_symbol in symbols_to_try:
            try:
                data = self._fetch_symbol_data(test_symbol, symbol)
                if data and 'error' not in data:
                    # Cache successful result
                    self.cache[cache_key] = data
                    return data
            except Exception as e:
                continue

        # All symbols failed
        error_result = {
            'error': f"Unable to retrieve data for {symbol}",
            'symbol': symbol,
            'attempted_symbols': symbols_to_try
        }
        return error_result

    def _get_symbol_variations(self, symbol: str) -> List[str]:
        """Get variations of symbol to try"""
        if symbol == 'BRK.A':
            return ['BRK-A', 'BRK.B', 'BRK-B']
        elif symbol == 'BRK.B':
            return ['BRK-B', 'BRK.B', 'BRK-A']
        else:
            return [symbol]

    def _fetch_symbol_data(self, test_symbol: str, original_symbol: str) -> Dict[str, Any]:
        """Fetch and validate data for a specific symbol"""

        stock = yf.Ticker(test_symbol)
        info = stock.info
        financials = stock.financials
        balance_sheet = stock.balance_sheet
        cashflow = stock.cashflow

        # Basic validation
        if not info or len(info) < 5:
            raise ValueError(f"Insufficient data for {test_symbol}")

        # Extract and validate key metrics
        raw_data = {
            'symbol': original_symbol,
            'actual_symbol_used': test_symbol,
            'company_name': info.get('longName', 'Unknown'),
            'sector': info.get('sector', 'Unknown'),
            'industry': info.get('industry', 'Unknown'),
            'market_cap': info.get('marketCap', 0),
            'enterprise_value': info.get('enterpriseValue', 0),

            # Core Munger Metrics
            'roe': self._validate_percentage(info.get('returnOnEquity')),
            'roa': self._validate_percentage(info.get('returnOnAssets')),
            'debt_to_equity': info.get('debtToEquity', 0),
            'current_ratio': info.get('currentRatio', 0),
            'quick_ratio': info.get('quickRatio', 0),
            'gross_margin': self._validate_percentage(info.get('grossMargins')),
            'operating_margin': self._validate_percentage(info.get('operatingMargins')),
            'profit_margin': self._validate_percentage(info.get('profitMargins')),

            # Valuation Metrics
            'pe_ratio': info.get('forwardPE', info.get('trailingPE')),
            'pb_ratio': info.get('priceToBook'),
            'ps_ratio': info.get('priceToSalesTrailing12Months'),
            'peg_ratio': info.get('pegRatio'),

            # Financial Statements
            'revenue': self._get_recent_value(financials, 'Total Revenue'),
            'net_income': self._get_recent_value(financials, 'Net Income'),
            'total_assets': self._get_recent_value(balance_sheet, 'Total Assets'),
            'total_debt': self._get_recent_value(balance_sheet, 'Total Debt'),
            'free_cash_flow': info.get('freeCashflow', 0),
            'operating_cash_flow': info.get('operatingCashflow', 0),

            # Growth Metrics
            'revenue_growth': info.get('revenueGrowth'),
            'earnings_growth': info.get('earningsGrowth'),

            # Additional Context
            'beta': info.get('beta'),
            'dividend_yield': self._validate_percentage(info.get('dividendYield')),
            'payout_ratio': self._validate_percentage(info.get('payoutRatio')),

            # Business Info
            'business_summary': info.get('longBusinessSummary', '')[:500],  # Truncate
            'website': info.get('website', ''),
            'employees': info.get('fullTimeEmployees'),
            'headquarters': f"{info.get('city', '')}, {info.get('country', '')}".strip(', '),

            # Data Quality
            'data_timestamp': datetime.now().isoformat(),
            'source': 'yfinance',
            'data_freshness': 'live',
            'completeness_score': self._calculate_completeness(info, financials, balance_sheet)
        }

        # Add validation flags
        raw_data['validation_flags'] = self._validate_data_quality(raw_data)

        return raw_data

    def _validate_percentage(self, value: Any) -> Optional[float]:
        """Convert and validate percentage values"""
        if value is None:
            return None
        try:
            # Convert to percentage if it's a decimal
            pct = float(value) * 100 if float(value) <= 1 else float(value)
            return round(pct, 2)
        except (ValueError, TypeError):
            return None

    def _get_recent_value(self, df: pd.DataFrame, column: str) -> Optional[float]:
        """Get most recent value from financial statement"""
        if df.empty or column not in df.index:
            return None
        try:
            return float(df.loc[column].iloc[0])
        except (IndexError, ValueError, TypeError):
            return None

    def _calculate_completeness(self, info: Dict, financials: pd.DataFrame, balance_sheet: pd.DataFrame) -> float:
        """Calculate data completeness score"""

        # Critical fields (weight = 3)
        critical_fields = ['longName', 'sector', 'marketCap', 'returnOnEquity']
        critical_score = sum(3 for field in critical_fields if info.get(field) is not None)

        # Important fields (weight = 2)
        important_fields = ['debtToEquity', 'currentRatio', 'trailingPE', 'grossMargins']
        important_score = sum(2 for field in important_fields if info.get(field) is not None)

        # Nice-to-have fields (weight = 1)
        nice_fields = ['beta', 'dividendYield', 'website', 'longBusinessSummary']
        nice_score = sum(1 for field in nice_fields if info.get(field) is not None)

        # Financial statements bonus
        financials_bonus = 5 if not financials.empty else 0
        balance_sheet_bonus = 5 if not balance_sheet.empty else 0

        total_possible = len(critical_fields) * 3 + len(important_fields) * 2 + len(nice_fields) + 10
        total_achieved = critical_score + important_score + nice_score + financials_bonus + balance_sheet_bonus

        return round((total_achieved / total_possible) * 100, 1)

    def _validate_data_quality(self, data: Dict[str, Any]) -> List[str]:
        """Validate data quality and return warning flags"""
        flags = []

        # Check for extreme values
        roe = data.get('roe')
        if roe and roe > 100:
            flags.append('extreme_roe')
        elif roe and roe < -50:
            flags.append('negative_roe')

        debt_ratio = data.get('debt_to_equity', 0)
        if debt_ratio > 500:
            flags.append('extreme_debt')

        pe_ratio = data.get('pe_ratio')
        if pe_ratio and pe_ratio > 100:
            flags.append('extreme_pe')
        elif pe_ratio and pe_ratio < 0:
            flags.append('negative_pe')

        # Check completeness
        if data.get('completeness_score', 0) < 60:
            flags.append('low_completeness')

        return flags

    def get_multiple_stocks(self, symbols: List[str]) -> Dict[str, Any]:
        """Get data for multiple stocks efficiently"""

        results = {}
        for symbol in symbols:
            results[symbol] = self.get_financial_data(symbol)

        return {
            'results': results,
            'summary': {
                'total_requested': len(symbols),
                'successful': len([r for r in results.values() if 'error' not in r]),
                'failed': len([r for r in results.values() if 'error' in r])
            }
        }

    def search_companies(self, query: str, max_results: int = 10) -> List[Dict[str, str]]:
        """
        Fast company search using Yahoo Finance's undocumented search API

        Args:
            query: Company name or ticker symbol to search for
            max_results: Maximum number of results to return

        Returns:
            List of matching companies with symbol, name, and type
        """

        # Check search cache first
        cache_key = f"search_{query.lower()}_{max_results}"
        cache_time_key = f"{cache_key}_{int(datetime.now().timestamp() // self.cache_duration)}"

        if cache_time_key in self.search_cache:
            return self.search_cache[cache_time_key]

        try:
            # Use Yahoo Finance search API
            search_results = self._yahoo_finance_search(query, max_results)

            # Cache and return results
            self.search_cache[cache_time_key] = search_results
            return search_results

        except Exception as e:
            error_result = [{'error': f'Search failed: {str(e)}'}]
            self.search_cache[cache_time_key] = error_result
            return error_result

    def _yahoo_finance_search(self, query: str, max_results: int = 10) -> List[Dict[str, str]]:
        """
        Use Yahoo Finance's undocumented search API for fast company lookup
        """

        try:
            # Yahoo Finance search endpoint
            url = "https://query1.finance.yahoo.com/v1/finance/search"

            params = {
                'q': query,
                'lang': 'en',
                'region': 'US',
                'quotesCount': max_results,
                'newsCount': 0  # We don't need news
            }

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            response = requests.get(url, params=params, headers=headers, timeout=10)
            response.raise_for_status()

            data = response.json()

            results = []
            quotes = data.get('quotes', [])

            for quote in quotes[:max_results]:
                # Filter for stocks only (skip ETFs, options, etc.)
                quote_type = quote.get('quoteType', '').upper()
                if quote_type in ['EQUITY', 'STOCK']:
                    results.append({
                        'symbol': quote.get('symbol', ''),
                        'name': quote.get('longname') or quote.get('shortname', 'Unknown'),
                        'sector': 'Unknown',  # Yahoo search doesn't include sector
                        'exchange': quote.get('exchange', 'Unknown'),
                        'market_cap': 0,  # Not available in search results
                        'match_type': 'yahoo_search',
                        'score': quote.get('score', 0)
                    })

            # Sort by score (highest first)
            results.sort(key=lambda x: x.get('score', 0), reverse=True)

            return results

        except requests.exceptions.RequestException as e:
            # Fallback to local search if Yahoo API fails
            return self._fallback_search(query, max_results)
        except Exception as e:
            return [{'error': f'Yahoo search failed: {str(e)}'}]

    def _fallback_search(self, query: str, max_results: int = 10) -> List[Dict[str, str]]:
        """
        Fallback search using optimized local matching when Yahoo API fails
        """

        search_results = []
        query_upper = query.upper().strip()

        # Method 1: Direct ticker lookup
        if len(query) <= 6 and query.isupper():
            direct_result = self._fast_ticker_lookup(query_upper)
            if direct_result:
                search_results.append(direct_result)

        # Method 2: Common mappings for fallback
        if len(search_results) < max_results and len(query) > 4 and not query.isupper():
            fuzzy_results = self._optimized_fuzzy_search(query, max_results - len(search_results))
            search_results.extend(fuzzy_results)

        return search_results[:max_results]

    def _fast_ticker_lookup(self, ticker: str) -> Optional[Dict[str, str]]:
        """Fast lookup for direct ticker match"""

        # Skip if we know this ticker fails
        if ticker in self.failed_tickers:
            return None

        try:
            # Check our main cache first
            financial_data = self.get_financial_data(ticker)
            if 'error' not in financial_data:
                return {
                    'symbol': ticker,
                    'name': financial_data.get('company_name', 'Unknown'),
                    'sector': financial_data.get('sector', 'Unknown'),
                    'exchange': financial_data.get('exchange', 'Unknown'),
                    'market_cap': financial_data.get('market_cap', 0),
                    'match_type': 'ticker_exact'
                }
            else:
                self.failed_tickers.add(ticker)
                return None

        except Exception:
            self.failed_tickers.add(ticker)
            return None

    def _priority_exchange_search(self, base_ticker: str, max_results: int) -> List[Dict[str, str]]:
        """Search exchanges in priority order based on common usage"""

        results = []

        # Priority order: most common international exchanges first
        priority_exchanges = [
            ('.CO', 'Copenhagen'),  # Nordic companies
            ('.L', 'London'),       # European companies
            ('.TO', 'Toronto'),     # Canadian companies
            ('.AX', 'Australia'),   # Australian companies
            ('.ST', 'Stockholm'),   # Swedish companies
            ('.PA', 'Paris'),       # French companies
            ('.DE', 'Frankfurt'),   # German companies
        ]

        for suffix, exchange_name in priority_exchanges:
            if len(results) >= max_results:
                break

            ticker_with_suffix = f"{base_ticker}{suffix}"

            # Skip if we know this fails
            if ticker_with_suffix in self.failed_tickers:
                continue

            try:
                financial_data = self.get_financial_data(ticker_with_suffix)
                if 'error' not in financial_data:
                    results.append({
                        'symbol': ticker_with_suffix,
                        'name': financial_data.get('company_name', 'Unknown'),
                        'sector': financial_data.get('sector', 'Unknown'),
                        'exchange': exchange_name,
                        'market_cap': financial_data.get('market_cap', 0),
                        'match_type': 'ticker_with_suffix'
                    })
                else:
                    self.failed_tickers.add(ticker_with_suffix)

            except Exception:
                self.failed_tickers.add(ticker_with_suffix)
                continue

        return results

    def _optimized_fuzzy_search(self, company_name: str, max_results: int) -> List[Dict[str, str]]:
        """Optimized fuzzy search using pre-defined mappings and smart patterns"""

        results = []
        query_lower = company_name.lower()

        # Enhanced common mappings - more comprehensive
        common_mappings = {
            'apple': ['AAPL'],
            'microsoft': ['MSFT'],
            'google': ['GOOGL', 'GOOG'],
            'alphabet': ['GOOGL', 'GOOG'],
            'amazon': ['AMZN'],
            'tesla': ['TSLA'],
            'meta': ['META'],
            'facebook': ['META'],
            'netflix': ['NFLX'],
            'pandora': ['PNDORA.CO', 'P'],
            'berkshire': ['BRK.A', 'BRK.B'],
            'walmart': ['WMT'],
            'coca cola': ['KO'],
            'mcdonalds': ['MCD'],
            'disney': ['DIS'],
            'nike': ['NKE'],
            'visa': ['V'],
            'mastercard': ['MA'],
            'nvidia': ['NVDA'],
            'intel': ['INTC'],
            'amd': ['AMD'],
            'oracle': ['ORCL'],
            'salesforce': ['CRM'],
            'adobe': ['ADBE'],
            'paypal': ['PYPL'],
            'uber': ['UBER'],
            'airbnb': ['ABNB'],
            'spotify': ['SPOT'],
            'zoom': ['ZM'],
            'slack': ['WORK'],
            'twitter': ['TWTR'],
            'snapchat': ['SNAP'],
            'pinterest': ['PINS'],
            'dropbox': ['DBX']
        }

        # Fast exact and partial matching
        for name_key, tickers in common_mappings.items():
            if len(results) >= max_results:
                break

            # Check for matches
            if (name_key in query_lower or
                query_lower in name_key or
                any(word in name_key for word in query_lower.split() if len(word) > 3)):

                for ticker in tickers:
                    if len(results) >= max_results:
                        break

                    # Skip failed tickers
                    if ticker in self.failed_tickers:
                        continue

                    try:
                        financial_data = self.get_financial_data(ticker)
                        if 'error' not in financial_data:
                            results.append({
                                'symbol': ticker,
                                'name': financial_data.get('company_name', 'Unknown'),
                                'sector': financial_data.get('sector', 'Unknown'),
                                'exchange': financial_data.get('exchange', 'Unknown'),
                                'market_cap': financial_data.get('market_cap', 0),
                                'match_type': 'name_fuzzy'
                            })
                        else:
                            self.failed_tickers.add(ticker)

                    except Exception:
                        self.failed_tickers.add(ticker)
                        continue

        return results

