"""
Comprehensive test suite for the Global Market Research API
"""

import pytest
import requests
import json
from typing import Dict, Any
import time

# Test configuration
BASE_URL = "http://localhost:8000"
API_TOKEN = "demo_token_123"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

class TestGlobalMarketResearchAPI:
    """Test suite for the Global Market Research API"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup for each test"""
        self.base_url = BASE_URL
        self.headers = HEADERS
        
        # Wait for server to be ready
        max_retries = 30
        for i in range(max_retries):
            try:
                response = requests.get(f"{self.base_url}/health", timeout=5)
                if response.status_code == 200:
                    break
            except:
                if i == max_retries - 1:
                    pytest.fail("API server not available")
                time.sleep(1)
    
    def test_health_check(self):
        """Test health check endpoint"""
        response = requests.get(f"{self.base_url}/health")
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
        assert "supported_countries" in data
    
    def test_root_endpoint(self):
        """Test root endpoint"""
        response = requests.get(f"{self.base_url}/")
        
        assert response.status_code == 200
        data = response.json()
        assert data["service"] == "Global Market Research Agents API"
        assert data["version"] == "1.0.0"
        assert "endpoints" in data
        assert data["status"] == "operational"
    
    def test_authentication_required(self):
        """Test that authentication is required"""
        response = requests.post(
            f"{self.base_url}/api/v1/chat",
            json={"query": "test query"}
        )
        
        assert response.status_code == 401
    
    def test_invalid_token(self):
        """Test invalid authentication token"""
        invalid_headers = {
            "Authorization": "Bearer invalid_token",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            f"{self.base_url}/api/v1/chat",
            headers=invalid_headers,
            json={"query": "test query"}
        )
        
        assert response.status_code == 401
    
    def test_chat_endpoint_basic(self):
        """Test basic chat functionality"""
        payload = {
            "query": "What are the risks of entering the German fintech market?",
            "session_id": "test_session_1"
        }
        
        response = requests.post(
            f"{self.base_url}/api/v1/chat",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert "session_id" in data
        assert data["session_id"] == "test_session_1"
        
        # Check response data structure
        response_data = data["data"]
        assert "response_type" in response_data
        assert "country" in response_data
        assert "industry" in response_data
        assert "message" in response_data
    
    def test_chat_endpoint_risk_assessment(self):
        """Test chat endpoint with risk assessment query"""
        payload = {
            "query": "What are the risks of investing in Bangladesh healthcare?",
            "session_id": "test_session_2"
        }
        
        response = requests.post(
            f"{self.base_url}/api/v1/chat",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        
        response_data = data["data"]
        assert response_data["response_type"] == "risk_assessment"
        assert response_data["country"] == "Bangladesh"
        assert response_data["industry"] == "healthcare"
        assert "risk_score" in response_data
        assert "risk_level" in response_data
        assert "risk_breakdown" in response_data
    
    def test_chat_endpoint_comparison(self):
        """Test chat endpoint with comparison query"""
        payload = {
            "query": "Compare technology markets in Estonia vs Latvia",
            "session_id": "test_session_3"
        }
        
        response = requests.post(
            f"{self.base_url}/api/v1/chat",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        
        response_data = data["data"]
        assert response_data["response_type"] == "comparison"
        assert response_data["industry"] == "technology"
        assert "comparisons" in response_data
        assert len(response_data["comparisons"]) >= 2
    
    def test_analyze_endpoint_market(self):
        """Test analyze endpoint with market analysis"""
        payload = {
            "country": "Rwanda",
            "industry": "fintech",
            "analysis_type": "market"
        }
        
        response = requests.post(
            f"{self.base_url}/api/v1/analyze",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        
        response_data = data["data"]
        assert response_data["response_type"] == "market_research"
        assert response_data["country"] == "Rwanda"
        assert response_data["industry"] == "fintech"
        assert "analysis" in response_data
        assert "market_size" in response_data
        assert "growth_rate" in response_data
    
    def test_analyze_endpoint_risk(self):
        """Test analyze endpoint with risk analysis"""
        payload = {
            "country": "Mongolia",
            "industry": "mining",
            "analysis_type": "risk"
        }
        
        response = requests.post(
            f"{self.base_url}/api/v1/analyze",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        
        response_data = data["data"]
        assert response_data["response_type"] == "risk_assessment"
        assert response_data["country"] == "Mongolia"
        assert response_data["industry"] == "mining"
        assert "overall_risk_score" in response_data
        assert "risk_level" in response_data
        assert "risk_scores" in response_data
    
    def test_analyze_endpoint_comprehensive(self):
        """Test analyze endpoint with comprehensive analysis"""
        payload = {
            "country": "Estonia",
            "industry": "technology",
            "analysis_type": "comprehensive"
        }
        
        response = requests.post(
            f"{self.base_url}/api/v1/analyze",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        
        response_data = data["data"]
        assert response_data["response_type"] == "comprehensive"
        assert response_data["country"] == "Estonia"
        assert response_data["industry"] == "technology"
        assert "analysis" in response_data
        
        # Check comprehensive analysis structure
        analysis = response_data["analysis"]
        assert "recommendation" in analysis
        assert "risk_assessment" in analysis
        assert "market_research" in analysis
    
    def test_compare_endpoint(self):
        """Test compare endpoint"""
        payload = {
            "countries": ["Germany", "Japan", "United Kingdom"],
            "industry": "fintech"
        }
        
        response = requests.post(
            f"{self.base_url}/api/v1/compare",
            headers=self.headers,
            json=payload
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        
        response_data = data["data"]
        assert response_data["response_type"] == "comparison"
        assert response_data["industry"] == "fintech"
        assert response_data["countries_analyzed"] == 3
        assert "comparisons" in response_data
        assert len(response_data["comparisons"]) == 3
        assert "recommended_country" in response_data
        
        # Check comparison structure
        for comparison in response_data["comparisons"]:
            assert "country" in comparison
            assert "decision" in comparison
            assert "priority" in comparison
            assert "risk_score" in comparison
            assert "risk_level" in comparison
    
    def test_list_countries(self):
        """Test list countries endpoint"""
        response = requests.get(
            f"{self.base_url}/api/v1/countries",
            headers=self.headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "total_countries" in data
        assert "countries" in data
        assert "regions" in data
        assert data["total_countries"] > 100  # Should have 195+ countries
        
        # Check that key countries are included
        countries = data["countries"]
        assert "Germany" in countries
        assert "Rwanda" in countries
        assert "Estonia" in countries
        assert "Bangladesh" in countries
    
    def test_list_industries(self):
        """Test list industries endpoint"""
        response = requests.get(
            f"{self.base_url}/api/v1/industries",
            headers=self.headers
        )
        
        assert response.status_code == 200
        data = response.json()
        assert "total_industries" in data
        assert "industries" in data
        assert data["total_industries"] > 20  # Should have 25+ industries
        
        # Check that key industries are included
        industries = data["industries"]
        assert "technology" in industries
        assert "fintech" in industries
        assert "healthcare" in industries
        assert "manufacturing" in industries
    
    def test_session_history(self):
        """Test session history endpoint"""
        session_id = "test_session_history"
        
        # First, make a chat request to create history
        chat_payload = {
            "query": "Test query for session history",
            "session_id": session_id
        }
        
        chat_response = requests.post(
            f"{self.base_url}/api/v1/chat",
            headers=self.headers,
            json=chat_payload
        )
        
        assert chat_response.status_code == 200
        
        # Now get the session history
        history_response = requests.get(
            f"{self.base_url}/api/v1/session/{session_id}",
            headers=self.headers
        )
        
        assert history_response.status_code == 200
        data = history_response.json()
        assert data["session_id"] == session_id
        assert data["conversation_count"] >= 1
        assert "history" in data
    
    def test_invalid_session_history(self):
        """Test session history with invalid session ID"""
        response = requests.get(
            f"{self.base_url}/api/v1/session/nonexistent_session",
            headers=self.headers
        )
        
        assert response.status_code == 404
    
    def test_input_validation(self):
        """Test input validation"""
        
        # Test empty query
        response = requests.post(
            f"{self.base_url}/api/v1/chat",
            headers=self.headers,
            json={"query": ""}
        )
        assert response.status_code == 422  # Validation error
        
        # Test missing required fields
        response = requests.post(
            f"{self.base_url}/api/v1/analyze",
            headers=self.headers,
            json={"country": "Germany"}  # Missing industry
        )
        assert response.status_code == 422  # Validation error
        
        # Test invalid analysis type
        response = requests.post(
            f"{self.base_url}/api/v1/analyze",
            headers=self.headers,
            json={
                "country": "Germany",
                "industry": "technology",
                "analysis_type": "invalid_type"
            }
        )
        assert response.status_code == 422  # Validation error
    
    def test_global_countries_support(self):
        """Test support for global countries"""
        
        global_test_cases = [
            {"country": "Rwanda", "industry": "fintech"},
            {"country": "Bangladesh", "industry": "healthcare"},
            {"country": "Estonia", "industry": "technology"},
            {"country": "Mongolia", "industry": "mining"},
            {"country": "Fiji", "industry": "tourism"}
        ]
        
        for test_case in global_test_cases:
            payload = {
                "country": test_case["country"],
                "industry": test_case["industry"],
                "analysis_type": "comprehensive"
            }
            
            response = requests.post(
                f"{self.base_url}/api/v1/analyze",
                headers=self.headers,
                json=payload
            )
            
            assert response.status_code == 200, f"Failed for {test_case['country']}"
            data = response.json()
            assert data["success"] is True
            assert data["data"]["country"] == test_case["country"]
            assert data["data"]["industry"] == test_case["industry"]
    
    def test_performance(self):
        """Test API performance"""
        
        # Test response time for chat endpoint
        start_time = time.time()
        
        response = requests.post(
            f"{self.base_url}/api/v1/chat",
            headers=self.headers,
            json={"query": "Quick performance test query"}
        )
        
        end_time = time.time()
        response_time = end_time - start_time
        
        assert response.status_code == 200
        assert response_time < 10.0  # Should respond within 10 seconds
        
        # Test response time for analysis endpoint
        start_time = time.time()
        
        response = requests.post(
            f"{self.base_url}/api/v1/analyze",
            headers=self.headers,
            json={
                "country": "Germany",
                "industry": "technology",
                "analysis_type": "market"
            }
        )
        
        end_time = time.time()
        response_time = end_time - start_time
        
        assert response.status_code == 200
        assert response_time < 8.0  # Should respond within 8 seconds

def run_manual_tests():
    """Run manual tests for development"""
    
    print("🧪 Running Manual API Tests")
    print("=" * 40)
    
    # Test health check
    print("\n1. Testing Health Check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test chat endpoint
    print("\n2. Testing Chat Endpoint...")
    try:
        response = requests.post(
            f"{BASE_URL}/api/v1/chat",
            headers=HEADERS,
            json={"query": "What are the risks of entering the German fintech market?"}
        )
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Response Type: {data['data']['response_type']}")
            print(f"   Country: {data['data']['country']}")
            print(f"   Industry: {data['data']['industry']}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test analysis endpoint
    print("\n3. Testing Analysis Endpoint...")
    try:
        response = requests.post(
            f"{BASE_URL}/api/v1/analyze",
            headers=HEADERS,
            json={
                "country": "Rwanda",
                "industry": "fintech",
                "analysis_type": "comprehensive"
            }
        )
        print(f"   Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Response Type: {data['data']['response_type']}")
            print(f"   Country: {data['data']['country']}")
            print(f"   Industry: {data['data']['industry']}")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n✅ Manual tests completed!")

if __name__ == "__main__":
    run_manual_tests()