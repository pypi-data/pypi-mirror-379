# Werkbank - Model Context Protocol for Atomistic Simulations

Setup
-----
To connect the werkbank server to claude code at the current working directory, ensure `werkbank` is installed in the current working directory and then run:

```bash
bunx @anthropic-ai/claude-code mcp add werkbank -- uv run --project "$(pwd)" werkbank-mcp
bunx @anthropic-ai/claude-code
```

# Werkbank UI

- flask --app werkbank.ui run
- bun run dev
