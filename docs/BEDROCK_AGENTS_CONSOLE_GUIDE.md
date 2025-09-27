# 🏗️ Bedrock Agents Console Setup Guide

This guide shows you how to recreate your market research agents using Amazon Bedrock Agents (managed service) through the AWS console.

## 🎯 What We'll Create

**3 Bedrock Agents** that mirror your programmatic agents:
1. **Market Research Agent** - Market analysis and opportunities
2. **Risk Assessment Agent** - Risk evaluation and scoring  
3. **Market Entry Advisor** - Combined recommendations (orchestrator equivalent)

## 📋 Prerequisites

### Required AWS Permissions
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:*",
                "iam:CreateRole",
                "iam:AttachRolePolicy",
                "iam:PassRole",
                "lambda:CreateFunction",
                "lambda:InvokeFunction",
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "*"
        }
    ]
}
```

### Setup Steps
1. ✅ **AWS Account** with Bedrock access
2. ✅ **Model Access** - Enable Claude 3 models in Bedrock console
3. ✅ **S3 Bucket** - For knowledge base documents (optional)
4. ✅ **IAM Roles** - Will be created during setup

---

## 🚀 Step-by-Step Console Setup

### Step 1: Enable Bedrock Model Access

1. **Go to Bedrock Console** → Model access
2. **Request Access** to these models:
   - ✅ `Claude 3 Sonnet` (for market research)
   - ✅ `Claude 3 Haiku` (for risk assessment)
   - ✅ `Titan Embeddings G1 - Text` (for knowledge base)

3. **Wait for approval** (usually instant for Claude models)

---

## 🔍 Agent 1: Market Research Agent

### Create the Agent

1. **Navigate to Bedrock Console** → Agents → Create Agent

2. **Agent Details:**
   ```
   Agent Name: MarketResearchAgent
   Description: Analyzes market opportunities, competition, and entry strategies
   ```

3. **Foundation Model:**
   ```
   Model: Claude 3 Sonnet
   ```

4. **Agent Instructions:**
   ```
   You are an expert market research analyst specializing in international market analysis.

   Your role is to provide comprehensive market research including:
   - Market size and growth analysis
   - Competitive landscape assessment  
   - Regulatory environment overview
   - Market entry opportunities and barriers
   - Cultural considerations for business
   - Growth projections and trends

   Always provide:
   1. Specific data points and metrics when available
   2. Key competitors and market share information
   3. Regulatory requirements and compliance needs
   4. Market entry strategies and recommendations
   5. Cultural factors that impact business success

   Format responses with clear sections and actionable insights.
   Be thorough but concise, focusing on business-relevant information.
   ```

### Configure Action Groups (Optional)

5. **Add Action Group** (for enhanced functionality):
   ```
   Action Group Name: MarketDataRetrieval
   Description: Retrieve real-time market data
   ```

6. **Create Lambda Function** for market data:
   ```python
   import json
   import boto3
   
   def lambda_handler(event, context):
       # Extract parameters
       country = event.get('country', 'Germany')
       industry = event.get('industry', 'technology')
       
       # Mock market data (replace with real API calls)
       market_data = {
           "market_size_usd": "180 billion",
           "growth_rate": "4.2%",
           "top_competitors": ["SAP", "Siemens", "Deutsche Telekom"],
           "regulatory_complexity": "High",
           "market_maturity": "Mature"
       }
       
       return {
           'statusCode': 200,
           'body': json.dumps({
               'country': country,
               'industry': industry,
               'data': market_data
           })
       }
   ```

7. **API Schema** for the action:
   ```json
   {
       "openapi": "3.0.0",
       "info": {
           "title": "Market Data API",
           "version": "1.0.0"
       },
       "paths": {
           "/market-data": {
               "post": {
                   "description": "Get market data for a country and industry",
                   "parameters": [
                       {
                           "name": "country",
                           "in": "query",
                           "required": true,
                           "schema": {"type": "string"}
                       },
                       {
                           "name": "industry", 
                           "in": "query",
                           "required": true,
                           "schema": {"type": "string"}
                       }
                   ],
                   "responses": {
                       "200": {
                           "description": "Market data retrieved successfully"
                       }
                   }
               }
           }
       }
   }
   ```

---

## ⚠️ Agent 2: Risk Assessment Agent

### Create the Agent

1. **Create New Agent:**
   ```
   Agent Name: RiskAssessmentAgent
   Description: Evaluates market entry risks across multiple categories
   ```

2. **Foundation Model:**
   ```
   Model: Claude 3 Haiku (faster for risk calculations)
   ```

3. **Agent Instructions:**
   ```
   You are a risk assessment specialist focused on international market entry risks.

   Analyze these risk categories with scores (1-10 scale, 10 = highest risk):

   1. POLITICAL RISK - Government stability, policy changes, political tensions
   2. ECONOMIC RISK - Currency volatility, inflation, market conditions  
   3. LEGAL/REGULATORY RISK - Compliance requirements, legal system reliability
   4. OPERATIONAL RISK - Infrastructure, talent availability, supply chain
   5. MARKET RISK - Competition intensity, market dynamics, saturation
   6. TECHNOLOGY RISK - Digital infrastructure, cybersecurity, tech adoption

   For each category provide:
   - Risk score (1-10)
   - 2-3 specific risk factors
   - 1-2 mitigation strategies

   Always conclude with:
   - Overall weighted risk score
   - Risk level (Low/Medium/High/Critical)
   - Market entry recommendation (Go/Caution/Stop)

   Be analytical, data-driven, and provide specific actionable insights.
   ```

### Add Risk Calculation Action

4. **Create Lambda for Risk Scoring:**
   ```python
   import json
   import random

   def lambda_handler(event, context):
       country = event.get('country', 'Germany')
       industry = event.get('industry', 'technology')
       
       # Risk scoring logic (replace with real data sources)
       risk_factors = {
           'political': random.uniform(2, 8),
           'economic': random.uniform(2, 7), 
           'legal': random.uniform(3, 9),
           'operational': random.uniform(2, 6),
           'market': random.uniform(3, 8),
           'technology': random.uniform(2, 5)
       }
       
       overall_score = sum(risk_factors.values()) / len(risk_factors)
       
       if overall_score <= 3:
           risk_level = "Low"
       elif overall_score <= 6:
           risk_level = "Medium"
       elif overall_score <= 8:
           risk_level = "High"
       else:
           risk_level = "Critical"
       
       return {
           'statusCode': 200,
           'body': json.dumps({
               'country': country,
               'industry': industry,
               'risk_scores': risk_factors,
               'overall_score': overall_score,
               'risk_level': risk_level
           })
       }
   ```

---

## 🎭 Agent 3: Market Entry Advisor (Orchestrator)

### Create the Master Agent

1. **Create New Agent:**
   ```
   Agent Name: MarketEntryAdvisor
   Description: Provides comprehensive market entry recommendations combining market research and risk assessment
   ```

2. **Foundation Model:**
   ```
   Model: Claude 3 Sonnet
   ```

3. **Agent Instructions:**
   ```
   You are a senior market entry consultant who provides comprehensive recommendations for international business expansion.

   Your analysis combines:
   1. Market research insights (opportunities, competition, market size)
   2. Risk assessment data (political, economic, operational risks)
   3. Strategic recommendations (entry strategy, timeline, priorities)

   For each market entry query, provide:

   EXECUTIVE SUMMARY:
   - Clear Go/No-Go recommendation
   - Priority level (High/Medium/Low)
   - Confidence score (1-100%)

   MARKET OPPORTUNITY:
   - Market size and growth potential
   - Competitive landscape
   - Key success factors

   RISK ANALYSIS:
   - Overall risk score and level
   - Top 3 risk factors
   - Mitigation strategies

   STRATEGIC RECOMMENDATIONS:
   - Recommended entry strategy
   - Timeline and milestones
   - Resource requirements
   - Success metrics

   Always be decisive, practical, and business-focused.
   Provide specific, actionable recommendations with clear reasoning.
   ```

### Configure Agent Collaboration

4. **Add Action Groups** to call other agents:

   **Action Group 1: Market Research**
   ```python
   import json
   import boto3

   def lambda_handler(event, context):
       bedrock_agent = boto3.client('bedrock-agent-runtime')
       
       # Call Market Research Agent
       response = bedrock_agent.invoke_agent(
           agentId='MARKET_RESEARCH_AGENT_ID',
           agentAliasId='TSTALIASID',
           sessionId=event.get('sessionId', 'default'),
           inputText=f"Analyze the {event.get('industry')} market in {event.get('country')}"
       )
       
       return {
           'statusCode': 200,
           'body': json.dumps({
               'market_analysis': response['completion']
           })
       }
   ```

   **Action Group 2: Risk Assessment**
   ```python
   import json
   import boto3

   def lambda_handler(event, context):
       bedrock_agent = boto3.client('bedrock-agent-runtime')
       
       # Call Risk Assessment Agent
       response = bedrock_agent.invoke_agent(
           agentId='RISK_ASSESSMENT_AGENT_ID',
           agentAliasId='TSTALIASID', 
           sessionId=event.get('sessionId', 'default'),
           inputText=f"Assess risks for {event.get('industry')} market entry in {event.get('country')}"
       )
       
       return {
           'statusCode': 200,
           'body': json.dumps({
               'risk_analysis': response['completion']
           })
       }
   ```

---

## 📚 Optional: Knowledge Base Setup

### Create Knowledge Base for Market Data

1. **Prepare Documents** (upload to S3):
   ```
   s3://your-bucket/market-data/
   ├── germany-market-report.pdf
   ├── japan-economic-overview.pdf
   ├── uk-regulatory-guide.pdf
   └── global-industry-trends.pdf
   ```

2. **Create Knowledge Base:**
   ```
   Knowledge Base Name: MarketResearchKB
   Description: Market research reports and economic data
   Data Source: S3 bucket with your documents
   Embedding Model: Titan Embeddings G1 - Text
   ```

3. **Associate with Agents:**
   - Link to Market Research Agent
   - Link to Market Entry Advisor

---

## 🧪 Testing Your Bedrock Agents

### Test Individual Agents

1. **Market Research Agent Test:**
   ```
   Query: "Analyze the fintech market opportunity in Germany"
   Expected: Detailed market analysis with size, competitors, regulations
   ```

2. **Risk Assessment Agent Test:**
   ```
   Query: "What are the risks of entering the Japanese e-commerce market?"
   Expected: Risk scores by category with mitigation strategies
   ```

3. **Market Entry Advisor Test:**
   ```
   Query: "Should my company expand to the UK technology market?"
   Expected: Comprehensive recommendation with market + risk analysis
   ```

### Test Conversations

**Example Chat Flow:**
```
User: "I'm considering expanding my fintech startup to Germany. What do you recommend?"

