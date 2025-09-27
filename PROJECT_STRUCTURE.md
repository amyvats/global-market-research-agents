# 📁 Project Structure

## 🗂️ Directory Overview

```
global-market-research-agents/
├── 📚 sagemaker-notebooks/           # Main Jupyter notebooks
│   ├── 01_bedrock_setup_and_testing.ipynb
│   ├── 02_market_research_agent.ipynb
│   ├── 03_risk_assessment_agent.ipynb
│   ├── 04_multi_agent_orchestration.ipynb
│   ├── 05_rag_enhanced_market_research.ipynb
│   ├── 06_agent_testing_guide.ipynb
│   └── 07_chatbot_interface.ipynb
├── 📖 docs/                          # Documentation
│   ├── AWS_SETUP.md                 # AWS infrastructure setup
│   ├── USER_GUIDE.md                # Comprehensive user guide
│   ├── PROJECT_OVERVIEW.md          # Project overview and architecture
│   ├── AWS_DEPLOYMENT_GUIDE.md      # Deployment strategies
│   ├── BEDROCK_AGENTS_CONSOLE_GUIDE.md
│   └── BEDROCK_CONSOLE_WALKTHROUGH.md
├── 🔧 scripts/                       # Setup and utility scripts
│   ├── setup_sagemaker.py           # SageMaker configuration
│   └── setup_rag_infrastructure.py  # RAG system setup
├── 🤖 agents/                        # Agent implementations
│   ├── risk_assessment_agent.py     # Standalone risk agent
│   └── tests/                       # Agent unit tests
├── 🔄 workflows/                     # Workflow definitions
├── 📄 README.md                      # Main project documentation
├── 🚀 QUICK_START.md                 # Quick start guide
├── 📋 requirements.txt               # Python dependencies
├── 🔒 .gitignore                     # Git ignore rules
└── 📊 PROJECT_STRUCTURE.md           # This file
```

## 📚 Notebook Descriptions

### Core Notebooks (Run in Order)

#### 01. Bedrock Setup and Testing
- **Purpose**: Initialize Amazon Bedrock connection
- **Key Features**: Client configuration, model testing, base classes
- **Prerequisites**: AWS credentials, Bedrock access
- **Runtime**: 2-3 minutes

#### 02. Market Research Agent
- **Purpose**: Market opportunity analysis
- **Key Features**: Market sizing, competition analysis, growth projections
- **Dependencies**: Notebook 01
- **Runtime**: 5-10 minutes per analysis

#### 03. Risk Assessment Agent
- **Purpose**: Multi-dimensional risk evaluation
- **Key Features**: Political, economic, legal, operational risk scoring
- **Dependencies**: Notebook 01
- **Runtime**: 3-5 minutes per assessment

#### 04. Multi-Agent Orchestration
- **Purpose**: Coordinated multi-agent analysis
- **Key Features**: Agent coordination, decision synthesis, recommendations
- **Dependencies**: Notebooks 01, 02, 03
- **Runtime**: 10-15 minutes per comprehensive analysis

#### 05. RAG Enhanced Market Research
- **Purpose**: Enhanced analysis with external data
- **Key Features**: Document ingestion, vector storage, context retrieval
- **Dependencies**: Notebooks 01-04, S3 access
- **Runtime**: 15-20 minutes (includes document processing)

#### 06. Agent Testing Guide
- **Purpose**: Comprehensive testing framework
- **Key Features**: Performance benchmarking, global testing, PDF reports
- **Dependencies**: All previous notebooks
- **Runtime**: 20-30 minutes for full test suite

#### 07. Chatbot Interface
- **Purpose**: Interactive natural language interface
- **Key Features**: NLP, global country support, conversational AI
- **Dependencies**: All previous notebooks
- **Runtime**: Instant responses after initialization

## 📖 Documentation Structure

### User Documentation
- **README.md**: Project overview, features, quick links
- **QUICK_START.md**: 30-minute setup guide
- **docs/USER_GUIDE.md**: Comprehensive usage instructions

### Technical Documentation
- **docs/AWS_SETUP.md**: Infrastructure setup and configuration
- **docs/PROJECT_OVERVIEW.md**: Architecture and technical details
- **docs/AWS_DEPLOYMENT_GUIDE.md**: Production deployment strategies

