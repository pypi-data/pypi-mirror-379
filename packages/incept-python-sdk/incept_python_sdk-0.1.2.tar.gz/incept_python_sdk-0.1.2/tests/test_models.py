"""
Tests for Incept SDK Models
"""

import pytest
from pydantic import ValidationError

from incept.models import (
    GenerateQuestionsRequest,
    GenerateQuestionsResponse,
    GeneratedQuestion,
    SkillContext,
    EvaluationInfo,
    CompletionsRequest,
    WolframSolveRequest
)


class TestGenerateQuestionsRequest:
    """Test suite for GenerateQuestionsRequest model"""
    
    def test_valid_request(self):
        """Test valid request creation"""
        request = GenerateQuestionsRequest(
            grade=5,
            instructions="Generate math questions"
        )
        
        assert request.grade == 5
        assert request.instructions == "Generate math questions"
        assert request.count == 5  # default value
        assert request.question_type == "mcq"  # default value
        assert request.language == "english"  # default value
        assert request.difficulty == "mixed"  # default value
    
    def test_request_with_all_fields(self):
        """Test request with all fields populated"""
        skill = SkillContext(
            id="math_basic",
            title="Basic Math",
            unit_name="Arithmetic",
            lesson_title="Addition"
        )
        
        request = GenerateQuestionsRequest(
            grade=7,
            instructions="Create algebra problems",
            count=10,
            question_type="mcq",
            language="arabic",
            difficulty="hard",
            subject="mathematics",
            model="openai",
            translate=True,
            evaluate=True,
            skill=skill,
            topic="Linear Equations",
            subtopic="One-step equations",
            unit="Algebra Unit 1",
            student_level="advanced",
            previous_mistakes=["Forgot to isolate variable"]
        )
        
        assert request.grade == 7
        assert request.count == 10
        assert request.language == "arabic"
        assert request.difficulty == "hard"
        assert request.translate is True
        assert request.evaluate is True
        assert request.skill.title == "Basic Math"
        assert request.topic == "Linear Equations"
        assert request.student_level == "advanced"
        assert len(request.previous_mistakes) == 1
    
    def test_invalid_grade_bounds(self):
        """Test invalid grade bounds"""
        # Grade too low
        with pytest.raises(ValidationError):
            GenerateQuestionsRequest(
                grade=-1,
                instructions="Test"
            )
        
        # Grade too high
        with pytest.raises(ValidationError):
            GenerateQuestionsRequest(
                grade=13,
                instructions="Test"
            )
    
    def test_invalid_count_bounds(self):
        """Test invalid count bounds"""
        # Count too low
        with pytest.raises(ValidationError):
            GenerateQuestionsRequest(
                grade=5,
                instructions="Test",
                count=0
            )
        
        # Count too high
        with pytest.raises(ValidationError):
            GenerateQuestionsRequest(
                grade=5,
                instructions="Test",
                count=101
            )
    
    def test_valid_difficulty_values(self):
        """Test valid difficulty values"""
        valid_difficulties = ["easy", "medium", "hard", "expert", "mixed"]
        
        for difficulty in valid_difficulties:
            request = GenerateQuestionsRequest(
                grade=5,
                instructions="Test",
                difficulty=difficulty
            )
            assert request.difficulty == difficulty
    
    def test_valid_student_level_values(self):
        """Test valid student level values"""
        valid_levels = ["struggling", "average", "advanced"]
        
        for level in valid_levels:
            request = GenerateQuestionsRequest(
                grade=5,
                instructions="Test",
                student_level=level
            )
            assert request.student_level == level


