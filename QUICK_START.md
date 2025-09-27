# 🚀 Quick Start Guide

Get up and running with the Global Market Research Agents in under 30 minutes.

## 📋 Prerequisites

- **AWS Account** with billing enabled
- **Amazon Bedrock** access (Claude 3 models)
- **Amazon SageMaker** access
- **Basic familiarity** with Jupyter notebooks

## ⚡ 5-Minute Setup

### Step 1: AWS Configuration (2 minutes)

#### Enable Bedrock Access
1. **AWS Console** → **Amazon Bedrock** → **Model access**
2. Click **Request model access**
3. Select **Anthropic Claude 3 Sonnet** ✅
4. Select **Anthropic Claude 3 Haiku** ✅ (optional, for faster responses)
5. Click **Submit** (approval usually takes < 5 minutes)

#### Create SageMaker Notebook
1. **AWS Console** → **SageMaker** → **Notebook instances**
2. Click **Create notebook instance**
3. **Name**: `market-research-agents`
4. **Instance type**: `ml.t3.medium` (or larger for better performance)
5. **IAM role**: Create new role with Bedrock and S3 access
6. Click **Create notebook instance**

### Step 2: Upload Project (1 minute)

1. **Wait for notebook status**: `InService` (takes 2-3 minutes)
2. Click **Open Jupyter** 
3. **Upload** the entire `sagemaker-notebooks/` folder
4. **Navigate** to the uploaded folder

### Step 3: Initialize System (2 minutes)

**Open and run** `01_bedrock_setup_and_testing.ipynb`:

```python
# Run this cell to initialize everything
import boto3
import json
from datetime import datetime

# Initialize Bedrock client
bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Test connection
print("🔄 Testing Bedrock connection...")
response = bedrock_client.list_foundation_models()
print("✅ Bedrock connection successful!")
print(f"📊 Available models: {len(response['modelSummaries'])}")
```

## 🧪 Test the System (5 minutes)

### Test 1: Basic Market Research
**Open** `02_market_research_agent.ipynb`:

```python
# Create and test market research agent
agent = MarketResearchAgent()

# Test with a major market
result = agent.analyze_market("Germany", "fintech")
print("✅ Market Research Agent working!")
print(f"📊 Analysis length: {len(result['analysis'])} characters")
```

### Test 2: Risk Assessment
**Open** `03_risk_assessment_agent.ipynb`:

```python
# Create and test risk assessment agent
risk_agent = RiskAssessmentAgent()

# Test risk assessment
result = risk_agent.comprehensive_risk_assessment("Japan", "technology")
print("✅ Risk Assessment Agent working!")
print(f"⚠️ Risk Score: {result['overall_risk_score']}/10")
```

### Test 3: Global Chatbot
**Open** `07_chatbot_interface.ipynb`:

```python
# Initialize chatbot
chatbot = MarketResearchChatbot()

# Add global countries (195+ countries)
add_global_countries()
print(f"🌍 Chatbot now supports {len(chatbot.countries)} countries")

# Test with a global query
response = chatbot.handle_query("What are the risks of entering the Rwanda fintech market?")
format_response(response)
```

## 🌍 Try Global Capabilities

### Test Different Regions
```python
# African markets
test_single_query("What are the fintech opportunities in Rwanda?")

# Asian emerging markets
test_single_query("Should I invest in Bangladesh healthcare?")

# European small countries
test_single_query("Compare technology in Estonia vs Latvia")

# Pacific islands
test_single_query("Tourism opportunities in Fiji")
```

### Run Complete Test Suite
```python
# Test everything at once
run_complete_test()

# Expected output:
# ✅ Basic functionality: 4/4 tests passed
# 🌍 Global countries added: 25 new countries
# 📊 Global detection: 5/5 tests passed (100%)
```

## 📊 Generate Your First Report

```python
# Open 06_agent_testing_guide.ipynb
# Generate PDF report with sample data
pdf_filename = generate_benchmark_pdf_report()
print(f"📄 Report generated: {pdf_filename}")

# Or create custom report
pdf_filename = generate_custom_pdf_report(
    countries=['Rwanda', 'Estonia', 'Bangladesh'], 
    industry='technology'
)
```

## 🎯 Example Use Cases

