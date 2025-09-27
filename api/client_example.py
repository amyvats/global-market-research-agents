"""
Example client for the Global Market Research API
Demonstrates how to interact with the API endpoints
"""

import requests
import json
from typing import Dict, Any

class MarketResearchAPIClient:
    """Client for interacting with the Global Market Research API"""
    
    def __init__(self, base_url: str = "http://localhost:8000", api_token: str = "demo_token_123"):
        """
        Initialize the API client
        
        Args:
            base_url: Base URL of the API server
            api_token: Authentication token (use demo_token_123 for demo)
        """
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
    
    def health_check(self) -> Dict[str, Any]:
        """Check API health status"""
        response = requests.get(f"{self.base_url}/health")
        return response.json()
    
    def chat_query(self, query: str, session_id: str = None, user_id: str = None) -> Dict[str, Any]:
        """
        Send a natural language query to the chatbot
        
        Args:
            query: Natural language market research question
            session_id: Optional session ID for conversation tracking
            user_id: Optional user ID for analytics
            
        Returns:
            API response with analysis results
        """
        payload = {
            "query": query,
            "session_id": session_id,
            "user_id": user_id
        }
        
        response = requests.post(
            f"{self.base_url}/api/v1/chat",
            headers=self.headers,
            json=payload
        )
        
        return response.json()
    
    def analyze_country(self, country: str, industry: str, analysis_type: str = "comprehensive") -> Dict[str, Any]:
        """
        Analyze a specific country and industry
        
        Args:
            country: Country name
            industry: Industry sector
            analysis_type: Type of analysis (market, risk, comprehensive)
            
        Returns:
            API response with analysis results
        """
        payload = {
            "country": country,
            "industry": industry,
            "analysis_type": analysis_type
        }
        
        response = requests.post(
            f"{self.base_url}/api/v1/analyze",
            headers=self.headers,
            json=payload
        )
        
        return response.json()
    
    def compare_countries(self, countries: list, industry: str) -> Dict[str, Any]:
        """
        Compare multiple countries for a specific industry
        
        Args:
            countries: List of country names
            industry: Industry sector
            
        Returns:
            API response with comparison results
        """
        payload = {
            "countries": countries,
            "industry": industry
        }
        
        response = requests.post(
            f"{self.base_url}/api/v1/compare",
            headers=self.headers,
            json=payload
        )
        
        return response.json()
    
    def list_countries(self) -> Dict[str, Any]:
        """Get list of supported countries"""
        response = requests.get(
            f"{self.base_url}/api/v1/countries",
            headers=self.headers
        )
        return response.json()
    
    def list_industries(self) -> Dict[str, Any]:
        """Get list of supported industries"""
        response = requests.get(
            f"{self.base_url}/api/v1/industries",
            headers=self.headers
        )
        return response.json()
    
    def get_session_history(self, session_id: str) -> Dict[str, Any]:
        """Get conversation history for a session"""
        response = requests.get(
            f"{self.base_url}/api/v1/session/{session_id}",
            headers=self.headers
        )
        return response.json()

def main():
    """Example usage of the API client"""
    
    # Initialize client
    client = MarketResearchAPIClient()
    
    print("🌍 Global Market Research API Client Demo")
    print("=" * 50)
    
    # 1. Health check
    print("\n1. 🏥 Health Check:")
    health = client.health_check()
    print(f"   Status: {health.get('status', 'unknown')}")
    
    # 2. Natural language chat queries
    print("\n2. 💬 Natural Language Queries:")
    
    chat_queries = [
        "What are the risks of entering the German fintech market?",
        "Should I expand my technology business to Rwanda?",
        "Compare e-commerce opportunities in Estonia vs Latvia"
    ]
    
    for i, query in enumerate(chat_queries, 1):
        print(f"\n   Query {i}: {query}")
        try:
            result = client.chat_query(query, session_id="demo_session")
            if result.get("success"):
                data = result["data"]
                print(f"   Response: {data['response_type']}")
                print(f"   Country: {data.get('country', 'N/A')}")
                print(f"   Industry: {data.get('industry', 'N/A')}")
                if 'risk_score' in data:
                    print(f"   Risk Score: {data['risk_score']}/10")
            else:
                print(f"   Error: {result.get('error', 'Unknown error')}")
        except Exception as e:
            print(f"   Error: {str(e)}")
    
    # 3. Structured country analysis
    print("\n3. 📊 Structured Analysis:")
    
    try:
        result = client.analyze_country("Bangladesh", "healthcare", "comprehensive")
        if result.get("success"):
            data = result["data"]
            print(f"   Analysis Type: {data['response_type']}")
            print(f"   Country: {data['country']}")
            print(f"   Industry: {data['industry']}")
            if 'analysis' in data and 'recommendation' in data['analysis']:
                rec = data['analysis']['recommendation']
                print(f"   Decision: {rec['decision']}")
                print(f"   Priority: {rec['priority']}")
                print(f"   Risk Score: {rec['risk_score']}/10")
        else:
            print(f"   Error: {result.get('error', 'Unknown error')}")
    except Exception as e:
        print(f"   Error: {str(e)}")
    
    # 4. Multi-country comparison
    print("\n4. 🔄 Country Comparison:")
    
    try:
        result = client.compare_countries(["Estonia", "Latvia", "Lithuania"], "technology")
        if result.get("success"):
            data = result["data"]
            print(f"   Industry: {data['industry']}")
            print(f"   Countries Analyzed: {data['countries_analyzed']}")
            print(f"   Recommended Country: {data.get('recommended_country', 'N/A')}")
            
            print("   Comparison Results:")
            for comp in data.get('comparisons', [])[:3]:
                print(f"     • {comp['country']}: {comp['decision']} (Risk: {comp['risk_score']}/10)")
        else:
            print(f"   Error: {result.get('error', 'Unknown error')}")
    except Exception as e:
        print(f"   Error: {str(e)}")
    
    # 5. List supported countries and industries
    print("\n5. 📋 Supported Resources:")
    
    try:
        countries = client.list_countries()
        industries = client.list_industries()
        
        print(f"   Supported Countries: {countries.get('total_countries', 0)}")
        print(f"   Supported Industries: {industries.get('total_industries', 0)}")
        
        # Show some examples
        if 'countries' in countries:
            print(f"   Example Countries: {', '.join(countries['countries'][:10])}...")
        
        if 'industries' in industries:
            print(f"   Example Industries: {', '.join(industries['industries'][:10])}...")
            
    except Exception as e:
        print(f"   Error: {str(e)}")
    
    print("\n✅ Demo completed!")
    print("\n💡 To run the API server:")
    print("   cd api")
    print("   pip install -r requirements.txt")
    print("   python main.py")
    print("\n📖 API Documentation: http://localhost:8000/docs")

if __name__ == "__main__":
    main()