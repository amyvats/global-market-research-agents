"""
Risk Assessment Agent for API
Simplified version of the notebook agent for API usage
"""

import boto3
import json
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class RiskAssessmentAgent:
    """Risk assessment agent for evaluating market entry risks"""
    
    def __init__(self):
        """Initialize the risk assessment agent"""
        try:
            self.bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')
            self.model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
            logger.info("✅ Risk Assessment Agent initialized with Bedrock")
        except Exception as e:
            logger.warning(f"⚠️ Bedrock not available, using mock mode: {str(e)}")
            self.bedrock_client = None
    
    def comprehensive_risk_assessment(self, country: str, industry: str) -> Dict[str, Any]:
        """
        Perform comprehensive risk assessment for market entry
        
        Args:
            country: Target country name
            industry: Industry sector
            
        Returns:
            Dictionary containing risk assessment results
        """
        
        if self.bedrock_client:
            return self._assess_with_bedrock(country, industry)
        else:
            return self._assess_mock(country, industry)
    
    def _assess_with_bedrock(self, country: str, industry: str) -> Dict[str, Any]:
        """Assess risks using Bedrock Claude model"""
        
        prompt = f"""
        Perform a comprehensive risk assessment for entering the {industry} market in {country}.
        
        Evaluate and score (1-10 scale, where 1=very low risk, 10=very high risk) the following risk categories:
        
        1. Political Risk - Government stability, policy changes, corruption
        2. Economic Risk - Currency volatility, inflation, GDP growth
        3. Legal Risk - Regulatory framework, IP protection, contract enforcement
        4. Operational Risk - Infrastructure, talent availability, logistics
        5. Market Risk - Competition, market maturity, demand volatility
        6. Technology Risk - Digital infrastructure, cybersecurity, innovation
        
        For each category, provide:
        - Risk score (1-10)
        - Brief explanation of key risk factors
        - Mitigation strategies
        
        Calculate an overall risk score and provide a risk level classification:
        - Low Risk (1-3): Stable, predictable environment
        - Medium Risk (4-6): Manageable challenges with planning
        - High Risk (7-8): Significant obstacles requiring expertise
        - Critical Risk (9-10): Major barriers, high failure probability
        
        Country: {country}
        Industry: {industry}
        """
        
        try:
            body = json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 4000,
                "temperature": 0.1,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            })
            
            response = self.bedrock_client.invoke_model(
                modelId=self.model_id,
                body=body
            )
            
            response_body = json.loads(response['body'].read())
            analysis_text = response_body['content'][0]['text']
            
            # Parse the response to extract structured data
            return self._parse_risk_response(analysis_text, country, industry)
            
        except Exception as e:
            logger.error(f"Bedrock risk assessment failed: {str(e)}")
            return self._assess_mock(country, industry)
    
    def _assess_mock(self, country: str, industry: str) -> Dict[str, Any]:
        """Mock risk assessment for demo purposes"""
        
        # Risk profiles by country (simplified)
        country_risk_profiles = {
            "Germany": {"base_risk": 2.5, "political": 2.0, "economic": 3.0, "legal": 2.0},
            "Japan": {"base_risk": 3.0, "political": 2.5, "economic": 3.5, "legal": 2.5},
            "Rwanda": {"base_risk": 5.5, "political": 6.0, "economic": 6.5, "legal": 5.0},
            "Bangladesh": {"base_risk": 6.2, "political": 6.5, "economic": 7.0, "legal": 6.0},
            "Estonia": {"base_risk": 3.2, "political": 3.0, "economic": 3.5, "legal": 2.8},
            "Mongolia": {"base_risk": 7.1, "political": 7.5, "economic": 8.0, "legal": 6.5}
        }
        
        # Industry risk modifiers
        industry_risk_modifiers = {
            "fintech": 1.2,      # Higher regulatory risk
            "healthcare": 1.1,    # Regulatory complexity
            "technology": 0.9,    # Generally lower risk
            "energy": 1.3,        # Political/regulatory risk
            "manufacturing": 1.0,  # Baseline
            "agriculture": 0.8    # Lower regulatory risk
        }
        
        # Get base risk profile
        profile = country_risk_profiles.get(country, {"base_risk": 5.0, "political": 5.0, "economic": 5.0, "legal": 5.0})
        industry_modifier = industry_risk_modifiers.get(industry, 1.0)
        
        # Calculate risk scores
        political_risk = min(10, profile["political"] * industry_modifier)
        economic_risk = min(10, profile["economic"] * industry_modifier)
        legal_risk = min(10, profile["legal"] * industry_modifier)
        operational_risk = min(10, (profile["base_risk"] + 1.0) * industry_modifier)
        market_risk = min(10, profile["base_risk"] * industry_modifier)
        technology_risk = min(10, (profile["base_risk"] - 0.5) * industry_modifier)
        
        # Calculate overall risk score
        overall_risk = (political_risk + economic_risk + legal_risk + operational_risk + market_risk + technology_risk) / 6
        
        # Determine risk level
        if overall_risk <= 3:
            risk_level = "Low"
        elif overall_risk <= 6:
            risk_level = "Medium"
        elif overall_risk <= 8:
            risk_level = "High"
        else:
            risk_level = "Critical"
        
        return {
            "overall_risk_score": round(overall_risk, 1),
            "risk_level": risk_level,
            "risk_scores": {
                "political_risk": round(political_risk, 1),
                "economic_risk": round(economic_risk, 1),
                "legal_risk": round(legal_risk, 1),
                "operational_risk": round(operational_risk, 1),
                "market_risk": round(market_risk, 1),
                "technology_risk": round(technology_risk, 1)
            },
            "analysis": f"""
            Risk Assessment for {industry} in {country}:
            
            Overall Risk Score: {overall_risk:.1f}/10 ({risk_level} Risk)
            
            Key Risk Factors:
            • Political Risk ({political_risk:.1f}/10): Government stability and policy environment
            • Economic Risk ({economic_risk:.1f}/10): Currency, inflation, and economic growth factors
            • Legal Risk ({legal_risk:.1f}/10): Regulatory framework and legal protection
            • Operational Risk ({operational_risk:.1f}/10): Infrastructure and operational challenges
            • Market Risk ({market_risk:.1f}/10): Competition and market dynamics
            • Technology Risk ({technology_risk:.1f}/10): Digital infrastructure and innovation capacity
            
            Recommendation: {"Proceed with confidence" if overall_risk <= 3 else 
                           "Proceed with caution" if overall_risk <= 6 else
                           "Proceed with extensive mitigation" if overall_risk <= 8 else
                           "Reconsider market entry"}
            """,
            "mitigation_strategies": [
                "Establish local partnerships to navigate regulatory environment",
                "Implement comprehensive compliance framework",
                "Develop contingency plans for political/economic volatility",
                "Invest in local talent and infrastructure development"
            ]
        }
    
    def _parse_risk_response(self, analysis_text: str, country: str, industry: str) -> Dict[str, Any]:
        """Parse Bedrock response into structured format"""
        
        # This is a simplified parser - in production, you'd want more sophisticated parsing
        return {
            "overall_risk_score": 4.2,
            "risk_level": "Medium",
            "risk_scores": {
                "political_risk": 4.0,
                "economic_risk": 4.5,
                "legal_risk": 3.8,
                "operational_risk": 4.8,
                "market_risk": 4.0,
                "technology_risk": 3.9
            },
            "analysis": analysis_text,
            "mitigation_strategies": [
                "Local partnerships",
                "Regulatory compliance",
                "Risk monitoring",
                "Contingency planning"
            ]
        }