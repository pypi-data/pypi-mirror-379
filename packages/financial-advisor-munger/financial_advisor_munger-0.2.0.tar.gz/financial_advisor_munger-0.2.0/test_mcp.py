#!/usr/bin/env python3
"""
Test script for Financial Advisor MCP Server
Validates core functionality before Claude Code integration
"""

import sys
import asyncio
from pathlib import Path

# Add src to path for testing
sys.path.insert(0, str(Path(__file__).parent / "src"))

from financial_advisor_mcp.data_provider import FinancialDataProvider
from financial_advisor_mcp.munger_persona import CharleMungerPersona


def test_data_provider():
    """Test financial data provider"""

    print("🔍 Testing Financial Data Provider...")

    provider = FinancialDataProvider()

    # Test with AAPL
    data = provider.get_financial_data('AAPL')

    if 'error' in data:
        print(f"❌ Data provider failed: {data['error']}")
        return False

    print(f"✅ Retrieved data for {data.get('company_name', 'Unknown')}")
    print(f"   Completeness: {data.get('completeness_score', 0):.1f}%")
    print(f"   Market Cap: ${data.get('market_cap', 0):,}")

    # Test BRK.A fix
    print("\n🧪 Testing BRK.A symbol fix...")
    brk_data = provider.get_financial_data('BRK.A')

    if 'error' in brk_data:
        print(f"❌ BRK.A fix failed: {brk_data['error']}")
        return False

    print(f"✅ BRK.A fix working: {brk_data.get('company_name', 'Unknown')}")
    print(f"   Used symbol: {brk_data.get('actual_symbol_used', 'Unknown')}")

    return True


def test_munger_persona():
    """Test Munger persona analysis"""

    print("\n🎩 Testing Munger Persona...")

    provider = FinancialDataProvider()
    munger = CharleMungerPersona()

    # Test with AAPL
    data = provider.get_financial_data('AAPL')
    if 'error' in data:
        print(f"❌ Cannot test persona - data error: {data['error']}")
        return False

    analysis = munger.analyze_investment(data)

    print(f"✅ Analysis complete for {analysis.get('company_name', 'Unknown')}")
    print(f"   Recommendation: {analysis.get('recommendation', 'Unknown')}")
    print(f"   Munger Score: {analysis.get('munger_score', 0)}/100")
    print(f"   Voice sample: \"{analysis.get('munger_voice', '')[:100]}...\"")

    # Test kill switches with TSLA
    print("\n⚡ Testing kill switches with TSLA...")
    tsla_data = provider.get_financial_data('TSLA')

    if 'error' not in tsla_data:
        tsla_analysis = munger.analyze_investment(tsla_data)
        kill_switches = tsla_analysis.get('kill_switches', [])

        if kill_switches:
            print(f"✅ Kill switches working: {len(kill_switches)} triggered")
            print(f"   Primary reason: {kill_switches[0].get('reason', 'Unknown')}")
        else:
            print("⚠️  Expected kill switches for TSLA but none triggered")

    return True


def test_mcp_tools_simulation():
    """Simulate MCP tool calls"""

    print("\n🛠️  Testing MCP Tool Simulation...")

    # Import the tools (they're functions, not async)
    try:
        from financial_advisor_mcp.server import analyze_stock_munger, get_financial_data

        # Test analyze_stock_munger
        print("   Testing analyze_stock_munger('AAPL')...")
        result = analyze_stock_munger('AAPL')

        if result.get('success'):
            analysis = result['analysis']
            print(f"✅ MCP analysis successful")
            print(f"   Company: {analysis.get('company_name', 'Unknown')}")
            print(f"   Recommendation: {analysis.get('recommendation', 'Unknown')}")
        else:
            print(f"❌ MCP analysis failed: {result}")
            return False

        # Test get_financial_data
        print("   Testing get_financial_data('MSFT')...")
        data_result = get_financial_data('MSFT')

        if data_result.get('success'):
            summary = data_result['data_summary']
            print(f"✅ MCP data retrieval successful")
            print(f"   Company: {summary.get('company', 'Unknown')}")
            print(f"   Sector: {summary.get('sector', 'Unknown')}")
        else:
            print(f"❌ MCP data retrieval failed: {data_result}")
            return False

        return True

    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False


def main():
    """Run all tests"""

    print("🎯 Financial Advisor MCP Server Testing")
    print("=" * 45)

    tests_passed = 0
    total_tests = 3

    # Test data provider
    if test_data_provider():
        tests_passed += 1

    # Test Munger persona
    if test_munger_persona():
        tests_passed += 1

    # Test MCP tools simulation
    if test_mcp_tools_simulation():
        tests_passed += 1

    print(f"\n📊 Test Results: {tests_passed}/{total_tests} passed")

    if tests_passed == total_tests:
        print("🎉 All tests passed! MCP server is ready for Claude Code integration.")
        print("\nNext steps:")
        print("1. Install: pip install -e .")
        print("2. Configure: python setup_mcp.py")
        print("3. Test in Claude Code: 'Analyze AAPL using Munger framework'")
    else:
        print("❌ Some tests failed. Please check the errors above.")

    return tests_passed == total_tests


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)