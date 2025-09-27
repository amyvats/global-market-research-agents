# 🖥️ Bedrock Console Walkthrough - Visual Guide

This is a detailed, step-by-step visual walkthrough for creating your market research agents in the Bedrock console.

## 🎯 Overview: What We're Building

**Before:** Programmatic agents in Jupyter notebooks
**After:** Managed Bedrock Agents accessible via console and API

```
┌─────────────────────────────────────────────────────────────┐
│                    BEDROCK AGENTS ARCHITECTURE              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐    ┌─────────────────┐                │
│  │ Market Research │    │ Risk Assessment │                │
│  │     Agent       │    │     Agent       │                │
│  │  (Claude 3      │    │  (Claude 3      │                │
│  │   Sonnet)       │    │   Haiku)        │                │
│  └─────────────────┘    └─────────────────┘                │
│           │                       │                         │
│           └───────────┬───────────┘                         │
│                       │                                     │
│              ┌─────────────────┐                           │
│              │ Market Entry    │                           │
│              │   Advisor       │                           │
│              │ (Orchestrator)  │                           │
│              │ (Claude 3       │                           │
│              │  Sonnet)        │                           │
│              └─────────────────┘                           │
│                       │                                     │
│              ┌─────────────────┐                           │
│              │ Knowledge Base  │                           │
│              │ (Market Reports)│                           │
│              │ (Titan Embed)   │                           │
│              └─────────────────┘                           │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 Phase 1: Initial Setup

### Step 1.1: Access Bedrock Console

1. **Open AWS Console** → Search "Bedrock"
2. **Select Region** → Choose `us-east-1` (N. Virginia) or `us-west-2` (Oregon)

```
🖼️ [Screenshot Placeholder: AWS Console with Bedrock service highlighted]
```

### Step 1.2: Enable Model Access

1. **Navigate:** Bedrock Console → **Model access** (left sidebar)
2. **Click:** "Manage model access" button

```
🖼️ [Screenshot Placeholder: Model access page with "Manage model access" button]
```

3. **Select Models:**
   - ✅ **Anthropic Claude 3 Sonnet**
   - ✅ **Anthropic Claude 3 Haiku** 
   - ✅ **Amazon Titan Embeddings G1 - Text**

```
🖼️ [Screenshot Placeholder: Model selection checkboxes with Claude and Titan models]
```

4. **Click:** "Request model access"
5. **Wait:** For approval (usually instant)

```
🖼️ [Screenshot Placeholder: Model access status showing "Access granted"]
```

---

## 🔍 Phase 2: Create Market Research Agent

### Step 2.1: Create New Agent

1. **Navigate:** Bedrock Console → **Agents** → **Create Agent**

```
🖼️ [Screenshot Placeholder: Agents page with "Create Agent" button highlighted]
```

2. **Fill Agent Details:**
   ```
   Agent name: MarketResearchAgent
   Agent description: Analyzes market opportunities, competition, and entry strategies for international markets
   ```

```
🖼️ [Screenshot Placeholder: Agent creation form with name and description fields filled]
```

### Step 2.2: Configure Foundation Model

3. **Select Model:**
   - **Model:** `Anthropic Claude 3 Sonnet`
   - **Version:** Latest available

```
🖼️ [Screenshot Placeholder: Model selection dropdown with Claude 3 Sonnet selected]
```

### Step 2.3: Add Agent Instructions

4. **Paste Instructions:**
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

   When analyzing a market, structure your response as:
   
   ## Market Overview
   - Market size in USD
   - Annual growth rate
   - Market maturity level
   
   ## Competitive Landscape
   - Top 5 competitors
   - Market share distribution
   - Competitive positioning
   
   ## Regulatory Environment
   - Key regulations affecting the industry
   - Compliance requirements
   - Regulatory complexity level
   
   ## Market Opportunities
   - Underserved segments
   - Emerging trends
   - Innovation gaps
   
   ## Entry Strategy Recommendations
   - Recommended approach
   - Key success factors
   - Timeline considerations
   ```

