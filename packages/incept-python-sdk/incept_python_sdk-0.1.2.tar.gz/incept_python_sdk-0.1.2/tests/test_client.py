"""
Tests for Incept SDK Client
"""

import pytest
import requests_mock
from unittest.mock import Mock

from incept import InceptClient
from incept.exceptions import (
    AuthenticationError,
    ValidationError,
    RateLimitError,
    ServerError,
    NetworkError,
    InceptAPIError
)


class TestInceptClient:
    """Test suite for InceptClient"""
    
    def setup_method(self):
        """Set up test client"""
        self.client = InceptClient(api_key="test-key", base_url="https://api.test.com")
    
    def test_client_initialization(self):
        """Test client initialization"""
        assert self.client.api_key == "test-key"
        assert self.client.base_url == "https://api.test.com"
        assert self.client.timeout == 30
        assert self.client.session.headers["Authorization"] == "Bearer test-key"
        assert self.client.session.headers["Content-Type"] == "application/json"
        assert "incept-python-sdk" in self.client.session.headers["User-Agent"]
    
    def test_client_custom_timeout(self):
        """Test client with custom timeout"""
        client = InceptClient(api_key="test-key", timeout=60)
        assert client.timeout == 60
    
    @requests_mock.Mocker()
    def test_generate_questions_success(self, m):
        """Test successful question generation"""
        mock_response = {
            "data": [
                {
                    "type": "mcq",
                    "question": "What is 2 + 2?",
                    "answer": "A",
                    "difficulty": "easy",
                    "explanation": "Simple addition",
                    "options": ["4", "3", "5", "6"]
                }
            ],
            "request_id": "test-123",
            "total_questions": 1,
            "grade": 5
        }
        
        m.post("https://api.test.com/v2/generate_questions", json=mock_response)
        
        response = self.client.generate_questions(
            grade=5,
            instructions="Generate math questions",
            count=1
        )
        
        assert len(response.data) == 1
        assert response.data[0].question == "What is 2 + 2?"
        assert response.data[0].answer == "A"
        assert response.request_id == "test-123"
        assert response.total_questions == 1
        assert response.grade == 5
    
    @requests_mock.Mocker()
    def test_generate_questions_with_evaluation(self, m):
        """Test question generation with evaluation"""
        mock_response = {
            "data": [
                {
                    "type": "mcq",
                    "question": "What is photosynthesis?",
                    "answer": "A",
                    "difficulty": "medium",
                    "explanation": "Process by which plants make food",
                    "options": ["Plant food production", "Animal breathing", "Water cycle", "Rock formation"]
                }
            ],
            "request_id": "test-456",
            "total_questions": 1,
            "grade": 7,
            "evaluation": {
                "overall_score": 0.85,
                "scores": {"clarity": 0.9, "relevance": 0.8},
                "recommendations": ["Add more context"],
                "report": "Good question quality"
            }
        }
        
        m.post("https://api.test.com/v2/generate_questions", json=mock_response)
        
        response = self.client.generate_questions(
            grade=7,
            instructions="Generate science questions",
            count=1,
            evaluate=True
        )
        
        assert response.evaluation is not None
        assert response.evaluation.overall_score == 0.85
        assert response.evaluation.scores["clarity"] == 0.9
        assert "Add more context" in response.evaluation.recommendations
    
    @requests_mock.Mocker()
    def test_completions_success(self, m):
        """Test successful completions request"""
        mock_response = {
            "response": "Photosynthesis is the process by which plants make food using sunlight."
        }
        
        m.post("https://api.test.com/completions", json=mock_response)
        
        response = self.client.completions(
            messages=[{"role": "user", "content": "Explain photosynthesis"}],
            provider="openai"
        )
        
        assert "photosynthesis" in response.response.lower()
    
    @requests_mock.Mocker()
    def test_wolfram_solve_success(self, m):
        """Test successful Wolfram solve request"""
        mock_response = {
            "solution": "2x",
            "steps": ["Apply power rule", "d/dx(x^2) = 2x"],
            "error": None
        }
        
        m.post("https://api.test.com/wolfram/solve", json=mock_response)
        
        response = self.client.wolfram_solve(
            question_text="What is the derivative of x^2?",
            subject="calculus",
            app_id="test-app-id"
        )
        
        assert response.solution == "2x"
        assert len(response.steps) == 2
        assert response.error is None
    
    @requests_mock.Mocker()
    def test_health_check_success(self, m):
        """Test successful health check"""
        mock_response = {"status": "healthy", "service": "incept-api"}
        m.get("https://api.test.com/health", json=mock_response)
        
        response = self.client.health_check()
        assert response["status"] == "healthy"
    
    @requests_mock.Mocker()
    def test_authentication_error(self, m):
        """Test authentication error handling"""
        m.post("https://api.test.com/v2/generate_questions", status_code=401)
        
        with pytest.raises(AuthenticationError, match="Invalid API key"):
            self.client.generate_questions(
                grade=5,
                instructions="Test",
                count=1
            )
    
    @requests_mock.Mocker()
    def test_validation_error(self, m):
        """Test validation error handling"""
        m.post(
            "https://api.test.com/v2/generate_questions",
            status_code=422,
            json={"detail": "Grade must be between 0 and 12"}
        )
        
        with pytest.raises(ValidationError, match="Grade must be between 0 and 12"):
            self.client.generate_questions(
                grade=15,
                instructions="Test",
                count=1
            )
    
    @requests_mock.Mocker()
    def test_rate_limit_error(self, m):
        """Test rate limit error handling"""
        m.post("https://api.test.com/v2/generate_questions", status_code=429)
        
        with pytest.raises(RateLimitError, match="Rate limit exceeded"):
            self.client.generate_questions(
                grade=5,
                instructions="Test",
                count=1
            )
    
    @requests_mock.Mocker()
    def test_server_error(self, m):
        """Test server error handling"""
        m.post("https://api.test.com/v2/generate_questions", status_code=500, text="Internal Server Error")
        
        with pytest.raises(ServerError, match="Server error \\(500\\)"):
            self.client.generate_questions(
                grade=5,
                instructions="Test",
                count=1
            )
    
    @requests_mock.Mocker()
    def test_network_error(self, m):
        """Test network error handling"""
        m.post("https://api.test.com/v2/generate_questions", exc=requests.exceptions.ConnectionError)
        
        with pytest.raises(NetworkError, match="Failed to connect to API"):
            self.client.generate_questions(
                grade=5,
                instructions="Test",
                count=1
            )
    
    @requests_mock.Mocker()
    def test_invalid_json_response(self, m):
        """Test invalid JSON response handling"""
        m.post("https://api.test.com/v2/generate_questions", text="Invalid JSON")
        
        with pytest.raises(InceptAPIError, match="Invalid JSON response"):
            self.client.generate_questions(
                grade=5,
                instructions="Test",
                count=1
            )
    
    def test_make_request_unsupported_method(self):
        """Test unsupported HTTP method"""
        with pytest.raises(ValueError, match="Unsupported HTTP method"):
            self.client._make_request("DELETE", "/test")
    
    @requests_mock.Mocker()
    def test_base_url_trailing_slash_handling(self, m):
        """Test that trailing slashes in base_url are handled correctly"""
        client = InceptClient(api_key="test-key", base_url="https://api.test.com/")
        assert client.base_url == "https://api.test.com"
        
        m.get("https://api.test.com/health", json={"status": "ok"})
        client.health_check()  # Should not raise an error
    
    @requests_mock.Mocker()
    def test_endpoint_leading_slash_handling(self, m):
        """Test that leading slashes in endpoints are handled correctly"""
        m.get("https://api.test.com/health", json={"status": "ok"})
        
        # Both should work the same way
        response1 = self.client._make_request("GET", "/health")
        response2 = self.client._make_request("GET", "health")
        
        assert response1 == response2 == {"status": "ok"}