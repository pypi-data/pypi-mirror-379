"""
Incept SDK Data Models
"""

from typing import List, Optional, Dict, Any, Literal
from pydantic import BaseModel, Field


class SkillContext(BaseModel):
    """Context information about a skill"""
    id: str
    title: str
    unit_name: str
    lesson_title: str
    standard_description: Optional[str] = None
    substandard_description: Optional[str] = None


class ExplanationStep(BaseModel):
    """Individual step in a question explanation"""
    title: str
    content: str
    image: Optional[str] = None
    image_alt_text: Optional[str] = None


class PersonalizedInsight(BaseModel):
    """Personalized academic insight"""
    answer: str
    insight: str


class DetailedExplanation(BaseModel):
    """Detailed explanation with steps and insights"""
    steps: List[ExplanationStep]
    personalized_academic_insights: List[PersonalizedInsight]


class VoiceoverStepScript(BaseModel):
    """Voiceover script for a single step"""
    step_number: int
    script: str


class VoiceoverScript(BaseModel):
    """Complete voiceover script for a question"""
    question_script: str
    answer_choice_scripts: Optional[List[str]] = None
    explanation_step_scripts: List[VoiceoverStepScript]


class EvaluationInfo(BaseModel):
    """Question evaluation information"""
    overall_score: Optional[float] = None
    scores: Optional[Dict[str, Any]] = None
    recommendations: Optional[List[str]] = None
    report: Optional[str] = None
    error: Optional[str] = None


class GeneratedQuestion(BaseModel):
    """A generated question with all associated data"""
    type: Literal["mcq"] = "mcq"
    question: str
    answer: str
    difficulty: str
    explanation: str
    options: Optional[List[str]] = None
    detailed_explanation: Optional[DetailedExplanation] = None
    voiceover_script: Optional[VoiceoverScript] = None
    image_url: Optional[str] = None
    di_formats_used: Optional[List[Dict[str, Any]]] = None


class GenerateQuestionsRequest(BaseModel):
    """Request model for generating questions"""
    grade: int = Field(..., ge=0, le=12, description="Grade level (0-12)")
    instructions: str = Field(..., description="Instructions for question generation")
    count: int = Field(default=5, ge=1, le=100, description="Number of questions")
    question_type: Literal["mcq"] = Field(default="mcq", description="Question type")
    language: str = Field(default="english", description="Language for content")
    difficulty: Optional[Literal["easy", "medium", "hard", "expert", "mixed"]] = Field(
        default="mixed", description="Difficulty level"
    )
    subject: Optional[str] = Field(default=None, description="Subject override")
    model: Optional[str] = Field(default="openai", description="AI model to use")
    translate: bool = Field(default=False, description="Enable translation")
    evaluate: bool = Field(default=False, description="Enable quality evaluation")
    skill: Optional[SkillContext] = None
    topic: Optional[str] = None
    subtopic: Optional[str] = None
    unit: Optional[str] = None
    student_level: Optional[Literal["struggling", "average", "advanced"]] = None
    previous_mistakes: Optional[List[str]] = None


class GenerateQuestionsResponse(BaseModel):
    """Response model for generated questions"""
    data: List[GeneratedQuestion]
    request_id: str
    total_questions: int
    grade: int
    evaluation: Optional[EvaluationInfo] = None


class CompletionsRequest(BaseModel):
    """Request model for completions endpoint"""
    messages: List[Dict[str, str]]
    max_tokens: int = 8000
    provider: str = "falcon"
    language: Optional[str] = "english"


class CompletionsResponse(BaseModel):
    """Response model for completions endpoint"""
    response: Any


class WolframSolveRequest(BaseModel):
    """Request model for Wolfram Alpha solve endpoint"""
    question_text: str
    subject: str
    app_id: str


class WolframSolveResponse(BaseModel):
    """Response model for Wolfram Alpha solve endpoint"""
    solution: str
    steps: Optional[List[str]] = None
    error: Optional[str] = None