```
🖼️ [Screenshot Placeholder: Large text area with agent instructions filled in]
```

### Step 2.4: Save and Test

5. **Click:** "Save and exit"
6. **Test the Agent:**
   - **Query:** "Analyze the fintech market in Germany"
   - **Expected:** Detailed market analysis with structure

```
🖼️ [Screenshot Placeholder: Agent test interface with query and response]
```

---

## ⚠️ Phase 3: Create Risk Assessment Agent

### Step 3.1: Create Second Agent

1. **Navigate:** Agents → **Create Agent**
2. **Fill Details:**
   ```
   Agent name: RiskAssessmentAgent
   Agent description: Evaluates market entry risks across political, economic, legal, operational, market, and technology categories
   ```

### Step 3.2: Configure Model

3. **Select Model:**
   - **Model:** `Anthropic Claude 3 Haiku` (faster for risk calculations)

```
🖼️ [Screenshot Placeholder: Model selection with Claude 3 Haiku highlighted]
```

### Step 3.3: Add Risk Assessment Instructions

4. **Paste Instructions:**
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
   - Overall weighted risk score (average of all categories)
   - Risk level (Low: 1-3, Medium: 4-6, High: 7-8, Critical: 9-10)
   - Market entry recommendation (Proceed/Caution/Reconsider)

   Structure your response as:

   ## Risk Assessment Summary
   - Overall Risk Score: X.X/10
   - Risk Level: [Low/Medium/High/Critical]
   - Recommendation: [Proceed/Caution/Reconsider]

   ## Detailed Risk Analysis

   ### Political Risk (Score: X/10)
   - Risk factors: [list 2-3]
   - Mitigation: [list 1-2 strategies]

   [Continue for all 6 categories]

   ## Strategic Recommendations
   - Priority actions for risk mitigation
   - Timeline for market entry
   - Monitoring requirements

   Be analytical, data-driven, and provide specific actionable insights.
   ```

### Step 3.4: Test Risk Agent

5. **Test Query:** "Assess the risks of entering the Japanese e-commerce market"
6. **Verify:** Risk scores and structured analysis

```
🖼️ [Screenshot Placeholder: Risk assessment agent test with structured risk analysis response]
```

---

## 🎭 Phase 4: Create Market Entry Advisor (Orchestrator)

### Step 4.1: Create Master Agent

1. **Create New Agent:**
   ```
   Agent name: MarketEntryAdvisor
   Agent description: Provides comprehensive market entry recommendations combining market research and risk assessment insights
   ```

2. **Select Model:** `Anthropic Claude 3 Sonnet`

### Step 4.2: Add Orchestrator Instructions

3. **Paste Instructions:**
   ```
   You are a senior market entry consultant who provides comprehensive recommendations for international business expansion.

   Your role is to analyze market opportunities while considering associated risks to provide balanced, strategic recommendations.

   For each market entry query, provide a comprehensive analysis structured as:

   ## Executive Summary
   - Clear recommendation: GO / PROCEED WITH CAUTION / RECONSIDER
   - Priority level: High / Medium / Low
   - Confidence score: X% (based on data availability and market clarity)
   - Timeline: Recommended entry timeframe

   ## Market Opportunity Analysis
   - Market size and growth potential
   - Competitive landscape overview
   - Key market drivers and trends
   - Revenue potential and ROI projections

   ## Risk Assessment
   - Overall risk score and level
   - Top 3 critical risk factors
   - Risk mitigation strategies
   - Contingency planning recommendations

   ## Strategic Entry Recommendations
   - Recommended market entry strategy (direct, partnership, acquisition, etc.)
   - Phase-based implementation plan
   - Resource requirements (financial, human, operational)
   - Key success metrics and KPIs
   - Critical milestones and timeline

   ## Cultural and Regulatory Considerations
   - Cultural factors affecting business success
   - Regulatory compliance requirements
   - Local partnership recommendations
   - Localization needs

   ## Next Steps
   - Immediate actions (next 30 days)
   - Short-term goals (3-6 months)
   - Long-term objectives (1-2 years)

   Always be decisive, practical, and business-focused.
   Provide specific, actionable recommendations with clear reasoning.
   Consider both upside potential and downside risks in your recommendations.
   ```

### Step 4.3: Test Orchestrator

4. **Test Query:** "Should my fintech startup expand to the German market?"
5. **Verify:** Comprehensive recommendation with all sections

```
🖼️ [Screenshot Placeholder: Market Entry Advisor response showing structured recommendation]
```

---

## 📚 Phase 5: Optional Knowledge Base Setup

### Step 5.1: Prepare Market Research Documents

1. **Create S3 Bucket:**
   ```
   Bucket name: market-research-kb-[your-account-id]
   Region: Same as your Bedrock agents
   ```

2. **Upload Documents:**
   ```
   market-research-kb-123456789/
   ├── germany/
   │   ├── germany-market-overview-2024.pdf
   │   ├── german-fintech-landscape.pdf
   │   └── germany-regulatory-guide.pdf
   ├── japan/
   │   ├── japan-economic-outlook.pdf
   │   ├── japanese-market-entry-guide.pdf
   │   └── japan-cultural-business-guide.pdf
   └── global/
       ├── global-fintech-trends-2024.pdf
       ├── international-market-entry-strategies.pdf
       └── regulatory-compliance-frameworks.pdf
   ```

```
🖼️ [Screenshot Placeholder: S3 bucket with organized market research documents]
```

### Step 5.2: Create Knowledge Base

1. **Navigate:** Bedrock Console → **Knowledge bases** → **Create knowledge base**

```
🖼️ [Screenshot Placeholder: Knowledge base creation page]
```

2. **Configure Knowledge Base:**
   ```
   Knowledge base name: MarketResearchKnowledgeBase
   Description: Comprehensive market research reports and economic data for international markets
   IAM role: Create new service role
   ```

3. **Add Data Source:**
   ```
   Data source name: MarketResearchDocuments
   S3 URI: s3://market-research-kb-[your-account-id]/
   Chunking strategy: Default chunking
   ```

```
🖼️ [Screenshot Placeholder: Data source configuration with S3 URI]
```

4. **Configure Embeddings:**
   ```
   Embeddings model: Titan Embeddings G1 - Text
   Vector database: Amazon OpenSearch Serverless (recommended)
   ```

```
🖼️ [Screenshot Placeholder: Embeddings model selection]
```

5. **Create and Sync:**
   - Click "Create knowledge base"
   - Wait for sync to complete (5-15 minutes)

```
🖼️ [Screenshot Placeholder: Knowledge base sync progress]
```

### Step 5.3: Associate Knowledge Base with Agents

1. **Edit Market Research Agent:**
   - Go to agent details
   - Click "Edit"
   - Scroll to "Knowledge bases"
   - Click "Associate knowledge base"
   - Select "MarketResearchKnowledgeBase"

```
🖼️ [Screenshot Placeholder: Knowledge base association interface]
```

2. **Repeat for Market Entry Advisor**

3. **Test Enhanced Agents:**
   - Query: "What does the latest data say about German fintech regulations?"
   - Verify: Agent references uploaded documents

```
🖼️ [Screenshot Placeholder: Agent response citing knowledge base sources]
```

---

## 🧪 Phase 6: Comprehensive Testing

### Step 6.1: Individual Agent Tests

**Test Market Research Agent:**
```
Queries to test:
1. "Analyze the technology market opportunity in Japan"
2. "What are the key competitors in the German fintech space?"
3. "Describe the regulatory environment for e-commerce in the UK"
```

**Test Risk Assessment Agent:**
```
Queries to test:
1. "What are the risks of entering the French healthcare market?"
2. "Assess political and economic risks for expansion to Brazil"
3. "Evaluate operational risks for a tech company in Singapore"
```

**Test Market Entry Advisor:**
```
Queries to test:
1. "Should my SaaS company expand to the Netherlands?"
2. "Compare market entry opportunities: Germany vs France for fintech"
3. "Provide a comprehensive analysis for entering the Japanese AI market"
```

### Step 6.2: Conversation Flow Testing

**Multi-turn Conversation Test:**
```
Turn 1: "I'm considering international expansion for my fintech startup"
Turn 2: "What markets should I consider in Europe?"
Turn 3: "Tell me more about the German market specifically"
Turn 4: "What are the main risks I should be aware of?"
Turn 5: "What would be your final recommendation?"
```

```
🖼️ [Screenshot Placeholder: Multi-turn conversation in agent test interface]
```

### Step 6.3: Performance Benchmarking

**Create Test Suite:**
1. **Response Time:** Measure average response time per agent
2. **Accuracy:** Compare responses to known market data
3. **Consistency:** Test same query multiple times
4. **Error Handling:** Test with invalid inputs

```
🖼️ [Screenshot Placeholder: Agent performance metrics dashboard]
```

---

## 🚀 Phase 7: Production Deployment

### Step 7.1: Create Agent Aliases

1. **For Each Agent:**
   - Go to agent details
   - Click "Create alias"
   - Name: "Production"
   - Description: "Production version for live use"

```
🖼️ [Screenshot Placeholder: Agent alias creation interface]
```

### Step 7.2: Set Up Monitoring

1. **CloudWatch Integration:**
   - Navigate to CloudWatch
   - Create dashboard for Bedrock agents
   - Add metrics for:
     - Invocation count
     - Error rate
     - Response time
     - Token usage

```
🖼️ [Screenshot Placeholder: CloudWatch dashboard with Bedrock agent metrics]
```

### Step 7.3: Configure Access Control

1. **IAM Policies for Agent Access:**
   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "bedrock:InvokeAgent"
               ],
               "Resource": [
                   "arn:aws:bedrock:*:*:agent/MARKET_RESEARCH_AGENT_ID",
                   "arn:aws:bedrock:*:*:agent/RISK_ASSESSMENT_AGENT_ID",
                   "arn:aws:bedrock:*:*:agent/MARKET_ENTRY_ADVISOR_ID"
               ]
           }
       ]
   }
   ```

