#!/usr/bin/env python3
"""
Basic usage example for Incept Python SDK
"""

from incept import InceptClient
from incept.exceptions import InceptAPIError

def main():
    # Initialize client with your API key
    client = InceptClient(api_key="your-api-key-here")
    
    try:
        # Basic question generation
        print("Generating basic questions...")
        response = client.generate_questions(
            grade=5,
            instructions="Generate questions about fractions and decimals",
            count=3,
            difficulty="medium"
        )
        
        print(f"Generated {len(response.data)} questions")
        print(f"Request ID: {response.request_id}")
        
        for i, question in enumerate(response.data, 1):
            print(f"\n--- Question {i} ---")
            print(f"Question: {question.question}")
            print(f"Answer: {question.answer}")
            print(f"Difficulty: {question.difficulty}")
            if question.options:
                print(f"Options: {', '.join(question.options)}")
            print(f"Explanation: {question.explanation}")
        
        # Question generation with skill context
        print("\n" + "="*50)
        print("Generating questions with skill context...")
        
        response_with_skill = client.generate_questions(
            grade=7,
            instructions="Create problems about solving linear equations",
            count=2,
            difficulty="medium",
            subject="mathematics",
            evaluate=True,  # Enable quality evaluation
            skill={
                "id": "linear_equations",
                "title": "Linear Equations",
                "unit_name": "Algebra",
                "lesson_title": "Solving One-Step Equations"
            }
        )
        
        for i, question in enumerate(response_with_skill.data, 1):
            print(f"\n--- Algebra Question {i} ---")
            print(f"Question: {question.question}")
            print(f"Answer: {question.answer}")
            
            # Show detailed explanation if available
            if question.detailed_explanation:
                print("Detailed Steps:")
                for step in question.detailed_explanation.steps:
                    print(f"  - {step.title}: {step.content}")
        
        # Show evaluation results
        if response_with_skill.evaluation:
            print(f"\nEvaluation Score: {response_with_skill.evaluation.overall_score:.2f}")
            if response_with_skill.evaluation.recommendations:
                print("Recommendations:")
                for rec in response_with_skill.evaluation.recommendations:
                    print(f"  - {rec}")
        
        # Health check
        print("\n" + "="*50)
        print("Checking API health...")
        health = client.health_check()
        print(f"API Status: {health.get('status', 'Unknown')}")
        
    except InceptAPIError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()