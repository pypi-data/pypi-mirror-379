"""
Incept API Client
"""

import requests
from typing import Optional, Dict, Any
from urllib.parse import urljoin

from .models import (
    GenerateQuestionsRequest,
    GenerateQuestionsResponse,
    CompletionsRequest,
    CompletionsResponse,
    WolframSolveRequest,
    WolframSolveResponse,
)
from .exceptions import (
    InceptAPIError,
    AuthenticationError,
    ValidationError,
    RateLimitError,
    ServerError,
    NetworkError,
)


class InceptClient:
    """
    Incept API Client
    
    A Python client for interacting with the Incept Question Generation API.
    
    Args:
        api_key: Your Incept API key
        base_url: Base URL for the API (default: https://api.incept.com)
        timeout: Request timeout in seconds (default: 30)
    
    Example:
        >>> client = InceptClient(api_key="your-api-key")
        >>> response = client.generate_questions(
        ...     grade=5,
        ...     instructions="Generate questions about fractions",
        ...     count=3
        ... )
    """
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.incept.com",
        timeout: int = 30
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "incept-python-sdk/0.1.0"
        })
    
    def _make_request(
        self, 
        method: str, 
        endpoint: str, 
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make an HTTP request to the API
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            data: Request data for POST requests
            
        Returns:
            Response data as dictionary
            
        Raises:
            InceptAPIError: For various API errors
        """
        url = urljoin(self.base_url + "/", endpoint.lstrip("/"))
        
        try:
            if method.upper() == "GET":
                response = self.session.get(url, timeout=self.timeout)
            elif method.upper() == "POST":
                response = self.session.post(url, json=data, timeout=self.timeout)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
                
        except requests.exceptions.ConnectionError as e:
            raise NetworkError(f"Failed to connect to API: {e}")
        except requests.exceptions.Timeout as e:
            raise NetworkError(f"Request timeout: {e}")
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error: {e}")
        
        # Handle HTTP status codes
        if response.status_code == 401:
            raise AuthenticationError("Invalid API key")
        elif response.status_code == 422:
            error_detail = response.json().get("detail", "Validation error")
            raise ValidationError(f"Validation error: {error_detail}")
        elif response.status_code == 429:
            raise RateLimitError("Rate limit exceeded")
        elif 500 <= response.status_code < 600:
            raise ServerError(f"Server error ({response.status_code}): {response.text}")
        elif response.status_code != 200:
            raise InceptAPIError(f"API error ({response.status_code}): {response.text}")
        
        try:
            return response.json()
        except ValueError as e:
            raise InceptAPIError(f"Invalid JSON response: {e}")
    
    def generate_questions(
        self,
        grade: int,
        instructions: str,
        count: int = 5,
        question_type: str = "mcq",
        language: str = "english",
        difficulty: Optional[str] = "mixed",
        subject: Optional[str] = None,
        model: Optional[str] = "openai",
        translate: bool = False,
        evaluate: bool = False,
        skill: Optional[Dict[str, Any]] = None,
        topic: Optional[str] = None,
        subtopic: Optional[str] = None,
        unit: Optional[str] = None,
        student_level: Optional[str] = None,
        previous_mistakes: Optional[list] = None,
    ) -> GenerateQuestionsResponse:
        """
        Generate educational questions
        
        Args:
            grade: Grade level (0-12)
            instructions: Instructions for question generation
            count: Number of questions to generate (default: 5)
            question_type: Type of questions ("mcq")
            language: Language for content (default: "english")
            difficulty: Difficulty level (default: "mixed")
            subject: Subject override
            model: AI model to use (default: "openai")
            translate: Enable translation (default: False)
            evaluate: Enable quality evaluation (default: False)
            skill: Skill context information
            topic: Topic specification
            subtopic: Subtopic specification
            unit: Unit specification
            student_level: Student level ("struggling", "average", "advanced")
            previous_mistakes: List of previous student mistakes
            
        Returns:
            GenerateQuestionsResponse object
            
        Example:
            >>> response = client.generate_questions(
            ...     grade=5,
            ...     instructions="Generate questions about fractions",
            ...     count=3,
            ...     difficulty="medium",
            ...     evaluate=True
            ... )
            >>> print(f"Generated {len(response.data)} questions")
        """
        request_data = GenerateQuestionsRequest(
            grade=grade,
            instructions=instructions,
            count=count,
            question_type=question_type,
            language=language,
            difficulty=difficulty,
            subject=subject,
            model=model,
            translate=translate,
            evaluate=evaluate,
            skill=skill,
            topic=topic,
            subtopic=subtopic,
            unit=unit,
            student_level=student_level,
            previous_mistakes=previous_mistakes,
        )
        
        response_data = self._make_request("POST", "/v2/generate_questions", request_data.dict())
        return GenerateQuestionsResponse(**response_data)
    
    def completions(
        self,
        messages: list,
        max_tokens: int = 8000,
        provider: str = "falcon",
        language: Optional[str] = "english"
    ) -> CompletionsResponse:
        """
        Get completions from the API
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            max_tokens: Maximum tokens to generate (default: 8000)
            provider: AI provider to use (default: "falcon")
            language: Response language (default: "english")
            
        Returns:
            CompletionsResponse object
            
        Example:
            >>> response = client.completions(
            ...     messages=[
            ...         {"role": "user", "content": "Explain photosynthesis"}
            ...     ],
            ...     provider="openai"
            ... )
        """
        request_data = CompletionsRequest(
            messages=messages,
            max_tokens=max_tokens,
            provider=provider,
            language=language
        )
        
        response_data = self._make_request("POST", "/completions", request_data.dict())
        return CompletionsResponse(**response_data)
    
    def wolfram_solve(
        self,
        question_text: str,
        subject: str,
        app_id: str
    ) -> WolframSolveResponse:
        """
        Solve a math problem using Wolfram Alpha
        
        Args:
            question_text: The math problem to solve
            subject: Subject area
            app_id: Wolfram Alpha App ID
            
        Returns:
            WolframSolveResponse object
            
        Example:
            >>> response = client.wolfram_solve(
            ...     question_text="What is the derivative of x^2?",
            ...     subject="calculus",
            ...     app_id="your-wolfram-app-id"
            ... )
        """
        request_data = WolframSolveRequest(
            question_text=question_text,
            subject=subject,
            app_id=app_id
        )
        
        response_data = self._make_request("POST", "/wolfram/solve", request_data.dict())
        return WolframSolveResponse(**response_data)
    
    def health_check(self) -> Dict[str, Any]:
        """
        Check API health status
        
        Returns:
            Health status dictionary
        """
        return self._make_request("GET", "/health")
    
    def get_api_documentation(self) -> Dict[str, Any]:
        """
        Get API documentation
        
        Returns:
            API documentation dictionary
        """
        return self._make_request("GET", "/api/documentation")