```
🖼️ [Screenshot Placeholder: IAM policy editor with Bedrock agent permissions]
```

---

## 🔗 Phase 8: Integration and API Usage

### Step 8.1: Get Agent IDs and Aliases

1. **Copy Agent Information:**
   ```
   Market Research Agent:
   - Agent ID: ABCDEF123456
   - Alias ID: TSTALIASID (for testing) / PROD123456 (for production)
   
   Risk Assessment Agent:
   - Agent ID: GHIJKL789012
   - Alias ID: TSTALIASID / PROD789012
   
   Market Entry Advisor:
   - Agent ID: MNOPQR345678
   - Alias ID: TSTALIASID / PROD345678
   ```

```
🖼️ [Screenshot Placeholder: Agent details page showing Agent ID and Alias ID]
```

### Step 8.2: API Integration Examples

**Python SDK Usage:**
```python
import boto3

# Initialize Bedrock Agent Runtime client
bedrock_agent = boto3.client('bedrock-agent-runtime', region_name='us-east-1')

# Call Market Research Agent
def get_market_analysis(country, industry):
    response = bedrock_agent.invoke_agent(
        agentId='ABCDEF123456',
        agentAliasId='PROD123456',
        sessionId='user-session-123',
        inputText=f"Analyze the {industry} market opportunity in {country}"
    )
    
    return response['completion']

# Call Risk Assessment Agent
def get_risk_assessment(country, industry):
    response = bedrock_agent.invoke_agent(
        agentId='GHIJKL789012',
        agentAliasId='PROD789012',
        sessionId='user-session-123',
        inputText=f"Assess the risks of entering the {industry} market in {country}"
    )
    
    return response['completion']

# Call Market Entry Advisor
def get_market_recommendation(country, industry):
    response = bedrock_agent.invoke_agent(
        agentId='MNOPQR345678',
        agentAliasId='PROD345678',
        sessionId='user-session-123',
        inputText=f"Should my company expand to the {industry} market in {country}?"
    )
    
    return response['completion']
```

