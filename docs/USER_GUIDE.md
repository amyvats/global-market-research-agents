# 📖 User Guide - Global Market Research Agents

Complete guide to using the Global Market Research Agents platform for worldwide market analysis.

## 🎯 Overview

The Global Market Research Agents platform provides AI-powered market research capabilities for **any country worldwide**. The system uses multiple specialized agents to provide comprehensive market analysis, risk assessment, and strategic recommendations.

## 🚀 Getting Started

### Prerequisites
- AWS account with Bedrock and SageMaker access
- Completed AWS setup (see `AWS_SETUP.md`)
- SageMaker notebook instance running

### First Steps
1. **Launch SageMaker**: Open your notebook instance
2. **Upload notebooks**: Upload the `sagemaker-notebooks/` folder
3. **Start with setup**: Open `01_bedrock_setup_and_testing.ipynb`
4. **Run cells sequentially**: Execute each cell to initialize the system

## 📚 Notebook Guide

### 01. Bedrock Setup and Testing
**Purpose**: Initialize Amazon Bedrock connection and test basic functionality

**Key Features**:
- Bedrock client configuration
- Model testing and validation
- Base agent class definition
- Connection troubleshooting

**Usage**:
```python
# Initialize Bedrock client
bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Test model access
test_response = invoke_bedrock_model("Hello, test message")
```

### 02. Market Research Agent
**Purpose**: Analyze market opportunities, size, competition, and trends

**Key Features**:
- Market size analysis
- Competitive landscape assessment
- Growth projections
- Regulatory environment analysis
- Cultural factors evaluation

**Usage**:
```python
# Create market research agent
market_agent = MarketResearchAgent()

# Analyze any country's market
result = market_agent.analyze_market("Rwanda", "fintech")
print(result['analysis'])
```

**Sample Output**:
```
Market Analysis for fintech in Rwanda:

1. Market Size & Growth:
   - Current market size: $45M USD
   - Annual growth rate: 23%
   - 5-year projection: $127M USD

2. Competitive Landscape:
   - Top competitors: Equity Bank, Bank of Kigali
   - Market share: Fragmented, no dominant player
   - Entry opportunities: Mobile payments, microfinance

3. Regulatory Environment:
   - Central Bank supportive of fintech innovation
   - Regulatory sandbox available
   - Clear licensing framework
```

### 03. Risk Assessment Agent
**Purpose**: Evaluate political, economic, legal, and operational risks

**Key Features**:
- Political stability analysis
- Economic risk factors
- Legal/regulatory compliance
- Operational challenges
- Overall risk scoring (1-10 scale)

**Usage**:
```python
# Create risk assessment agent
risk_agent = RiskAssessmentAgent()

# Assess risks for any country
result = risk_agent.comprehensive_risk_assessment("Estonia", "technology")
print(f"Overall Risk Score: {result['overall_risk_score']}/10")
```

**Risk Categories**:
- **Political Risk**: Government stability, policy changes
- **Economic Risk**: Currency, inflation, market conditions
- **Legal Risk**: Regulatory compliance, legal system
- **Operational Risk**: Infrastructure, talent, supply chain
- **Market Risk**: Competition, market dynamics
- **Technology Risk**: Digital infrastructure, cybersecurity

### 04. Multi-Agent Orchestration
**Purpose**: Coordinate multiple agents for comprehensive analysis

**Key Features**:
- Parallel agent execution
- Results synthesis
- Decision recommendations
- Priority scoring
- Confidence assessment

**Usage**:
```python
# Create orchestrator
orchestrator = MultiAgentOrchestrator()

# Get comprehensive analysis
result = orchestrator.comprehensive_market_entry_analysis("Bangladesh", "healthcare")

# Access different components
market_data = result['market_research']
risk_data = result['risk_assessment']
recommendation = result['recommendation']
```

**Decision Framework**:
- **PROCEED_WITH_CONFIDENCE** 🟢: Low risk (1-4), high opportunity
- **PROCEED_WITH_CAUTION** 🟡: Medium risk (4-6), good opportunity
- **PROCEED_WITH_MITIGATION** 🟠: High risk (6-8), requires planning
- **RECONSIDER_ENTRY** 🔴: Critical risk (8-10), not recommended

### 05. RAG Enhanced Market Research
**Purpose**: Enhance analysis with external data sources and vector storage

**Key Features**:
- Document ingestion and processing
- Vector database integration
- Enhanced context retrieval
- S3 storage for vectorstores
- Versioning and backup

**Usage**:
```python
# Create RAG-enhanced agent
rag_agent = RAGEnhancedMarketResearch()

# Add documents for context
rag_agent.add_documents([
    "Rwanda Economic Report 2024.pdf",
    "East Africa Fintech Trends.docx"
])

# Get enhanced analysis
result = rag_agent.enhanced_market_analysis("Rwanda", "fintech")
```

### 06. Agent Testing Guide
**Purpose**: Comprehensive testing framework for all agents

**Key Features**:
- Individual agent testing
- Performance benchmarking
- Global country testing
- Decision reasoning analysis
- PDF report generation

