"""
Multi-Agent Orchestrator for API
Coordinates market research and risk assessment agents
"""

import logging
from typing import Dict, Any
from .market_research_agent import MarketResearchAgent
from .risk_assessment_agent import RiskAssessmentAgent

logger = logging.getLogger(__name__)

class MultiAgentOrchestrator:
    """Orchestrates multiple agents for comprehensive market analysis"""
    
    def __init__(self):
        """Initialize the orchestrator with all agents"""
        self.market_agent = MarketResearchAgent()
        self.risk_agent = RiskAssessmentAgent()
        logger.info("✅ Multi-Agent Orchestrator initialized")
    
    def comprehensive_market_entry_analysis(self, country: str, industry: str) -> Dict[str, Any]:
        """
        Perform comprehensive market entry analysis using all agents
        
        Args:
            country: Target country name
            industry: Industry sector
            
        Returns:
            Dictionary containing comprehensive analysis and recommendations
        """
        
        try:
            # Get market research analysis
            logger.info(f"Running market analysis for {industry} in {country}")
            market_analysis = self.market_agent.analyze_market(country, industry)
            
            # Get risk assessment
            logger.info(f"Running risk assessment for {industry} in {country}")
            risk_analysis = self.risk_agent.comprehensive_risk_assessment(country, industry)
            
            # Generate recommendation based on both analyses
            recommendation = self._generate_recommendation(market_analysis, risk_analysis, country, industry)
            
            return {
                "country": country,
                "industry": industry,
                "market_research": market_analysis,
                "risk_assessment": risk_analysis,
                "recommendation": recommendation,
                "analysis_timestamp": "2024-01-01T00:00:00Z"  # Would use actual timestamp
            }
            
        except Exception as e:
            logger.error(f"Comprehensive analysis failed: {str(e)}")
            raise
    
    def _generate_recommendation(self, market_analysis: Dict, risk_analysis: Dict, country: str, industry: str) -> Dict[str, Any]:
        """
        Generate strategic recommendation based on market and risk analysis
        
        Args:
            market_analysis: Market research results
            risk_analysis: Risk assessment results
            country: Target country
            industry: Target industry
            
        Returns:
            Strategic recommendation with decision and priority
        """
        
        risk_score = risk_analysis["overall_risk_score"]
        market_size = market_analysis.get("market_size", 0)
        growth_rate = market_analysis.get("growth_rate", 0)
        
        # Calculate opportunity score (simplified)
        opportunity_score = self._calculate_opportunity_score(market_size, growth_rate)
        
        # Decision matrix based on risk vs opportunity
        decision, priority, confidence = self._decision_matrix(risk_score, opportunity_score)
        
        return {
            "decision": decision,
            "priority": priority,
            "confidence": confidence,
            "risk_score": risk_score,
            "opportunity_score": opportunity_score,
            "reasoning": self._generate_reasoning(decision, risk_score, opportunity_score, country, industry),
            "next_steps": self._generate_next_steps(decision, country, industry),
            "timeline": self._estimate_timeline(decision, risk_score)
        }
    
    def _calculate_opportunity_score(self, market_size: float, growth_rate: float) -> float:
        """Calculate opportunity score based on market metrics"""
        
        # Normalize market size (log scale)
        size_score = min(10, max(1, (market_size / 1000000000) * 2))  # Billions scale
        
        # Growth rate score
        growth_score = min(10, max(1, growth_rate / 2))  # 20% growth = 10 points
        
        # Combined opportunity score
        opportunity_score = (size_score + growth_score) / 2
        
        return round(opportunity_score, 1)
    
    def _decision_matrix(self, risk_score: float, opportunity_score: float) -> tuple:
        """
        Decision matrix based on risk vs opportunity
        
        Returns:
            Tuple of (decision, priority, confidence)
        """
        
        if risk_score <= 4 and opportunity_score >= 7:
            return "PROCEED_WITH_CONFIDENCE", "High", "High"
        elif risk_score <= 6 and opportunity_score >= 6:
            return "PROCEED_WITH_CAUTION", "Medium", "High"
        elif risk_score <= 8 and opportunity_score >= 5:
            return "PROCEED_WITH_MITIGATION", "Medium", "Medium"
        elif risk_score <= 6 and opportunity_score >= 4:
            return "PROCEED_WITH_CAUTION", "Low", "Medium"
        else:
            return "RECONSIDER_ENTRY", "Low", "High"
    
    def _generate_reasoning(self, decision: str, risk_score: float, opportunity_score: float, country: str, industry: str) -> str:
        """Generate reasoning for the recommendation"""
        
        reasoning_map = {
            "PROCEED_WITH_CONFIDENCE": f"Low risk ({risk_score}/10) and high opportunity ({opportunity_score}/10) make {country} an excellent market for {industry} expansion.",
            "PROCEED_WITH_CAUTION": f"Moderate risk ({risk_score}/10) with good opportunity ({opportunity_score}/10) suggest careful market entry planning for {industry} in {country}.",
            "PROCEED_WITH_MITIGATION": f"Higher risk ({risk_score}/10) requires extensive mitigation strategies, but opportunity ({opportunity_score}/10) justifies consideration for {industry} in {country}.",
            "RECONSIDER_ENTRY": f"High risk ({risk_score}/10) and limited opportunity ({opportunity_score}/10) suggest reconsidering {industry} market entry in {country}."
        }
        
        return reasoning_map.get(decision, "Analysis completed with mixed indicators.")
    
    def _generate_next_steps(self, decision: str, country: str, industry: str) -> list:
        """Generate recommended next steps based on decision"""
        
        next_steps_map = {
            "PROCEED_WITH_CONFIDENCE": [
                "Develop detailed market entry strategy",
                "Identify local partners and distributors",
                "Prepare regulatory compliance framework",
                "Allocate resources for market entry",
                "Set timeline for market launch"
            ],
            "PROCEED_WITH_CAUTION": [
                "Conduct deeper market research",
                "Develop comprehensive risk mitigation plan",
                "Establish local partnerships",
                "Create phased market entry approach",
                "Monitor market conditions closely"
            ],
            "PROCEED_WITH_MITIGATION": [
                "Develop extensive risk management framework",
                "Secure local expertise and partnerships",
                "Create contingency plans for major risks",
                "Consider pilot program or limited entry",
                "Establish exit strategy if needed"
            ],
            "RECONSIDER_ENTRY": [
                "Explore alternative markets with better risk/opportunity profile",
                "Monitor market conditions for future opportunities",
                "Consider indirect market entry through partnerships",
                "Evaluate different industry segments",
                "Reassess in 6-12 months"
            ]
        }
        
        return next_steps_map.get(decision, ["Conduct additional analysis"])
    
    def _estimate_timeline(self, decision: str, risk_score: float) -> str:
        """Estimate implementation timeline based on decision and risk"""
        
        timeline_map = {
            "PROCEED_WITH_CONFIDENCE": "3-6 months",
            "PROCEED_WITH_CAUTION": "6-12 months", 
            "PROCEED_WITH_MITIGATION": "12-18 months",
            "RECONSIDER_ENTRY": "Reassess in 6-12 months"
        }
        
        return timeline_map.get(decision, "6-12 months")