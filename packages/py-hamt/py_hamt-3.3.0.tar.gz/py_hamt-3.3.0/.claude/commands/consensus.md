---
description: Execute multi-model consensus planning workflow using 3 specialized models via MCP
allowed-tools: Bash(mkdir:*), Bash(echo:*), Bash(date:*), Bash(cd:*), Bash(pwd:*), Bash(realpath:*)
argument-hint: "problem description"
---

**INITIALIZATION:**
Generate session and setup:
```bash
# Simple timestamp-based session ID
SESSION_ID=$(date +%Y-%m-%d_%H-%M-%S)_consensus
BASE_DIR="docs/consensus"
SESSION_DIR="$BASE_DIR/$SESSION_ID"

# Create session directory
mkdir -p "$SESSION_DIR"

# Update index with new session
echo "- [$SESSION_ID](./$SESSION_ID/) - $ARGUMENTS - $(date)" >> "$BASE_DIR/index.md"

# Get absolute path for consistency
ABSOLUTE_SESSION_DIR=$(realpath "$SESSION_DIR")

echo "Created session: $SESSION_ID"
echo "Session directory: $ABSOLUTE_SESSION_DIR"

**PHASE 1 - PARALLEL MODEL CONSULTATION:**
Launch 3 simultaneous planning tasks using absolute session path directory:

1. **GPT Plan**: 
   Use gpt-planner subagent with context:
   - Problem to analyze: "$ARGUMENTS"
   - Working directory: $ABSOLUTE_SESSION_DIR
   - Required output: gpt-plan.md
   - Session ID: $SESSION_ID

2. **Gemini Plan**: 
   Use gemini-planner subagent with context:
   - Problem to analyze: "$ARGUMENTS"  
   - Working directory: $ABSOLUTE_SESSION_DIR
   - Required output: gemini-plan.md
   - Session ID: $SESSION_ID

3. **Claude Plan**: 
   Use claude-planner subagent with context:
   - Problem to analyze: "$ARGUMENTS"
   - Working directory: $ABSOLUTE_SESSION_DIR
   - Required output: claude-plan.md
   - Session ID: $SESSION_ID

**PHASE 2 - INTELLIGENT COMPILATION:**
After all 3 models complete, use consensus-compiler subagent with context:

- Working directory: $ABSOLUTE_SESSION_DIR
- Session ID: $SESSION_ID
- Problem: "$ARGUMENTS"
- Input files: gpt-plan.md, gemini-plan.md, claude-plan.md
- Output file: compiled-solution.md
- Note: All files are in the working directory provided

Problem to analyze: $ARGUMENTS