**Usage**:
```python
# Test global capabilities
quick_global_test(['Rwanda', 'Estonia', 'Bangladesh'])

# Generate performance report
results = benchmark_agents_global()
pdf_file = generate_benchmark_pdf_report(results)
```

### 07. Chatbot Interface
**Purpose**: Interactive natural language interface for market research

**Key Features**:
- Natural language processing
- Smart country/industry detection
- Intent classification
- Conversational memory
- Global country support (195+ countries)

**Usage**:
```python
# Initialize chatbot
chatbot = MarketResearchChatbot()

# Add global countries
add_global_countries()

# Ask natural language questions
response = chatbot.handle_query("What are the risks of entering the Rwanda fintech market?")
format_response(response)
```

## 🌍 Global Capabilities

### Supported Countries
The system supports **all 195+ countries worldwide**:

#### By Region:
- **🌍 Africa**: 54 countries (Rwanda, Kenya, Ghana, Nigeria, etc.)
- **🌏 Asia**: 48 countries (Bangladesh, Nepal, Mongolia, Myanmar, etc.)
- **🌍 Europe**: 44 countries (Estonia, Latvia, Slovenia, Malta, etc.)
- **🌎 Americas**: 35 countries (Ecuador, Uruguay, Costa Rica, etc.)
- **🌊 Oceania**: 14 countries (Fiji, Samoa, Tonga, Vanuatu, etc.)

#### By Development Level:
- **Developed**: G7 countries, EU, developed Asia-Pacific
- **Emerging**: BRICS, major emerging economies
- **Developing**: Frontier markets, least developed countries

### Example Queries by Region

#### African Markets
```python
# Fintech in East Africa
"What are the fintech opportunities in Rwanda?"
"Compare mobile money markets in Kenya vs Tanzania"
"Should I invest in digital banking in Ghana?"

# Agriculture in West Africa
"Agriculture technology opportunities in Nigeria"
"Food processing market in Senegal"
"Sustainable farming in Mali"
```

#### Asian Markets
```python
# Technology in South Asia
"Software development outsourcing in Bangladesh"
"IT services market in Nepal"
"Digital transformation in Sri Lanka"

# Manufacturing in Southeast Asia
"Textile manufacturing in Myanmar"
"Electronics assembly in Cambodia"
"Automotive parts in Laos"
```

#### European Markets
```python
# Startups in Baltic States
"Technology startup ecosystem in Estonia"
"Fintech regulations in Latvia"
"E-commerce growth in Lithuania"

# Tourism in Mediterranean
"Tourism recovery in Malta"
"Hospitality technology in Cyprus"
"Sustainable tourism in Slovenia"
```

#### Pacific Markets
```python
# Tourism and Sustainability
"Eco-tourism opportunities in Fiji"
"Renewable energy potential in Samoa"
"Sustainable fisheries in Tonga"
"Climate adaptation in Vanuatu"
```

## 🎯 Query Types and Intents

### Risk Assessment Queries
**Trigger words**: risk, risks, dangerous, safe, safety
```python
"What are the risks of entering the German fintech market?"
"Is it safe to invest in healthcare in Bangladesh?"
"How dangerous is the political situation in Myanmar?"
```

### Market Research Queries
**Trigger words**: market, size, opportunity, competition, competitors
```python
"What's the market size for AI in Singapore?"
"Who are the main competitors in Estonian fintech?"
"What opportunities exist in Rwandan agriculture?"
```

### Comparison Queries
**Trigger words**: compare, comparison, vs, versus, better
```python
"Compare technology markets in Japan vs South Korea"
"Estonia vs Latvia for startup expansion"
"Which is better: Thailand or Vietnam for manufacturing?"
```

### Recommendation Queries
**Trigger words**: should, recommend, advice, enter, expand
```python
"Should I expand my e-commerce business to France?"
"Do you recommend entering the Bangladeshi healthcare market?"
"What's your advice for investing in Mongolian mining?"
```

## 📊 Understanding Results

### Risk Scores (1-10 Scale)
- **1.0-3.0**: 🟢 **Low Risk** - Stable, established markets
- **3.1-6.0**: 🟡 **Medium Risk** - Growing markets with challenges
- **6.1-8.0**: 🟠 **High Risk** - Complex markets requiring expertise
- **8.1-10.0**: 🔴 **Critical Risk** - Unstable or restricted markets

### Priority Levels
- **High Priority** 🚀: Excellent opportunity, immediate focus
- **Medium Priority** ⚖️: Good opportunity, consider after high-priority
- **Low Priority** 📋: Limited opportunity or high complexity
- **Very Low Priority** ⏸️: Not recommended for current plans

### Confidence Levels
- **High Confidence** (80-100%): Strong data, clear recommendations
- **Medium Confidence** (60-79%): Good data, some uncertainty
- **Low Confidence** (40-59%): Limited data, high uncertainty

## 🧪 Testing Your Setup

