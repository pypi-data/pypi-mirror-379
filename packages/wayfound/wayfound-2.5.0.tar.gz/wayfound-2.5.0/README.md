# Wayfound Python SDK

[![PyPI version](https://badge.fury.io/py/wayfound.svg)](https://badge.fury.io/py/wayfound)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

The official Python SDK for [Wayfound AI](https://wayfound.ai) - the observability and compliance platform designed specifically for conversational AI agents and agentic workflows.

## 🚀 Features

- **Simple Session Management** - Track complete conversations between users and AI assistants and agentic workflows
- **Compliance Monitoring** - Automatically detect guideline violations in AI responses
- **Async Support** - Handle sessions synchronously or asynchronously
- **Flexible Message Format** - Support for various message types and metadata
- **Easy Integration** - Drop-in compatibility with existing Python applications

## 📦 Installation

Install the Wayfound SDK using pip:

```bash
pip install wayfound
```

## 🔧 Quick Start

### 1. Get Your API Credentials

First, you'll need to obtain your API credentials from the [Wayfound dashboard](https://app.wayfound.ai):

- `WAYFOUND_API_KEY` - Your authentication token
- `WAYFOUND_AGENT_ID` - The ID of the agent you're tracking

### 2. Basic Usage

```python
from wayfound import Session

# Initialize a session
session = Session(
    wayfound_api_key="your-api-key",
    agent_id="your-agent-id"
)

# Format your conversation messages
messages = [
    {
        "timestamp": "2025-01-15T10:00:00Z",
        "event_type": "assistant_message",
        "attributes": {
            "content": "Hello! How can I help you today?"
        }
    },
    {
        "timestamp": "2025-01-15T10:00:05Z",
        "event_type": "user_message",
        "attributes": {
            "content": "What's the weather like?"
        }
    },
    {
        "timestamp": "2025-01-15T10:00:10Z",
        "event_type": "assistant_message",
        "attributes": {
            "content": "I'd be happy to help with weather information. Could you please tell me your location?"
        }
    }
]

# Submit the session for analysis
result = session.complete_session(messages=messages, is_async=False)

# Check for compliance violations
if 'compliance' in result:
    violations = [item for item in result['compliance'] if not item['result']['compliant']]
    if violations:
        print(f"Found {len(violations)} guideline violations")
        for violation in violations:
            print(f"- {violation['guideline']}: {violation['result']['reason']}")
    else:
        print("✅ No compliance violations detected!")
```

### 3. Environment Variables

For convenience, you can set environment variables instead of passing credentials directly:

```bash
export WAYFOUND_API_KEY="your-api-key"
export WAYFOUND_AGENT_ID="your-agent-id"
```

Then initialize without parameters:

```python
from wayfound import Session

session = Session()  # Automatically uses environment variables
```

## 📚 API Reference

### Session Class

#### Constructor Parameters

| Parameter              | Type  | Description                         | Required |
| ---------------------- | ----- | ----------------------------------- | -------- |
| `wayfound_api_key`     | `str` | Your Wayfound API key               | Yes\*    |
| `agent_id`             | `str` | The agent ID to track               | Yes\*    |
| `session_id`           | `str` | Existing session ID (for appending) | No       |
| `application_id`       | `str` | Application identifier              | No       |
| `visitor_id`           | `str` | Unique visitor identifier           | No       |
| `visitor_display_name` | `str` | Human-readable visitor name         | No       |
| `account_id`           | `str` | Account identifier                  | No       |
| `account_display_name` | `str` | Human-readable account name         | No       |

\*Required unless set as environment variables

#### Methods

##### `complete_session(messages=None, is_async=True)`

Submits a complete conversation session for analysis.

**Parameters:**

- `messages` (list): List of formatted message objects
- `is_async` (bool): Whether to process asynchronously (default: True)

**Returns:** Dictionary with session results and compliance data

##### `append_to_session(messages, is_async=True)`

Adds additional messages to an existing session.

**Parameters:**

- `messages` (list): List of formatted message objects to append
- `is_async` (bool): Whether to process asynchronously (default: True)

**Returns:** Dictionary with updated session results

### Message Format

Each message should follow this structure:

```python
{
    "timestamp": "2025-01-15T10:00:00Z",  # ISO 8601 format
    "event_type": "assistant_message",     # or "user_message"
    "label": "greeting",                   # optional: message classification
    "description": "Initial greeting",     # optional: human-readable description
    "attributes": {
        "content": "Your message content here",
        # Additional custom attributes as needed
    }
}
```

## 🛠️ Advanced Usage

### Working with Existing Sessions

```python
# Start a new session
session = Session(wayfound_api_key="key", agent_id="agent")
result = session.complete_session(initial_messages)

# Later, append more messages to the same session
additional_messages = [
    {
        "timestamp": "2025-01-15T10:05:00Z",
        "event_type": "user_message",
        "attributes": {"content": "Follow-up question"}
    }
]

session.append_to_session(additional_messages)
```

### Custom Visitor and Account Tracking

```python
session = Session(
    wayfound_api_key="your-key",
    agent_id="your-agent",
    visitor_id="visitor-123",
    visitor_display_name="John Doe",
    account_id="acct-456",
    account_display_name="Acme Corp"
)
```

## 🔍 Examples

Check out the [`examples/`](examples/) directory for more detailed examples:

- [`simple.py`](examples/simple.py) - Basic session tracking with compliance checking

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: [Wayfound Docs](https://docs.wayfound.ai)

## 🏷️ Version

Current version: **2.3.0**
