# iagent - DevOps AI Agent

**iagent** is an intelligent AI agent framework specifically optimized for DevOps tasks. It combines the power of Large Language Models (LLMs) with practical DevOps tools to help you troubleshoot, debug, and solve infrastructure problems.

## Features

- **DevOps-Focused**: Specialized for Kubernetes, Docker, CI/CD, Infrastructure as Code, and more
- **Multi-LLM Support**: Works with OpenAI, LiteLLM, Ollama, HuggingFace, and AWS Bedrock
- **Safe by Default**: Code preview mode prevents accidental execution
- **AI-Powered Search**: Real-time DevOps troubleshooting with direct answers
- **Intelligent Log Analysis**: Advanced multi-log analysis (NGINX, syslog, security logs) with LLM-generated incident response recommendations
- **Multiple Agent Types**: Code agents, tool-calling agents, and triage agents
- **CI/CD Debugger**: AI-powered GitHub Actions and workflow debugging with intelligent fix suggestions

## Quick Start

### Installation

```bash
pip install ideaweaver-agent
```

### Environment Setup

**IMPORTANT: You MUST set your API key before using iagent (both CLI and API)**

```bash
# Set your OpenAI API key (REQUIRED for both CLI and API usage)
export OPENAI_API_KEY="your-api-key-here"

# Optional: Set default model
export IAGENT_MODEL_ID="gpt-4o-mini"
```

**Note**: Without setting the API key, both the CLI and API will fail to work.

## Usage

### Command Line Interface (CLI)

#### Basic Usage

```bash
# Safe mode (default) - shows code without executing
iagent "How do I troubleshoot Kubernetes pod restarts?"

# Execute mode - actually runs the code (use with caution)
iagent "Check Docker container health" --execute

# With web search for real-time DevOps solutions
iagent "Fix Terraform plan errors" --tools web_search

# NGINX log analysis with detailed recommendations
iagent "Analyze nginx logs from the last 600 minutes" --tools parse_logs --log-file nginx_access.log

# System performance monitoring
iagent "Monitor system performance" --tools system_monitor

# CI/CD debugging with AI-powered analysis
iagent "Check CI/CD status for my repository owner/repo" --tools get_cicd_status
iagent "Debug my GitHub Actions workflow failure for owner/repo" --tools debug_cicd_failure
iagent "Analyze CI/CD error patterns for owner/repo" --tools analyze_cicd_patterns
```

#### CLI Options

```bash
iagent "your task" [OPTIONS]

Options:
  --model-type {openai,litellm,huggingface,ollama,bedrock}
                        Model provider (default: openai)
  --model-id MODEL_ID   Model ID (default: gpt-4o-mini)
  --agent-type {code,tool,triage}
                        Agent type (default: code)
  --tools TOOLS         Tools to use (e.g., web_search, parse_logs, final_answer)
  --log-file LOG_FILE   Path to log file for parse_logs tool
  --max-steps MAX_STEPS Maximum number of steps (default: 10)
  --stream              Stream output in real-time
  --execute             Execute code locally (default: safe preview mode)
  --verbose             Enable verbose logging
```

### Python API Usage

#### Quick API Test

```python
#!/usr/bin/env python3
import os
from iagent.agents import ToolCallingAgent
from iagent.models import OpenAIModel
from iagent.tools import get_tool

# DevOps tool calling agent
model = OpenAIModel(model_id="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
tools = [get_tool('web_search'), get_tool('parse_logs'), get_tool('final_answer')]
agent = ToolCallingAgent(model=model, tools=tools)
result = agent.run("How do I troubleshoot Kubernetes pod restarts?")
print(result.answer)

# Direct web search
web_search = get_tool('web_search')
result = web_search.execute("Docker container health check failed")
print(result)

# Direct log analysis (supports nginx, syslog, secure logs)
parse_logs = get_tool('parse_logs')
result = parse_logs.execute("nginx_access.log", window_minutes=600, log_type="nginx")
print(result)
```

#### Basic API Example

```python
import os
from iagent.agents import CodeAgent, ToolCallingAgent
from iagent.models import OpenAIModel, LiteLLMModel, OllamaModel
from iagent.tools import get_tool
from iagent.executor import LocalPythonExecutor

# 1. Create a model
model = OpenAIModel(
    model_id="gpt-4o-mini",
    api_key="your-api-key"  # or set OPENAI_API_KEY env var
)

# 2. Create tools
web_search = get_tool('web_search')
parse_logs = get_tool('parse_logs')
final_answer = get_tool('final_answer')
tools = [web_search, parse_logs, final_answer]

# 3. Create executor (safe mode by default)
executor = LocalPythonExecutor(dry_run=True)  # Set dry_run=False to execute

# 4. Create agent
agent = CodeAgent(
    model=model,
    tools=tools,
    max_steps=10,
    preview_mode=True,  # Set to False to execute code
    executor=executor
)

# 5. Run the agent
result = agent.run("How do I troubleshoot Kubernetes pod restarts?")
print(f"Answer: {result.answer}")
print(f"Duration: {result.duration:.2f}s")
print(f"Steps: {len(result.steps)}")
```

