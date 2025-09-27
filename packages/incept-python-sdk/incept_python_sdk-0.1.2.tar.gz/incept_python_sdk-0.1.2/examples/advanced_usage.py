#!/usr/bin/env python3
"""
Advanced usage example for Incept Python SDK
"""

from incept import InceptClient
from incept.exceptions import (
    AuthenticationError,
    ValidationError,
    RateLimitError,
    ServerError,
    NetworkError,
    InceptAPIError
)

def demonstrate_completions(client):
    """Demonstrate the completions endpoint"""
    print("=== Completions Example ===")
    
    try:
        response = client.completions(
            messages=[
                {"role": "system", "content": "You are a helpful math tutor specializing in geometry."},
                {"role": "user", "content": "Explain how to calculate the area of a triangle in simple terms for a 6th grader."}
            ],
            provider="openai",
            max_tokens=500,
            language="english"
        )
        
        print("Completion Response:")
        print(response.response)
        
    except InceptAPIError as e:
        print(f"Completions error: {e}")

def demonstrate_multilingual_generation(client):
    """Demonstrate multilingual question generation"""
    print("\n=== Multilingual Generation Example ===")
    
    try:
        # Generate questions in Arabic
        response = client.generate_questions(
            grade=8,
            instructions="Generate geometry questions about triangles and circles",
            count=2,
            language="arabic",
            difficulty="medium",
            subject="geometry",
            translate=True
        )
        
        print(f"Generated {len(response.data)} questions in Arabic:")
        for i, question in enumerate(response.data, 1):
            print(f"\nQuestion {i}: {question.question}")
            print(f"Answer: {question.answer}")
            if question.options:
                print(f"Options: {', '.join(question.options)}")
                
    except InceptAPIError as e:
        print(f"Multilingual generation error: {e}")

def demonstrate_comprehensive_evaluation(client):
    """Demonstrate comprehensive question evaluation"""
    print("\n=== Comprehensive Evaluation Example ===")
    
    try:
        response = client.generate_questions(
            grade=10,
            instructions="Create challenging calculus problems about derivatives",
            count=2,
            difficulty="hard",
            subject="mathematics",
            evaluate=True,  # Enable detailed evaluation
            student_level="advanced",
            skill={
                "id": "derivatives",
                "title": "Derivatives",
                "unit_name": "Calculus",
                "lesson_title": "Basic Differentiation Rules",
                "standard_description": "Find derivatives using power rule and chain rule"
            }
        )
        
        print(f"Generated {len(response.data)} calculus questions:")
        
        for i, question in enumerate(response.data, 1):
            print(f"\n--- Question {i} ---")
            print(f"Q: {question.question}")
            print(f"A: {question.answer}")
            
            # Show DI formats used if available
            if question.di_formats_used:
                print("Direct Instruction formats used:")
                for format_info in question.di_formats_used:
                    print(f"  - {format_info.get('title', 'Unknown format')}")
            
            # Show detailed explanation
            if question.detailed_explanation:
                print("Detailed explanation steps:")
                for step in question.detailed_explanation.steps:
                    print(f"  {step.title}: {step.content}")
                
                if question.detailed_explanation.personalized_academic_insights:
                    print("Academic insights:")
                    for insight in question.detailed_explanation.personalized_academic_insights:
                        print(f"  - {insight.insight}")
        
        # Show comprehensive evaluation
        if response.evaluation:
            print(f"\n=== Evaluation Results ===")
            print(f"Overall Score: {response.evaluation.overall_score:.2%}")
            
            if response.evaluation.scores:
                print("Detailed Scores:")
                for metric, score in response.evaluation.scores.items():
                    print(f"  {metric}: {score:.2f}")
            
            if response.evaluation.recommendations:
                print("Recommendations for improvement:")
                for rec in response.evaluation.recommendations:
                    print(f"  • {rec}")
            
            if response.evaluation.report:
                print(f"\nEvaluation Report:\n{response.evaluation.report}")
                
    except InceptAPIError as e:
        print(f"Evaluation error: {e}")

def demonstrate_error_handling(client):
    """Demonstrate comprehensive error handling"""
    print("\n=== Error Handling Examples ===")
    
    # Test validation error
    try:
        client.generate_questions(
            grade=15,  # Invalid grade (>12)
            instructions="Test validation",
            count=1
        )
    except ValidationError as e:
        print(f"✓ Caught validation error: {e}")
    
    # Test with invalid client to trigger authentication error
    invalid_client = InceptClient(api_key="invalid-key")
    try:
        invalid_client.generate_questions(
            grade=5,
            instructions="Test auth",
            count=1
        )
    except AuthenticationError as e:
        print(f"✓ Caught authentication error: {e}")
    except Exception as e:
        print(f"✓ Caught error (may be network): {e}")

def main():
    """Main function demonstrating advanced SDK usage"""
    
    # Initialize client
    client = InceptClient(
        api_key="your-api-key-here",
        base_url="http://localhost:8000",  # Local development
        timeout=60
    )
    
    try:
        # Check API health first
        health = client.health_check()
        print(f"API Health: {health.get('status', 'Unknown')}")
        
        # Run demonstrations
        demonstrate_completions(client)
        demonstrate_multilingual_generation(client)
        demonstrate_comprehensive_evaluation(client)
        demonstrate_error_handling(client)
        
        print("\n=== Advanced Usage Complete ===")
        
    except NetworkError as e:
        print(f"Network error - is the API server running? {e}")
    except RateLimitError as e:
        print(f"Rate limit exceeded: {e}")
    except ServerError as e:
        print(f"Server error: {e}")
    except InceptAPIError as e:
        print(f"API error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()