### Basic Functionality Test
```python
# Test basic chatbot functionality
test_chatbot_simple()

# Expected output:
# ✅ SUCCESS: Query parsed successfully!
# 🌍 Countries: ['Germany']
# 🏭 Industries: ['fintech']
# 🎯 Intent: risk_assessment
```

### Global Capabilities Test
```python
# Add global countries
add_global_countries()

# Test global detection
test_global_queries()

# Expected output:
# ✅ SUCCESS: Global country 'Rwanda' detected!
# 📊 Success rate: 5/5 (100.0%)
```

### Custom Country Test
```python
# Test any countries you're interested in
test_single_query("What are the mining opportunities in Mongolia?")

# Expected output:
# 🌍 Countries detected: ['Mongolia']
# 🏭 Industries detected: ['mining']
# 🎯 Intent: market_research
```

## 📄 Generating Reports

### PDF Report Generation
```python
# Generate comprehensive PDF report
pdf_filename = generate_benchmark_pdf_report()

# Custom country analysis report
pdf_filename = generate_custom_pdf_report(
    countries=['Rwanda', 'Kenya', 'Ghana'], 
    industry='fintech'
)
```

### Report Contents
- **Executive Summary**: Overall assessment and key findings
- **Country Analysis**: Detailed breakdown by country
- **Risk Assessment**: Comprehensive risk evaluation
- **Market Opportunities**: Growth potential and opportunities
- **Strategic Recommendations**: Actionable next steps
- **Global Capabilities**: System performance metrics

## 🔧 Customization and Configuration

### Model Configuration
```python
# Adjust model parameters
class CustomMarketResearchAgent(MarketResearchAgent):
    def __init__(self):
        super().__init__(
            model_id="anthropic.claude-3-haiku-20240307-v1:0",  # Faster model
            temperature=0.5,  # More conservative responses
            max_tokens=1500   # Shorter responses
        )
```

### Adding Custom Industries
```python
# Extend industry list
chatbot.industries.extend([
    "renewable energy", "sustainable agriculture", "green technology",
    "space technology", "biotechnology", "nanotechnology"
])
```

### Custom Risk Factors
```python
# Add custom risk assessment criteria
custom_risk_factors = {
    "environmental_risk": "Climate change and environmental regulations",
    "social_risk": "Social stability and demographic trends",
    "governance_risk": "Corporate governance and transparency"
}
```

## 🚨 Troubleshooting

### Common Issues

#### 1. Model Access Denied
```python
# Check Bedrock model access
try:
    response = bedrock_client.list_foundation_models()
    print("✅ Bedrock access working")
except Exception as e:
    print(f"❌ Bedrock access error: {e}")
```

#### 2. Country Not Detected
```python
# Add country manually if not in list
if "YourCountry" not in chatbot.countries:
    chatbot.countries.append("YourCountry")
    print("✅ Country added to detection list")
```

#### 3. Slow Response Times
```python
# Switch to faster model for development
agent = MarketResearchAgent(
    model_id="anthropic.claude-3-haiku-20240307-v1:0"
)
```

#### 4. Memory Issues
```python
# Clear conversation history
chatbot.conversation_history = []
print("✅ Conversation history cleared")
```

### Performance Optimization

#### 1. Parallel Processing
```python
# Process multiple countries simultaneously
import concurrent.futures

def analyze_country(country):
    return market_agent.analyze_market(country, "technology")

countries = ["Rwanda", "Estonia", "Bangladesh"]
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(analyze_country, countries))
```

#### 2. Caching Results
```python
# Simple caching mechanism
import functools

@functools.lru_cache(maxsize=100)
def cached_market_analysis(country, industry):
    return market_agent.analyze_market(country, industry)
```

## 📈 Best Practices

### 1. Query Optimization
- **Be specific**: Include country and industry names
- **Use clear language**: Avoid ambiguous terms
- **One question per query**: Don't combine multiple questions

### 2. Result Interpretation
- **Consider confidence levels**: Higher confidence = more reliable
- **Cross-reference sources**: Validate with external data
- **Update regularly**: Market conditions change rapidly

### 3. Cost Management
- **Use appropriate models**: Haiku for simple queries, Sonnet for complex
- **Batch similar queries**: Process multiple countries together
- **Cache frequent queries**: Avoid redundant API calls

### 4. Security
- **No sensitive data**: Don't include confidential information in queries
- **Regular updates**: Keep dependencies and models updated
- **Access control**: Use proper IAM roles and permissions

## 🤝 Getting Help

### Documentation
- **AWS Setup**: See `AWS_SETUP.md` for infrastructure setup
- **Quick Start**: See `QUICK_START.md` for rapid deployment
- **API Reference**: Check notebook docstrings for detailed API info

### Support Channels
- **GitHub Issues**: Report bugs and request features
- **AWS Support**: For infrastructure and service issues
- **Community**: Join discussions and share experiences

### Contributing
- **Bug Reports**: Include error messages and reproduction steps
- **Feature Requests**: Describe use case and expected behavior
- **Code Contributions**: Follow coding standards and include tests

---

**🌍 Ready to analyze markets worldwide? Start with the Quick Start guide and explore global opportunities!**