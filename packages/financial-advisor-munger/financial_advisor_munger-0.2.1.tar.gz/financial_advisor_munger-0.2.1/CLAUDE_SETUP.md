# Charlie Munger MCP for Claude Users 🎯

## Super Simple Setup (Like `npx` for Python)

### Option 1: Direct Run with `pipx` (Recommended)

```bash
# Install pipx once (if you don't have it)
pip install --user pipx

# Run MCP server directly (no local installation needed!)
pipx run financial-advisor-munger munger-mcp
```

This works exactly like `npx` - runs the MCP server without installing anything locally!

### Option 2: Install Once, Use Everywhere

```bash
pipx install financial-advisor-munger
munger-mcp  # Available globally
```

### Option 3: From GitHub (Development Version)

```bash
pipx run --spec git+https://github.com/arnaldo-delisio/financial-advisor.git#subdirectory=financial-advisor-mcp financial-advisor-munger munger-mcp
```

## Claude Code MCP Configuration

Once the server is running, add this to your Claude Code MCP settings:

```json
{
  "mcpServers": {
    "munger": {
      "command": "pipx",
      "args": ["run", "financial-advisor-munger", "munger-mcp"],
      "description": "Charlie Munger Investment Analysis"
    }
  }
}
```

**OR** if you installed it globally:

```json
{
  "mcpServers": {
    "munger": {
      "command": "munger-mcp",
      "args": [],
      "description": "Charlie Munger Investment Analysis"
    }
  }
}
```

## Usage in Claude Code

Once configured, just ask Claude:

```
Can you analyze Apple stock using Munger's framework?
```

```
Search for companies named "Pandora" and analyze the best match
```

```
Compare AAPL, MSFT, and GOOGL using Charlie Munger's criteria
```

## Available MCP Tools

- `analyze_stock_munger(symbol)` - Full Munger analysis
- `ask_munger_followup(symbol, question_type)` - Follow-up questions
- `compare_stocks_munger(symbols)` - Multi-stock comparison
- `get_financial_data(symbol)` - Raw financial data
- `clarify_company_identity(query)` - Smart company search

## International Stocks Supported

- US: `AAPL`, `MSFT`, `BRK.A`
- Europe: `PNDORA.CO` (Copenhagen), `NESN.SW` (Swiss)
- Asia: `7203.T` (Tokyo), `0700.HK` (Hong Kong)

## Troubleshooting

If `pipx` isn't available:
```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

Then restart your terminal and try again.

---

**That's it!** No repo cloning, no virtual environments, no local setup. Just like using `npx` for Node packages! 🚀