### Startup Expansion
```python
query = "Should I expand my fintech startup to Estonia or Latvia?"
response = chatbot.handle_query(query)
# Gets comparison analysis with risk scores and recommendations
```

### Investment Research
```python
query = "What are the risks of investing in Bangladeshi healthcare?"
response = chatbot.handle_query(query)
# Gets detailed risk assessment and market analysis
```

### Market Entry Strategy
```python
query = "Compare tourism opportunities in Fiji vs Samoa"
response = chatbot.handle_query(query)
# Gets comparative analysis with strategic recommendations
```

## 🔧 Customization Options

### Switch to Faster Model (for development)
```python
# Use Claude 3 Haiku for faster responses
agent = MarketResearchAgent(
    model_id="anthropic.claude-3-haiku-20240307-v1:0"
)
```

### Add Custom Industries
```python
# Extend industry recognition
chatbot.industries.extend([
    "renewable energy", "sustainable agriculture", "space technology"
])
```

### Test Custom Countries
```python
# Test any country not in the default list
test_single_query("Analyze the mining sector in Mongolia")
```

## 🚨 Troubleshooting

### Common Issues & Solutions

#### ❌ "Bedrock Access Denied"
```python
# Check model access status
import boto3
bedrock = boto3.client('bedrock', region_name='us-east-1')
try:
    models = bedrock.list_foundation_models()
    print("✅ Bedrock access working")
except Exception as e:
    print(f"❌ Error: {e}")
    print("💡 Solution: Request model access in Bedrock console")
```

#### ❌ "NameError: chatbot is not defined"
```python
# Make sure to run the chatbot initialization cell first
chatbot = MarketResearchChatbot()
print("✅ Chatbot initialized")
```

#### ❌ "Country not detected"
```python
# Add country manually
chatbot.countries.append("YourCountry")
print("✅ Country added to detection list")
```

#### ❌ Slow responses
```python
# Switch to faster model
agent = MarketResearchAgent(
    model_id="anthropic.claude-3-haiku-20240307-v1:0"
)
print("✅ Using faster Claude 3 Haiku model")
```

### Performance Tips

1. **Start with Haiku**: Use Claude 3 Haiku for development/testing
2. **Batch queries**: Process multiple countries together
3. **Cache results**: Avoid repeating identical queries
4. **Use appropriate instance**: Upgrade to `ml.m5.large` for heavy usage

## 📚 Next Steps

### Explore Advanced Features
1. **RAG Enhancement** (`05_rag_enhanced_market_research.ipynb`)
   - Add external documents for context
   - Enhanced analysis with custom data

2. **Multi-Agent Orchestration** (`04_multi_agent_orchestration.ipynb`)
   - Coordinated analysis across agents
   - Comprehensive decision frameworks

3. **Testing Framework** (`06_agent_testing_guide.ipynb`)
   - Performance benchmarking
   - Custom country testing
   - PDF report generation

### Production Deployment
- **SageMaker Endpoints**: For production API deployment
- **Lambda Functions**: For serverless deployment
- **API Gateway**: For REST API access

### Cost Optimization
- **Model Selection**: Use Haiku for simple queries, Sonnet for complex
- **Instance Sizing**: Right-size your SageMaker instances
- **Auto-stopping**: Configure notebooks to auto-stop when idle

## 🎉 Success Checklist

- [ ] ✅ Bedrock access approved and tested
- [ ] ✅ SageMaker notebook instance running
- [ ] ✅ All notebooks uploaded and accessible
- [ ] ✅ Basic agents tested and working
- [ ] ✅ Global chatbot initialized with 195+ countries
- [ ] ✅ Sample queries tested successfully
- [ ] ✅ PDF report generated
- [ ] ✅ Ready for production use

## 🌟 What You Can Do Now

**🌍 Analyze ANY country worldwide:**
- All 54 African countries
- All 48 Asian countries  
- All 44 European countries
- All 35 American countries
- All 14 Pacific nations

**💬 Ask natural language questions:**
- "What are the risks in Rwanda?"
- "Compare Estonia vs Latvia for startups"
- "Should I invest in Bangladesh healthcare?"

**📊 Generate professional reports:**
- Market analysis reports
- Risk assessment summaries
- Strategic recommendations
- Global benchmarking studies

---

**🚀 Congratulations! You now have a global market research platform that can analyze business opportunities in any country worldwide. Start exploring and discover new markets!**