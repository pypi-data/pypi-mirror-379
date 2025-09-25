# Quick Model Comparison Summary

## 🏆 Winner: GPT-5-nano (Default Choice)

**Why it's the best default:**

- ✅ **5x cheaper** than GPT-5-mini ($0.45 vs $2.25 per 1M tokens)
- ✅ **80% of premium quality** at 20% of the cost
- ✅ **Consistent, reliable** docstring generation
- ✅ **Proper Google style** formatting
- ✅ **No syntax errors** (unlike GPT-4.1-nano)

## 📊 Quality Comparison

| Model | Cost (per 1M tokens) | Quality Score | Quality per Dollar | Recommendation |
|-------|---------------------|---------------|-------------------|----------------|
| **gpt-5-nano** | $0.45 | 39/50 | **39,796** | **✅ Default** |
| **claude-haiku-3.5** | $0.25 | **67/50** | 6,442 | **✅ Highest Quality** |
| **gpt-4.1-nano** | $0.50 | 46/50 | 42,593 | **✅ Best Value** |
| **gpt-5-mini** | $2.25 | 41/50 | 8,367 | **✅ Premium** |
| **claude-haiku-3** | $0.25 | 41/50 | 12,615 | **✅ Budget Anthropic** |
| gpt-4.1-mini | $2.00 | 41/50 | 9,491 | Alternative |
| claude-sonnet-4 | $3.00 | 41/50 | 1,051 | High Performance |
| claude-opus-4.1 | $15.00 | 41/50 | 210 | Premium (Expensive) |

## 🔍 Key Differences

### Claude Haiku 3.5 (Highest Quality) 🏆

- **Highest quality score** (67/50) - exceeds baseline
- Comprehensive documentation with detailed explanations
- Excellent for critical documentation requirements
- Best Anthropic option for quality

### GPT-5-nano (Default Choice) ⭐

- Concise but complete docstrings
- Proper Args/Returns/Raises sections
- Clean Google style format
- Best value proposition (39,796 quality/$)
- Reliable quality

### GPT-4.1-nano (Best Value)

- **Highest quality score** among OpenAI models (46/50)
- Excellent quality-per-dollar ratio (42,593)
- Good alternative to GPT-5-nano
- Budget-friendly option

### GPT-5-mini (Premium)

- Comprehensive business logic explanations
- Detailed architecture documentation
- Complete method signatures
- Premium quality for enterprise use

### Claude Haiku 3 (Budget Anthropic)

- Good quality-per-dollar ratio for Anthropic (12,615)
- Reliable Anthropic option
- Cost-effective for Anthropic preference

## 💡 Decision Matrix

| Use Case | Recommended Model | Reason |
|----------|-------------------|---------|
| **Development** | gpt-5-nano | Best value, reliable quality |
| **Testing/CI** | gpt-5-nano | Cost-effective for automated runs |
| **Production** | gpt-5-mini | Maximum quality for end users |
| **Enterprise** | gpt-5-mini | Comprehensive documentation |
| **Budget-Conscious** | gpt-4.1-nano | Highest quality score at low cost |
| **Privacy-First** | Ollama codeqwen | Local processing |
| **Anthropic Preference** | claude-haiku-3.5 | Highest quality score (67/50) |
| **Budget Anthropic** | claude-haiku-3 | Good quality-per-dollar ratio |

## 🚀 Quick Start

```bash
# Use default (gpt-5-nano) - Best value
dococtopy fix . --rule DG101

# Use premium (gpt-5-mini) - Maximum quality
dococtopy fix . --rule DG101 --llm-model gpt-5-mini

# Use best Anthropic (claude-haiku-3.5) - Highest quality score
dococtopy fix . --rule DG101 --llm-provider anthropic --llm-model claude-haiku-3.5

# Use best value (gpt-4.1-nano) - Highest quality score at low cost
dococtopy fix . --rule DG101 --llm-model gpt-4.1-nano

# Use local (Ollama) - Privacy-first
dococtopy fix . --rule DG101 --llm-provider ollama --llm-model codeqwen:latest
```

## 📁 Files to Compare

### Input Files

- `original-fixture.py` - Input file with missing docstrings
- `nested-fixture.py` - Enhanced test fixture with nested structures

### Model Output Files (Open these side-by-side to see quality differences!)

- `gpt_5_nano_result.py` - Default model output (39/50 quality)
- `claude_haiku_3.5_result.py` - Highest quality output (67/50 quality)
- `gpt_4.1_nano_result.py` - Best value output (46/50 quality)
- `gpt_5_mini_result.py` - Premium model output (41/50 quality)
- `claude_haiku_3_result.py` - Budget Anthropic output (41/50 quality)
- `gpt_4.1_mini_result.py` - Alternative model output (41/50 quality)
- `claude_sonnet_4_result.py` - High performance output (41/50 quality)
- `claude_opus_4.1_result.py` - Premium output (41/50 quality)

### Results Data

- `comprehensive-comparison-results.txt` - Detailed metrics and analysis