Agent: [Calls market research and risk assessment, then provides comprehensive recommendation]

User: "What about Japan instead?"

Agent: [Remembers context, compares Germany vs Japan, provides updated recommendation]
```

---

## 🔄 Console vs Code Comparison

| Feature | Programmatic Agents | Bedrock Console Agents |
|---------|-------------------|----------------------|
| **Setup Time** | 2-3 hours coding | 30-60 minutes clicking |
| **Customization** | Full control | Limited to console options |
| **Maintenance** | Code updates needed | Managed by AWS |
| **Scaling** | Manual infrastructure | Auto-scaling |
| **Cost** | SageMaker + Bedrock | Bedrock only |
| **Integration** | Custom APIs | Built-in APIs |
| **Memory** | Custom implementation | Built-in session memory |
| **Knowledge Base** | Custom RAG | Managed knowledge base |

---

## 🚀 Deployment Checklist

### Pre-Deployment
- [ ] Model access approved
- [ ] IAM roles configured  
- [ ] S3 bucket created (if using knowledge base)
- [ ] Lambda functions tested

### Agent Creation
- [ ] Market Research Agent created and tested
- [ ] Risk Assessment Agent created and tested  
- [ ] Market Entry Advisor created and tested
- [ ] Action groups configured
- [ ] Knowledge base linked (optional)

### Testing
- [ ] Individual agent tests passed
- [ ] Multi-agent workflows tested
- [ ] Error handling verified
- [ ] Performance benchmarked

### Production
- [ ] Agents published to production aliases
- [ ] Monitoring configured
- [ ] Access controls set
- [ ] Documentation updated

---

## 💡 Pro Tips

### Best Practices
1. **Start Simple** - Create basic agents first, add complexity later
2. **Test Thoroughly** - Use the test console extensively before production
3. **Monitor Usage** - Set up CloudWatch metrics for agent performance
4. **Version Control** - Use aliases for different versions (dev/staging/prod)
5. **Security** - Implement proper IAM policies and resource-based policies

### Common Issues
- **Model Access** - Ensure all required models are enabled
- **IAM Permissions** - Agent execution roles need proper permissions
- **Lambda Timeouts** - Set appropriate timeout values for action groups
- **Knowledge Base Sync** - Allow time for document indexing

### Cost Optimization
- Use **Claude 3 Haiku** for simple tasks (cheaper)
- Use **Claude 3 Sonnet** for complex analysis
- Implement **session management** to reduce redundant calls
- Monitor **token usage** and optimize prompts

---

## 🎯 Next Steps

1. **Create your first agent** using this guide
2. **Test with sample queries** to verify functionality  
3. **Add knowledge base** for enhanced accuracy
4. **Integrate with applications** using the Bedrock Agent APIs
5. **Monitor and optimize** based on usage patterns

Your Bedrock Agents will provide the same market research capabilities as your programmatic agents, but with managed infrastructure and built-in features like session memory and knowledge bases!