class TestGeneratedQuestion:
    """Test suite for GeneratedQuestion model"""
    
    def test_minimal_question(self):
        """Test minimal valid question"""
        question = GeneratedQuestion(
            question="What is 2 + 2?",
            answer="A",
            difficulty="easy",
            explanation="Simple addition"
        )
        
        assert question.type == "mcq"  # default value
        assert question.question == "What is 2 + 2?"
        assert question.answer == "A"
        assert question.difficulty == "easy"
        assert question.explanation == "Simple addition"
        assert question.options is None
    
    def test_complete_question(self):
        """Test complete question with all fields"""
        question = GeneratedQuestion(
            type="mcq",
            question="What is photosynthesis?",
            answer="A",
            difficulty="medium",
            explanation="The process by which plants make food",
            options=["Food production", "Respiration", "Digestion", "Circulation"],
            image_url="https://example.com/image.png",
            di_formats_used=[{"format": "5.1", "title": "Science Introduction"}]
        )
        
        assert question.type == "mcq"
        assert len(question.options) == 4
        assert question.image_url == "https://example.com/image.png"
        assert len(question.di_formats_used) == 1


class TestSkillContext:
    """Test suite for SkillContext model"""
    
    def test_minimal_skill_context(self):
        """Test minimal skill context"""
        skill = SkillContext(
            id="math_001",
            title="Basic Addition",
            unit_name="Arithmetic",
            lesson_title="Single Digit Addition"
        )
        
        assert skill.id == "math_001"
        assert skill.title == "Basic Addition"
        assert skill.unit_name == "Arithmetic"
        assert skill.lesson_title == "Single Digit Addition"
        assert skill.standard_description is None
    
    def test_complete_skill_context(self):
        """Test complete skill context"""
        skill = SkillContext(
            id="algebra_001",
            title="Linear Equations",
            unit_name="Algebra",
            lesson_title="Solving One-Step Equations",
            standard_description="Solve linear equations in one variable",
            substandard_description="Use inverse operations to isolate variables"
        )
        
        assert skill.standard_description == "Solve linear equations in one variable"
        assert skill.substandard_description == "Use inverse operations to isolate variables"


class TestEvaluationInfo:
    """Test suite for EvaluationInfo model"""
    
    def test_minimal_evaluation(self):
        """Test minimal evaluation info"""
        eval_info = EvaluationInfo()
        
        assert eval_info.overall_score is None
        assert eval_info.scores is None
        assert eval_info.recommendations is None
        assert eval_info.report is None
        assert eval_info.error is None
    
    def test_complete_evaluation(self):
        """Test complete evaluation info"""
        eval_info = EvaluationInfo(
            overall_score=0.85,
            scores={"clarity": 0.9, "relevance": 0.8, "difficulty": 0.85},
            recommendations=["Add visual aids", "Simplify language"],
            report="Overall good quality with room for improvement",
            error=None
        )
        
        assert eval_info.overall_score == 0.85
        assert len(eval_info.scores) == 3
        assert len(eval_info.recommendations) == 2
        assert "good quality" in eval_info.report
    
    def test_evaluation_with_error(self):
        """Test evaluation with error"""
        eval_info = EvaluationInfo(
            error="Evaluation service unavailable"
        )
        
        assert eval_info.error == "Evaluation service unavailable"
        assert eval_info.overall_score is None


class TestCompletionsRequest:
    """Test suite for CompletionsRequest model"""
    
    def test_minimal_completions_request(self):
        """Test minimal completions request"""
        request = CompletionsRequest(
            messages=[{"role": "user", "content": "Hello"}]
        )
        
        assert len(request.messages) == 1
        assert request.max_tokens == 8000  # default
        assert request.provider == "falcon"  # default
        assert request.language == "english"  # default
    
    def test_complete_completions_request(self):
        """Test complete completions request"""
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Explain quantum physics"}
        ]
        
        request = CompletionsRequest(
            messages=messages,
            max_tokens=1000,
            provider="openai",
            language="spanish"
        )
        
        assert len(request.messages) == 2
        assert request.max_tokens == 1000
        assert request.provider == "openai"
        assert request.language == "spanish"


class TestWolframSolveRequest:
    """Test suite for WolframSolveRequest model"""
    
    def test_wolfram_request(self):
        """Test Wolfram solve request"""
        request = WolframSolveRequest(
            question_text="What is the derivative of x^2?",
            subject="calculus",
            app_id="test-app-123"
        )
        
        assert request.question_text == "What is the derivative of x^2?"
        assert request.subject == "calculus"
        assert request.app_id == "test-app-123"