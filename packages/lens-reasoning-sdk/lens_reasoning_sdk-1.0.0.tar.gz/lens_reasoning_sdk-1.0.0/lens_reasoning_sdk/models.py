from enum import Enum

class ReasoningStepType(str, Enum):
    """Comprehensive registry of all possible reasoning step types"""

    # Core Analysis Steps
    PROBLEM_DECOMPOSITION = "problem_decomposition"
    FACT_EXTRACTION = "fact_extraction"
    EVIDENCE_GATHERING = "evidence_gathering"
    PATTERN_RECOGNITION = "pattern_recognition"
    HYPOTHESIS_FORMATION = "hypothesis_formation"

    # Logical Operations
    DEDUCTIVE_REASONING = "deductive_reasoning"
    INDUCTIVE_REASONING = "inductive_reasoning"
    ABDUCTIVE_REASONING = "abductive_reasoning"
    CAUSAL_ANALYSIS = "causal_analysis"
    CONTRADICTION_CHECK = "contradiction_check"

    # Evaluation Steps
    EVIDENCE_VALIDATION = "evidence_validation"
    CONFIDENCE_ASSESSMENT = "confidence_assessment"
    RISK_ASSESSMENT = "risk_assessment"
    COMPARATIVE_ANALYSIS = "comparative_analysis"
    QUALITY_CHECK = "quality_check"

    # Synthesis Steps
    INFORMATION_SYNTHESIS = "information_synthesis"
    CONCLUSION_FORMATION = "conclusion_formation"
    RECOMMENDATION_GENERATION = "recommendation_generation"
    DECISION_MAKING = "decision_making"

    # External Operations
    TOOL_INVOCATION = "tool_invocation"
    KNOWLEDGE_RETRIEVAL = "knowledge_retrieval"
    DOCUMENT_ANALYSIS = "document_analysis"
    WEB_SEARCH = "web_search"

    # Meta Operations
    STRATEGY_PLANNING = "strategy_planning"
    APPROACH_SELECTION = "approach_selection"
    STEP_VALIDATION = "step_validation"
    ERROR_DETECTION = "error_detection"
    COURSE_CORRECTION = "course_correction"