### Step 8.3: Web Application Integration

**Simple Web Interface:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Market Research Assistant</title>
</head>
<body>
    <div id="chat-container">
        <div id="messages"></div>
        <input type="text" id="user-input" placeholder="Ask about market opportunities...">
        <button onclick="sendMessage()">Send</button>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('user-input');
            const message = input.value;
            
            // Call your backend API that integrates with Bedrock Agents
            const response = await fetch('/api/market-research', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({query: message})
            });
            
            const result = await response.json();
            displayMessage(result.response);
            input.value = '';
        }
        
        function displayMessage(message) {
            const messagesDiv = document.getElementById('messages');
            messagesDiv.innerHTML += `<div class="message">${message}</div>`;
        }
    </script>
</body>
</html>
```

---

## 📊 Phase 9: Monitoring and Optimization

### Step 9.1: Usage Analytics

**Key Metrics to Track:**
- **Invocation Volume:** Calls per agent per day
- **Response Time:** Average latency per agent
- **Error Rate:** Failed invocations percentage
- **Token Usage:** Cost tracking per agent
- **User Satisfaction:** Response quality ratings

```
🖼️ [Screenshot Placeholder: Comprehensive analytics dashboard]
```

### Step 9.2: Performance Optimization

**Optimization Strategies:**
1. **Prompt Engineering:** Refine instructions based on usage patterns
2. **Model Selection:** Switch between Claude models based on complexity needs
3. **Caching:** Implement response caching for common queries
4. **Load Balancing:** Distribute requests across multiple agent aliases

### Step 9.3: Continuous Improvement

**Feedback Loop:**
1. **Collect User Feedback:** Implement rating system
2. **Analyze Conversations:** Review chat logs for improvement opportunities
3. **Update Knowledge Base:** Add new market research documents regularly
4. **Refine Instructions:** Update agent prompts based on performance data

---

## ✅ Success Checklist

### Pre-Production Checklist
- [ ] All three agents created and tested
- [ ] Knowledge base configured and synced
- [ ] Agent aliases created for production
- [ ] IAM permissions configured
- [ ] Monitoring dashboard set up
- [ ] API integration tested
- [ ] Error handling implemented
- [ ] Cost monitoring enabled

### Go-Live Checklist
- [ ] Production aliases activated
- [ ] User access controls in place
- [ ] Backup and recovery procedures documented
- [ ] Support procedures established
- [ ] Performance baselines recorded
- [ ] User training completed

### Post-Launch Checklist
- [ ] Usage metrics reviewed weekly
- [ ] User feedback collected and analyzed
- [ ] Knowledge base updated monthly
- [ ] Agent performance optimized
- [ ] Cost optimization implemented
- [ ] Security audit completed

---

## 🎯 Comparison: Console vs Code

| Aspect | Bedrock Console Agents | Programmatic Agents |
|--------|----------------------|-------------------|
| **Setup Time** | 1-2 hours | 4-6 hours |
| **Technical Skill** | Low (point-and-click) | High (coding required) |
| **Customization** | Medium (console options) | High (full control) |
| **Maintenance** | Low (managed service) | High (code updates) |
| **Scaling** | Automatic | Manual |
| **Cost** | Pay-per-use | SageMaker + Bedrock |
| **Integration** | Built-in APIs | Custom APIs |
| **Memory** | Built-in sessions | Custom implementation |
| **Knowledge Base** | Managed RAG | Custom RAG |
| **Monitoring** | CloudWatch integration | Custom monitoring |
| **Deployment** | One-click aliases | CI/CD pipelines |

**Recommendation:** Use Bedrock Console Agents for faster deployment and easier management, especially for business users who need quick results without coding complexity.

---

## 🚀 Next Steps

1. **Start with Phase 1-2** to create your first agent
2. **Test thoroughly** before moving to the next agent
3. **Add knowledge base** once basic agents are working
4. **Integrate with applications** using the provided API examples
5. **Monitor and optimize** based on real usage patterns

Your Bedrock Console agents will provide the same market research capabilities as your programmatic agents, but with significantly less setup time and ongoing maintenance!