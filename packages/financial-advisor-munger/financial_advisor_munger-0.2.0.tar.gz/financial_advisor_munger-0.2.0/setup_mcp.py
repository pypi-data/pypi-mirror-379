#!/usr/bin/env python3
"""
Setup script for Financial Advisor MCP Server
Helps configure Claude Code integration
"""

import json
import os
import sys
from pathlib import Path


def find_claude_config_dir():
    """Find the Claude Code configuration directory"""

    # Common Claude Code config locations
    possible_paths = [
        Path.home() / ".claude" / "config",
        Path.home() / ".config" / "claude",
        Path.home() / "AppData" / "Roaming" / "Claude",  # Windows
        Path.home() / "Library" / "Application Support" / "Claude",  # macOS
    ]

    for path in possible_paths:
        if path.exists():
            return path

    return None


def get_mcp_config():
    """Generate MCP server configuration"""

    current_dir = Path(__file__).parent.absolute()
    python_path = sys.executable

    return {
        "mcpServers": {
            "financial-advisor": {
                "command": python_path,
                "args": ["-m", "financial_advisor_mcp.server"],
                "env": {},
                "description": "Charlie Munger Investment Analysis"
            }
        }
    }


def update_claude_config():
    """Update Claude Code configuration with MCP server"""

    config_dir = find_claude_config_dir()

    if not config_dir:
        print("❌ Could not find Claude Code configuration directory")
        print("\nPlease manually add this configuration to your Claude Code MCP settings:")
        print(json.dumps(get_mcp_config(), indent=2))
        return False

    config_file = config_dir / "mcp_settings.json"

    # Load existing config or create new
    if config_file.exists():
        with open(config_file, 'r') as f:
            config = json.load(f)
    else:
        config = {"mcpServers": {}}

    # Add our server
    new_config = get_mcp_config()
    config["mcpServers"].update(new_config["mcpServers"])

    # Save updated config
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)

    print(f"✅ Updated Claude Code configuration: {config_file}")
    return True


def test_installation():
    """Test if the MCP server can be imported"""

    try:
        from financial_advisor_mcp.server import mcp
        print("✅ MCP server import successful")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        print("Please run: pip install -e .")
        return False


def main():
    """Main setup process"""

    print("🎯 Financial Advisor MCP Server Setup")
    print("=" * 45)

    # Check if we're in the right directory
    if not Path("src/financial_advisor_mcp").exists():
        print("❌ Please run this script from the financial-advisor-mcp directory")
        return

    # Test installation
    print("\n📦 Testing installation...")
    if not test_installation():
        print("\n🔧 Please install the package first:")
        print("   pip install -e .")
        return

    # Update Claude Code config
    print("\n⚙️  Configuring Claude Code...")
    success = update_claude_config()

    if success:
        print("\n🎉 Setup complete!")
        print("\nNext steps:")
        print("1. Restart Claude Code")
        print("2. Try: 'Can you analyze AAPL using Munger's framework?'")
    else:
        print("\n📝 Manual configuration required:")
        print("Add this to your Claude Code MCP settings:")
        print(json.dumps(get_mcp_config(), indent=2))

    print("\n📖 For more information, see README.md")


if __name__ == "__main__":
    main()