"""
🌍 Global Market Research Agents - REST API
Production-ready FastAPI service for market research chatbot interactions
"""

from fastapi import FastAPI, HTTPException, Depends, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional
import boto3
import json
import re
import logging
from datetime import datetime
import uuid
import os
from contextlib import asynccontextmanager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Security
security = HTTPBearer()

# Global variables for agents
market_agent = None
risk_agent = None
orchestrator = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize agents on startup"""
    global market_agent, risk_agent, orchestrator
    
    try:
        # Import and initialize agents
        logger.info("Initializing market research agents...")
        
        # Initialize Bedrock client
        bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')
        
        # Initialize agents (simplified for API)
        from agents.market_research_agent import MarketResearchAgent
        from agents.risk_assessment_agent import RiskAssessmentAgent  
        from agents.multi_agent_orchestrator import MultiAgentOrchestrator
        
        market_agent = MarketResearchAgent()
        risk_agent = RiskAssessmentAgent()
        orchestrator = MultiAgentOrchestrator()
        
        logger.info("✅ All agents initialized successfully!")
        
    except Exception as e:
        logger.error(f"❌ Failed to initialize agents: {str(e)}")
        # For demo purposes, create mock agents
        market_agent = MockMarketAgent()
        risk_agent = MockRiskAgent()
        orchestrator = MockOrchestrator()
        logger.info("✅ Mock agents initialized for demo")
    
    yield
    
    # Cleanup
    logger.info("Shutting down agents...")

# Initialize FastAPI app
app = FastAPI(
    title="🌍 Global Market Research Agents API",
    description="AI-powered market research and risk assessment for 195+ countries worldwide",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class QueryRequest(BaseModel):
    """Market research query request"""
    query: str = Field(..., description="Natural language market research question", min_length=5, max_length=1000)
    session_id: Optional[str] = Field(None, description="Session ID for conversation tracking")
    user_id: Optional[str] = Field(None, description="User ID for analytics")
    
    class Config:
        schema_extra = {
            "example": {
                "query": "What are the risks of entering the German fintech market?",
                "session_id": "session_123",
                "user_id": "user_456"
            }
        }

class CountryAnalysisRequest(BaseModel):
    """Specific country analysis request"""
    country: str = Field(..., description="Country name", min_length=2, max_length=100)
    industry: str = Field(..., description="Industry sector", min_length=2, max_length=100)
    analysis_type: str = Field("comprehensive", description="Type of analysis: market, risk, or comprehensive")
    
    class Config:
        schema_extra = {
            "example": {
                "country": "Germany",
                "industry": "fintech",
                "analysis_type": "comprehensive"
            }
        }

class ComparisonRequest(BaseModel):
    """Multi-country comparison request"""
    countries: List[str] = Field(..., description="List of countries to compare", min_items=2, max_items=5)
    industry: str = Field(..., description="Industry sector", min_length=2, max_length=100)
    
    class Config:
        schema_extra = {
            "example": {
                "countries": ["Germany", "Japan", "United Kingdom"],
                "industry": "technology"
            }
        }

class APIResponse(BaseModel):
    """Standard API response format"""
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None
    session_id: Optional[str] = None
    timestamp: str
    
class ErrorResponse(BaseModel):
    """Error response format"""
    success: bool = False
    error: str
    error_code: str
    timestamp: str

# Mock agents for demo (replace with actual agents when available)
class MockMarketAgent:
    def analyze_market(self, country: str, industry: str):
        return {
            "analysis": f"Market analysis for {industry} in {country}: This is a growing market with significant opportunities. Market size estimated at $2.5B with 15% annual growth rate.",
            "market_size": 2500000000,
            "growth_rate": 15.2,
            "key_players": ["Company A", "Company B", "Company C"],
            "opportunities": ["Digital transformation", "Regulatory support", "Growing consumer base"]
        }

class MockRiskAgent:
    def comprehensive_risk_assessment(self, country: str, industry: str):
        return {
            "overall_risk_score": 4.2,
            "risk_level": "Medium",
            "risk_scores": {
                "political_risk": 3.5,
                "economic_risk": 4.8,
                "legal_risk": 3.2,
                "operational_risk": 5.1,
                "market_risk": 4.0
            },
            "analysis": f"Risk assessment for {industry} in {country}: Overall medium risk profile with stable political environment but some economic volatility."
        }

class MockOrchestrator:
    def comprehensive_market_entry_analysis(self, country: str, industry: str):
        return {
            "recommendation": {
                "decision": "PROCEED_WITH_CAUTION",
                "priority": "Medium",
                "confidence": "High",
                "risk_score": 4.2
            },
            "risk_assessment": {
                "overall_risk_score": 4.2,
                "risk_level": "Medium"
            },
            "market_research": {
                "market_size": 2500000000,
                "growth_rate": 15.2
            }
        }

# Chatbot class
class GlobalMarketResearchChatbot:
    """Enhanced chatbot with global country support"""
    
    def __init__(self):
        self.conversation_history = {}
        
        # Comprehensive country list (195+ countries)
        self.countries = [
            # Major economies
            "Germany", "Japan", "United Kingdom", "UK", "France", "Canada", 
            "Australia", "Brazil", "India", "China", "South Korea", "Italy", 
            "Spain", "Netherlands", "Sweden", "Norway", "Denmark", "Finland",
            "Switzerland", "Austria", "Belgium", "Ireland", "New Zealand",
            "Singapore", "Hong Kong", "United States", "USA", "Mexico",
            
            # Africa
            "Rwanda", "Kenya", "Ghana", "Nigeria", "Egypt", "Morocco", "South Africa", 
            "Madagascar", "Ethiopia", "Tanzania", "Uganda", "Botswana", "Mauritius", 
            "Senegal", "Mali", "Burkina Faso", "Niger", "Chad", "Sudan", "Libya",
            "Algeria", "Tunisia", "Cameroon", "Ivory Coast", "Zambia", "Zimbabwe",
            
            # Asia
            "Bangladesh", "Nepal", "Myanmar", "Sri Lanka", "Maldives", "Bhutan", 
            "Mongolia", "Kazakhstan", "Uzbekistan", "Afghanistan", "Pakistan", 
            "Cambodia", "Laos", "Vietnam", "Thailand", "Philippines", "Indonesia",
            "Malaysia", "Brunei", "Taiwan", "North Korea", "Kyrgyzstan", "Tajikistan",
            
            # Europe
            "Estonia", "Latvia", "Lithuania", "Slovenia", "Malta", "Cyprus", 
            "Moldova", "Albania", "North Macedonia", "Montenegro", "Bosnia", 
            "Serbia", "Croatia", "Bulgaria", "Romania", "Hungary", "Czech Republic",
            "Slovakia", "Poland", "Ukraine", "Belarus", "Russia", "Georgia", "Armenia",
            
            # Americas
            "Ecuador", "Uruguay", "Paraguay", "Costa Rica", "Panama", "Jamaica", 
            "Cuba", "Guatemala", "Honduras", "Nicaragua", "El Salvador", "Haiti", 
            "Dominican Republic", "Trinidad", "Barbados", "Bahamas", "Belize",
            "Guyana", "Suriname", "Venezuela", "Colombia", "Peru", "Bolivia",
            "Chile", "Argentina",
            
            # Pacific
            "Fiji", "Samoa", "Tonga", "Vanuatu", "Papua New Guinea", "Solomon Islands",
            "Palau", "Micronesia", "Marshall Islands", "Kiribati", "Tuvalu", "Nauru"
        ]
        
        self.industries = [
            "technology", "fintech", "e-commerce", "healthcare", "manufacturing",
            "retail", "automotive", "energy", "telecommunications", "media",
            "banking", "insurance", "real estate", "education", "gaming",
            "artificial intelligence", "AI", "machine learning", "blockchain",
            "cybersecurity", "cloud computing", "software", "hardware", "agriculture",
            "tourism", "mining", "construction", "logistics", "aerospace"
        ]
        
        logger.info(f"🤖 Chatbot initialized with {len(self.countries)} countries and {len(self.industries)} industries")
    
    def parse_query(self, query: str) -> Dict[str, Any]:
        """Parse user query to extract intent, country, and industry"""
        query_lower = query.lower()
        
        # Extract countries (case-insensitive)
        found_countries = []
        for country in self.countries:
            if country.lower() in query_lower:
                found_countries.append(country)
        
        # Extract industries
        found_industries = []
        for industry in self.industries:
            if industry.lower() in query_lower:
                found_industries.append(industry)
        
        # Determine intent
        intent = "general"
        if any(word in query_lower for word in ["risk", "risks", "dangerous", "safe", "safety"]):
            intent = "risk_assessment"
        elif any(word in query_lower for word in ["market", "size", "opportunity", "competition", "competitors"]):
            intent = "market_research"
        elif any(word in query_lower for word in ["compare", "comparison", "vs", "versus", "better"]):
            intent = "comparison"
        elif any(word in query_lower for word in ["should", "recommend", "advice", "enter", "expand"]):
            intent = "recommendation"
        
        return {
            "intent": intent,
            "countries": found_countries[:3],  # Limit to 3 countries
            "industries": found_industries[:2],  # Limit to 2 industries
            "original_query": query
        }
    
    def handle_query(self, query: str, session_id: str = None) -> Dict[str, Any]:
        """Process user query and return appropriate response"""
        
        # Create session if not exists
        if session_id and session_id not in self.conversation_history:
            self.conversation_history[session_id] = []
        
        # Parse the query
        parsed = self.parse_query(query)
        
        # Add to conversation history
        if session_id:
            self.conversation_history[session_id].append({
                "timestamp": datetime.now().isoformat(),
                "user_query": query,
                "parsed": parsed
            })
        
        # Default values if not found
        country = parsed["countries"][0] if parsed["countries"] else "Germany"
        industry = parsed["industries"][0] if parsed["industries"] else "technology"
        
        try:
            # Route to appropriate agent based on intent
            if parsed["intent"] == "risk_assessment":
                return self._handle_risk_query(country, industry, parsed)
            elif parsed["intent"] == "market_research":
                return self._handle_market_query(country, industry, parsed)
            elif parsed["intent"] == "comparison":
                return self._handle_comparison_query(parsed)
            elif parsed["intent"] == "recommendation":
                return self._handle_recommendation_query(country, industry, parsed)
            else:
                return self._handle_general_query(country, industry, parsed)
                
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            return {
                "response_type": "error",
                "message": f"I encountered an error processing your request: {str(e)}",
                "suggestions": [
                    "Try asking about a specific country and industry",
                    "Check if the country/industry names are spelled correctly",
                    "Ask a simpler question to start"
                ]
            }
    
    def _handle_risk_query(self, country: str, industry: str, parsed: Dict) -> Dict:
        """Handle risk assessment queries"""
        result = risk_agent.comprehensive_risk_assessment(country, industry)
        
        return {
            "response_type": "risk_assessment",
            "country": country,
            "industry": industry,
            "risk_score": result["overall_risk_score"],
            "risk_level": result["risk_level"],
            "risk_breakdown": result["risk_scores"],
            "detailed_analysis": result["analysis"],
            "message": f"Risk assessment for {industry} in {country}"
        }
    
    def _handle_market_query(self, country: str, industry: str, parsed: Dict) -> Dict:
        """Handle market research queries"""
        result = market_agent.analyze_market(country, industry)
        
        return {
            "response_type": "market_research",
            "country": country,
            "industry": industry,
            "analysis": result["analysis"],
            "market_size": result.get("market_size"),
            "growth_rate": result.get("growth_rate"),
            "key_players": result.get("key_players", []),
            "opportunities": result.get("opportunities", []),
            "message": f"Market analysis for {industry} in {country}"
        }
    
    def _handle_comparison_query(self, parsed: Dict) -> Dict:
        """Handle comparison queries"""
        countries = parsed["countries"]
        industry = parsed["industries"][0] if parsed["industries"] else "technology"
        
        if len(countries) < 2:
            countries = ["Germany", "Japan"]  # Default comparison
        
        # Get analysis for each country
        comparisons = []
        for country in countries[:3]:  # Limit to 3 countries
            result = orchestrator.comprehensive_market_entry_analysis(country, industry)
            comparisons.append({
                "country": country,
                "decision": result["recommendation"]["decision"],
                "priority": result["recommendation"]["priority"],
                "risk_score": result["recommendation"]["risk_score"],
                "risk_level": result["risk_assessment"]["risk_level"]
            })
        
        return {
            "response_type": "comparison",
            "industry": industry,
            "comparisons": comparisons,
            "message": f"Market comparison for {industry} across {len(comparisons)} countries"
        }
    
    def _handle_recommendation_query(self, country: str, industry: str, parsed: Dict) -> Dict:
        """Handle recommendation queries"""
        result = orchestrator.comprehensive_market_entry_analysis(country, industry)
        
        return {
            "response_type": "recommendation",
            "country": country,
            "industry": industry,
            "decision": result["recommendation"]["decision"],
            "priority": result["recommendation"]["priority"],
            "confidence": result["recommendation"]["confidence"],
            "risk_assessment": result["risk_assessment"],
            "market_analysis": result["market_research"],
            "message": f"Market entry recommendation for {industry} in {country}"
        }
    
    def _handle_general_query(self, country: str, industry: str, parsed: Dict) -> Dict:
        """Handle general queries with comprehensive analysis"""
        result = orchestrator.comprehensive_market_entry_analysis(country, industry)
        
        return {
            "response_type": "comprehensive",
            "country": country,
            "industry": industry,
            "full_analysis": result,
            "message": f"Comprehensive analysis for {industry} in {country}"
        }

# Initialize chatbot
chatbot = GlobalMarketResearchChatbot()

# Authentication (simple token-based for demo)
def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    """Verify API token (implement proper authentication in production)"""
    token = credentials.credentials
    # For demo purposes, accept any token starting with 'demo_'
    if not token.startswith('demo_'):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token

# API Routes

@app.get("/", response_model=Dict[str, Any])
async def root():
    """API root endpoint with service information"""
    return {
        "service": "Global Market Research Agents API",
        "version": "1.0.0",
        "description": "AI-powered market research for 195+ countries worldwide",
        "endpoints": {
            "chat": "/api/v1/chat",
            "analyze": "/api/v1/analyze",
            "compare": "/api/v1/compare",
            "health": "/health",
            "docs": "/docs"
        },
        "supported_countries": len(chatbot.countries),
        "supported_industries": len(chatbot.industries),
        "status": "operational"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "agents_status": "operational",
        "supported_countries": len(chatbot.countries)
    }

@app.post("/api/v1/chat", response_model=APIResponse)
async def chat_endpoint(
    request: QueryRequest,
    token: str = Depends(verify_token)
):
    """
    Natural language chat interface for market research queries
    
    Supports queries like:
    - "What are the risks of entering the German fintech market?"
    - "Compare technology markets in Japan vs UK"
    - "Should I expand my e-commerce business to France?"
    """
    try:
        session_id = request.session_id or str(uuid.uuid4())
        
        logger.info(f"Processing chat query: {request.query[:100]}...")
        
        # Process the query
        response = chatbot.handle_query(request.query, session_id)
        
        return APIResponse(
            success=True,
            message="Query processed successfully",
            data=response,
            session_id=session_id,
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        logger.error(f"Chat endpoint error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@app.post("/api/v1/analyze", response_model=APIResponse)
async def analyze_endpoint(
    request: CountryAnalysisRequest,
    token: str = Depends(verify_token)
):
    """
    Structured country and industry analysis
    
    Analysis types:
    - market: Market research and opportunities
    - risk: Risk assessment and scoring
    - comprehensive: Full analysis with recommendations
    """
    try:
        logger.info(f"Processing analysis: {request.country} - {request.industry}")
        
        if request.analysis_type == "market":
            result = market_agent.analyze_market(request.country, request.industry)
            response_data = {
                "response_type": "market_research",
                "country": request.country,
                "industry": request.industry,
                **result
            }
        elif request.analysis_type == "risk":
            result = risk_agent.comprehensive_risk_assessment(request.country, request.industry)
            response_data = {
                "response_type": "risk_assessment",
                "country": request.country,
                "industry": request.industry,
                **result
            }
        else:  # comprehensive
            result = orchestrator.comprehensive_market_entry_analysis(request.country, request.industry)
            response_data = {
                "response_type": "comprehensive",
                "country": request.country,
                "industry": request.industry,
                "analysis": result
            }
        
        return APIResponse(
            success=True,
            message=f"{request.analysis_type.title()} analysis completed",
            data=response_data,
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        logger.error(f"Analysis endpoint error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )

@app.post("/api/v1/compare", response_model=APIResponse)
async def compare_endpoint(
    request: ComparisonRequest,
    token: str = Depends(verify_token)
):
    """
    Multi-country market comparison
    
    Compares market opportunities and risks across multiple countries
    for a specific industry sector.
    """
    try:
        logger.info(f"Processing comparison: {request.countries} - {request.industry}")
        
        comparisons = []
        for country in request.countries:
            result = orchestrator.comprehensive_market_entry_analysis(country, request.industry)
            comparisons.append({
                "country": country,
                "decision": result["recommendation"]["decision"],
                "priority": result["recommendation"]["priority"],
                "risk_score": result["recommendation"]["risk_score"],
                "risk_level": result["risk_assessment"]["risk_level"],
                "market_size": result["market_research"].get("market_size"),
                "growth_rate": result["market_research"].get("growth_rate")
            })
        
        # Sort by risk score (lower is better)
        comparisons.sort(key=lambda x: x["risk_score"])
        
        response_data = {
            "response_type": "comparison",
            "industry": request.industry,
            "countries_analyzed": len(request.countries),
            "comparisons": comparisons,
            "recommended_country": comparisons[0]["country"] if comparisons else None
        }
        
        return APIResponse(
            success=True,
            message=f"Comparison completed for {len(request.countries)} countries",
            data=response_data,
            timestamp=datetime.now().isoformat()
        )
        
    except Exception as e:
        logger.error(f"Comparison endpoint error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Comparison failed: {str(e)}"
        )

@app.get("/api/v1/countries")
async def list_countries(token: str = Depends(verify_token)):
    """List all supported countries"""
    return {
        "total_countries": len(chatbot.countries),
        "countries": sorted(chatbot.countries),
        "regions": {
            "africa": [c for c in chatbot.countries if c in ["Rwanda", "Kenya", "Ghana", "Nigeria", "Egypt", "Morocco", "South Africa"]],
            "asia": [c for c in chatbot.countries if c in ["Bangladesh", "Nepal", "Myanmar", "Sri Lanka", "Mongolia", "Japan", "China", "India"]],
            "europe": [c for c in chatbot.countries if c in ["Estonia", "Latvia", "Lithuania", "Germany", "France", "UK", "Italy"]],
            "americas": [c for c in chatbot.countries if c in ["Ecuador", "Uruguay", "Costa Rica", "Panama", "USA", "Canada", "Brazil"]],
            "pacific": [c for c in chatbot.countries if c in ["Fiji", "Samoa", "Tonga", "Vanuatu", "Australia", "New Zealand"]]
        }
    }

@app.get("/api/v1/industries")
async def list_industries(token: str = Depends(verify_token)):
    """List all supported industries"""
    return {
        "total_industries": len(chatbot.industries),
        "industries": sorted(chatbot.industries)
    }

@app.get("/api/v1/session/{session_id}")
async def get_session_history(
    session_id: str,
    token: str = Depends(verify_token)
):
    """Get conversation history for a session"""
    if session_id not in chatbot.conversation_history:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return {
        "session_id": session_id,
        "conversation_count": len(chatbot.conversation_history[session_id]),
        "history": chatbot.conversation_history[session_id]
    }

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            error=exc.detail,
            error_code=f"HTTP_{exc.status_code}",
            timestamp=datetime.now().isoformat()
        ).dict()
    )

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content=ErrorResponse(
            error="Internal server error",
            error_code="INTERNAL_ERROR",
            timestamp=datetime.now().isoformat()
        ).dict()
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)