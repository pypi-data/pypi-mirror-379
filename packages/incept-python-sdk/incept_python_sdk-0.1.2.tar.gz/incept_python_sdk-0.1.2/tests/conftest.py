"""
Pytest configuration and fixtures for Incept SDK tests
"""

import pytest
from incept import InceptClient


@pytest.fixture
def mock_client():
    """Create a mock client for testing"""
    return InceptClient(api_key="test-api-key", base_url="https://api.test.com")


@pytest.fixture
def sample_question_response():
    """Sample question generation response"""
    return {
        "data": [
            {
                "type": "mcq",
                "question": "What is the capital of France?",
                "answer": "A",
                "difficulty": "easy",
                "explanation": "Paris is the capital and largest city of France.",
                "options": ["Paris", "London", "Berlin", "Rome"],
                "detailed_explanation": {
                    "steps": [
                        {
                            "title": "Identify the Country",
                            "content": "The question asks about France",
                            "image": None,
                            "image_alt_text": None
                        },
                        {
                            "title": "Recall Geography Knowledge",
                            "content": "Paris is the well-known capital of France",
                            "image": None,
                            "image_alt_text": None
                        }
                    ],
                    "personalized_academic_insights": [
                        {
                            "answer": "A",
                            "insight": "Knowledge of European capitals is fundamental geography"
                        }
                    ]
                },
                "voiceover_script": {
                    "question_script": "What is the capital of France?",
                    "answer_choice_scripts": ["Paris", "London", "Berlin", "Rome"],
                    "explanation_step_scripts": [
                        {
                            "step_number": 1,
                            "script": "First, identify that we're looking for France's capital"
                        },
                        {
                            "step_number": 2,
                            "script": "Paris is the capital and largest city of France"
                        }
                    ]
                },
                "image_url": None,
                "di_formats_used": [
                    {
                        "title": "Geography Introduction",
                        "format_number": "3.1",
                        "skill_name": "World Geography"
                    }
                ]
            }
        ],
        "request_id": "test-request-123",
        "total_questions": 1,
        "grade": 6,
        "evaluation": {
            "overall_score": 0.92,
            "scores": {
                "clarity": 0.95,
                "relevance": 0.90,
                "difficulty": 0.85,
                "engagement": 0.88
            },
            "recommendations": [
                "Consider adding a map visual aid",
                "Include cultural context about Paris"
            ],
            "report": "High quality geography question with clear options and good explanation structure."
        }
    }


@pytest.fixture
def sample_completions_response():
    """Sample completions response"""
    return {
        "response": "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods from carbon dioxide and water."
    }


@pytest.fixture
def sample_wolfram_response():
    """Sample Wolfram solve response"""
    return {
        "solution": "2x",
        "steps": [
            "Apply the power rule for derivatives",
            "d/dx(x^2) = 2x^(2-1) = 2x"
        ],
        "error": None
    }