### Console Guides
- **docs/BEDROCK_CONSOLE_WALKTHROUGH.md**: Bedrock setup walkthrough
- **docs/BEDROCK_AGENTS_CONSOLE_GUIDE.md**: Advanced Bedrock configuration

## 🔧 Scripts and Utilities

### Setup Scripts
- **scripts/setup_sagemaker.py**: Automated SageMaker configuration
- **scripts/setup_rag_infrastructure.py**: RAG system initialization

### Agent Implementations
- **agents/risk_assessment_agent.py**: Standalone risk assessment
- **agents/tests/**: Unit tests for agent functionality

## 🔄 Workflows

### Development Workflow
1. **Setup**: Run AWS setup and notebook initialization
2. **Development**: Modify agents and test functionality
3. **Testing**: Use testing framework to validate changes
4. **Documentation**: Update relevant documentation

### Production Workflow
1. **Deployment**: Use deployment scripts for production setup
2. **Monitoring**: Configure CloudWatch and alerting
3. **Scaling**: Adjust instance types and auto-scaling
4. **Maintenance**: Regular updates and security patches

## 📊 File Sizes and Dependencies

### Notebook Sizes
| Notebook | Size | Cells | Dependencies |
|----------|------|-------|--------------|
| 01_bedrock_setup | ~50KB | 15 | boto3, json |
| 02_market_research | ~75KB | 20 | Notebook 01 |
| 03_risk_assessment | ~80KB | 22 | Notebook 01 |
| 04_orchestration | ~100KB | 25 | Notebooks 01-03 |
| 05_rag_enhanced | ~120KB | 30 | Notebooks 01-04, S3 |
| 06_testing_guide | ~150KB | 35 | All previous |
| 07_chatbot | ~200KB | 40 | All previous |

### Documentation Sizes
| Document | Size | Purpose |
|----------|------|---------|
| README.md | ~15KB | Project overview |
| QUICK_START.md | ~12KB | Setup guide |
| USER_GUIDE.md | ~25KB | Usage instructions |
| AWS_SETUP.md | ~20KB | Infrastructure setup |
| PROJECT_OVERVIEW.md | ~18KB | Technical details |

## 🚀 Getting Started Paths

### For Developers
1. **Clone repository**
2. **Read README.md** for overview
3. **Follow QUICK_START.md** for setup
4. **Run notebooks 01-07** in sequence
5. **Explore docs/USER_GUIDE.md** for advanced features

### For Business Users
1. **Read docs/PROJECT_OVERVIEW.md** for business context
2. **Follow QUICK_START.md** for setup
3. **Use notebook 07** (chatbot interface) for queries
4. **Generate reports** using notebook 06

### For Researchers
1. **Review docs/PROJECT_OVERVIEW.md** for methodology
2. **Setup development environment**
3. **Use notebooks 01-06** for systematic analysis
4. **Customize agents** for specific research needs

### For DevOps/Infrastructure
1. **Follow docs/AWS_SETUP.md** for infrastructure
2. **Use scripts/** for automated setup
3. **Review docs/AWS_DEPLOYMENT_GUIDE.md** for production
4. **Configure monitoring and scaling**

## 🔒 Security Considerations

### File Permissions
- **Notebooks**: Read/write for development, read-only for production
- **Scripts**: Execute permissions for setup scripts
- **Documentation**: Read-only for all users

### Sensitive Data
- **No credentials**: All credentials via AWS IAM roles
- **No PII**: No personal data stored in notebooks
- **Encryption**: All data encrypted in transit and at rest

### Access Control
- **IAM roles**: Principle of least privilege
- **VPC isolation**: Optional for enhanced security
- **Audit logging**: CloudTrail for all API calls

## 📈 Maintenance and Updates

### Regular Maintenance
- **Weekly**: Check for security updates
- **Monthly**: Review performance metrics
- **Quarterly**: Update documentation and dependencies

### Version Control
- **Git**: All code and documentation versioned
- **Releases**: Tagged releases for stable versions
- **Branches**: Feature branches for development

### Backup Strategy
- **Code**: Git repository with remote backups
- **Data**: S3 versioning and cross-region replication
- **Configuration**: Infrastructure as code (CloudFormation)

---

**📁 This structure provides a scalable, maintainable foundation for global market research capabilities.**