## Available Tools

### Built-in Tools

- **`web_search`**: AI-powered search for DevOps solutions with direct answers
- **`parse_logs`**: Advanced multi-log analysis tool with intelligent security threat detection and LLM-generated recommendations
- **`system_monitor`**: Monitor system performance including CPU, memory, disk, and processes with AI-powered recommendations

### CI/CD Debugger Tools

- **`get_cicd_status`**: Get comprehensive status of recent CI/CD workflow runs
- **`debug_cicd_failure`**: AI-powered debugging of GitHub Actions workflow failures
- **`analyze_cicd_patterns`**: Analyze error patterns across multiple CI/CD runs

## Configuration

### Environment Variables

```bash
# Required for OpenAI
export OPENAI_API_KEY="your-openai-api-key"

# Required for CI/CD debugging
export GITHUB_TOKEN="your-github-token"

# Optional: Default model configuration
export IAGENT_MODEL_ID="gpt-4o-mini"

# For other providers
export LITELLM_API_KEY="your-litellm-key"
export HF_TOKEN="your-huggingface-token"
export AWS_DEFAULT_REGION="us-east-1"
export OLLAMA_BASE_URL="http://localhost:11434"
```

### Model Configuration

```python
# OpenAI models
"gpt-4o-mini"    # Fast and cost-effective
"gpt-4o"         # More capable
"gpt-4"          # Most capable

# LiteLLM models (100+ providers)
"claude-3-sonnet"
"claude-3-haiku"
"gemini-pro"
"llama2"

# Ollama models (local)
"llama2"
"codellama"
"mistral"
```

## Safety Features

### Safe Mode (Default)
- **Code Preview**: Shows code without executing
- **AST Validation**: Validates code syntax before execution
- **Import Restrictions**: Blocks dangerous imports
- **Sandboxed Execution**: Limited access to system resources

### Execution Mode
- **Use with Caution**: Only enable when you trust the code
- **Local Execution**: Runs code on your machine
- **Full System Access**: Can modify files and system state

```bash
# Safe mode (default)
iagent "Check system resources" 

# Execution mode (use carefully)
iagent "Check system resources" --execute
```

## Examples

### Kubernetes Troubleshooting

```bash
# Pod restart issues
iagent "My pod keeps restarting with CrashLoopBackOff status" --tools web_search

# Resource constraints
iagent "Check if my pods have enough CPU and memory allocated" --execute

# Service connectivity
iagent "Debug why my Kubernetes service is not accessible" --execute
```

### Docker Operations

```bash
# Container health
iagent "Check health of all running Docker containers" --execute

# Image analysis
iagent "Analyze my Docker image for security vulnerabilities" --execute

# Performance monitoring
iagent "Monitor Docker container resource usage" --execute
```

### CI/CD Debugging

```bash
# GitHub Actions debugging
iagent "Debug my failed GitHub Actions workflow" --tools web_search

# Pipeline optimization
iagent "Optimize my CI/CD pipeline for faster builds" --execute

# Deployment issues
iagent "Troubleshoot deployment failures in production" --execute
```

### Infrastructure as Code

```bash
# Terraform issues
iagent "Fix Terraform state conflicts" --execute

# Ansible troubleshooting
iagent "Debug Ansible playbook execution errors" --execute

# Cloud resource management
iagent "Audit my AWS resources for cost optimization" --execute
```

### Log Analysis & Monitoring

```bash
# NGINX log analysis with detailed recommendations
iagent "Analyze nginx logs from the last 600 minutes" --tools parse_logs --log-file nginx_access.log

# System log analysis
iagent "Analyze system logs for errors" --tools parse_logs --log-file /var/log/syslog

# Security log analysis
iagent "Analyze security logs for threats" --tools parse_logs --log-file /var/log/secure
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.

## Support

- **Issues**: Report bugs and request features on [GitHub Issues](https://github.com/plakhera/iagent/issues)
- **Documentation**: Check the [docs/](docs/) directory for detailed guides

## Acknowledgments

- Built on top of the powerful LLM ecosystem
- Inspired by the DevOps community's need for intelligent automation
- Thanks to all contributors and users who help improve this project

---

**Disclaimer**: This tool can execute code on your system. Always review code before execution and use safe mode when unsure. The authors are not responsible for any damage caused by code execution.