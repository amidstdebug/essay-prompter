from __future__ import annotations

# ruff: noqa: E501,UP006,UP035,UP045
import random
from typing import Any, Dict, List, Optional

ESSAY_TYPES: List[Dict[str, Any]] = [
    {"id": "narrative", "name": "Narrative", "purpose": "Tell a story with reflection and meaning", "complexity": 1},
    {"id": "expository", "name": "Expository", "purpose": "Explain a concept clearly and logically", "complexity": 1},
    {"id": "analytical", "name": "Analytical", "purpose": "Break down a topic into parts and interpret how it works", "complexity": 2},
    {"id": "argumentative", "name": "Argumentative", "purpose": "Take a position and defend it with reasoning and evidence", "complexity": 3},
    {"id": "synthesis", "name": "Synthesis", "purpose": "Integrate multiple perspectives or sources into one coherent view", "complexity": 4},
]

TOPIC_OPTIONS: List[Dict[str, Any]] = [
    {"id": "topic_01", "domain": "History", "prompt_seed": "How the personal computer changed work, education, and home life from the 1970s to the 2000s", "complexity": 2},
    {"id": "topic_02", "domain": "Science", "prompt_seed": "Should gene editing be limited to disease prevention, or allowed for human enhancement", "complexity": 3},
    {"id": "topic_03", "domain": "Maths", "prompt_seed": "Why statistical thinking matters in elections, health reporting, and daily decisions", "complexity": 2},
    {"id": "topic_04", "domain": "Geography", "prompt_seed": "How geography shapes the rise of major port cities and trade networks", "complexity": 2},
    {"id": "topic_05", "domain": "Arts", "prompt_seed": "How film soundtracks shape emotion, memory, and meaning in storytelling", "complexity": 2},
    {"id": "topic_06", "domain": "Technology", "prompt_seed": "The history of the Apple computer and what made it culturally and commercially influential", "complexity": 2},
    {"id": "topic_07", "domain": "Philosophy", "prompt_seed": "What counts as a fair society, and how should fairness be measured", "complexity": 3},
    {"id": "topic_08", "domain": "Economics", "prompt_seed": "Why inflation feels different across income groups", "complexity": 2},
    {"id": "topic_09", "domain": "Psychology", "prompt_seed": "How habit formation works and why good intentions often fail", "complexity": 2},
    {"id": "topic_10", "domain": "Environment", "prompt_seed": "How cities can adapt to extreme heat without worsening inequality", "complexity": 3},
    {"id": "topic_11", "domain": "Politics", "prompt_seed": "Should voting be compulsory in modern democracies", "complexity": 3},
    {"id": "topic_12", "domain": "Literature", "prompt_seed": "Why retellings of old myths still appeal to modern audiences", "complexity": 2},
    {"id": "topic_13", "domain": "Business", "prompt_seed": "Why some startups scale fast but fail to build durable companies", "complexity": 3},
    {"id": "topic_14", "domain": "Engineering", "prompt_seed": "How design tradeoffs shape everyday products like phones, bikes, and kitchen tools", "complexity": 2},
    {"id": "topic_15", "domain": "Sociology", "prompt_seed": "How social media changes friendship, status, and identity", "complexity": 2},
    {"id": "topic_16", "domain": "Education", "prompt_seed": "What schools should teach that exams usually ignore", "complexity": 2},
    {"id": "topic_17", "domain": "Law", "prompt_seed": "When should privacy rights outweigh public safety concerns", "complexity": 3},
    {"id": "topic_18", "domain": "Health", "prompt_seed": "Why prevention is harder to sustain than treatment in public health systems", "complexity": 3},
    {"id": "topic_19", "domain": "Media", "prompt_seed": "How recommendation algorithms shape taste, attention, and culture", "complexity": 2},
    {"id": "topic_20", "domain": "History", "prompt_seed": "Why some revolutions succeed while others collapse into chaos", "complexity": 3},
    {"id": "topic_21", "domain": "Maths", "prompt_seed": "The invention of zero and how it transformed mathematics and trade", "complexity": 2},
    {"id": "topic_22", "domain": "Science", "prompt_seed": "How uncertainty and error bars improve scientific honesty", "complexity": 3},
    {"id": "topic_23", "domain": "Technology", "prompt_seed": "Should AI tools be allowed in classrooms, and under what rules", "complexity": 3},
    {"id": "topic_24", "domain": "Geography", "prompt_seed": "Why water access shapes politics, migration, and development", "complexity": 3},
    {"id": "topic_25", "domain": "Arts", "prompt_seed": "How architecture influences behavior in schools, offices, and public spaces", "complexity": 2},
    {"id": "topic_26", "domain": "Philosophy", "prompt_seed": "Is progress mainly technological, moral, or both", "complexity": 3},
    {"id": "topic_27", "domain": "Economics", "prompt_seed": "What makes a policy efficient but politically unpopular", "complexity": 3},
    {"id": "topic_28", "domain": "Psychology", "prompt_seed": "Why groups make worse decisions than individuals in some situations", "complexity": 3},
    {"id": "topic_29", "domain": "Environment", "prompt_seed": "Should cities prioritize public transit over private cars in dense areas", "complexity": 2},
    {"id": "topic_30", "domain": "Culture", "prompt_seed": "How language shapes identity, memory, and social belonging", "complexity": 2},
]

THINKING_LENSES: List[Dict[str, Any]] = [
    {"id": "lens_01", "name": "Historical Lens", "focus": "Trace how the topic developed over time and what turning points mattered", "complexity": 1},
    {"id": "lens_02", "name": "Ethical Lens", "focus": "Evaluate what is fair, harmful, justified, or responsible", "complexity": 2},
    {"id": "lens_03", "name": "Economic Lens", "focus": "Analyze incentives, costs, scarcity, and tradeoffs", "complexity": 2},
    {"id": "lens_04", "name": "Scientific Lens", "focus": "Explain mechanisms, evidence quality, and testable claims", "complexity": 2},
    {"id": "lens_05", "name": "Psychological Lens", "focus": "Examine motivation, bias, identity, and behavior", "complexity": 2},
    {"id": "lens_06", "name": "Cultural Lens", "focus": "Study symbols, norms, values, and collective meaning", "complexity": 2},
    {"id": "lens_07", "name": "Political Lens", "focus": "Focus on institutions, power, governance, and policy incentives", "complexity": 3},
    {"id": "lens_08", "name": "Systems Lens", "focus": "Map interdependencies, feedback loops, and unintended consequences", "complexity": 3},
    {"id": "lens_09", "name": "Comparative Lens", "focus": "Compare across places, eras, groups, or models using clear criteria", "complexity": 2},
    {"id": "lens_10", "name": "Future or Foresight Lens", "focus": "Project plausible futures, risks, and strategic choices", "complexity": 3},
    {"id": "lens_11", "name": "Design Lens", "focus": "Examine user needs, constraints, and tradeoffs in how something is built", "complexity": 2},
    {"id": "lens_12", "name": "Legal Lens", "focus": "Interpret rights, duties, liability, and enforcement questions", "complexity": 3},
    {"id": "lens_13", "name": "Environmental Lens", "focus": "Assess ecological impact, sustainability, and externalities", "complexity": 2},
    {"id": "lens_14", "name": "Equity Lens", "focus": "Ask who benefits, who bears the cost, and how outcomes differ by group", "complexity": 3},
    {"id": "lens_15", "name": "Innovation Lens", "focus": "Analyze why ideas spread, stall, or become dominant", "complexity": 2},
    {"id": "lens_16", "name": "Risk Lens", "focus": "Evaluate uncertainty, downside exposure, resilience, and mitigation", "complexity": 3},
    {"id": "lens_17", "name": "Communication Lens", "focus": "Examine framing, rhetoric, messaging, and audience interpretation", "complexity": 2},
    {"id": "lens_18", "name": "Moral Philosophy Lens", "focus": "Use frameworks like utilitarian, duty-based, or virtue ethics reasoning", "complexity": 4},
    {"id": "lens_19", "name": "Data and Measurement Lens", "focus": "Examine what gets measured, what is missed, and how metrics distort behavior", "complexity": 3},
    {"id": "lens_20", "name": "Human Development Lens", "focus": "Assess effects across childhood, adulthood, and aging", "complexity": 2},
    {"id": "lens_21", "name": "Labor Lens", "focus": "Focus on work, skill shifts, bargaining power, and productivity", "complexity": 2},
    {"id": "lens_22", "name": "Globalization Lens", "focus": "Analyze cross-border flows of goods, people, ideas, and power", "complexity": 3},
    {"id": "lens_23", "name": "Historical Counterfactual Lens", "focus": "Test how outcomes might change if one key event or decision differed", "complexity": 4},
    {"id": "lens_24", "name": "Institutional Lens", "focus": "Study how rules and organizations shape behavior over time", "complexity": 3},
    {"id": "lens_25", "name": "Behavioral Economics Lens", "focus": "Combine incentives with bounded rationality and cognitive bias", "complexity": 4},
    {"id": "lens_26", "name": "Narrative Framing Lens", "focus": "Examine who controls the story and how narratives create legitimacy", "complexity": 3},
    {"id": "lens_27", "name": "Technology Stack Lens", "focus": "Break the topic into layers, dependencies, and points of failure", "complexity": 3},
    {"id": "lens_28", "name": "Tradeoff Lens", "focus": "Center the essay on tensions where improving one goal weakens another", "complexity": 2},
    {"id": "lens_29", "name": "Stakeholder Lens", "focus": "Analyze the topic from the perspective of all major affected groups", "complexity": 2},
    {"id": "lens_30", "name": "Civilization Scale Lens", "focus": "Connect the topic to long-run human development and societal trajectory", "complexity": 4},
]

RHETORICAL_BRIEFS: List[Dict[str, Any]] = [
    {"id": "brief_01", "audience": "A smart 14-year-old", "tone": "Clear and accessible", "constraints": ["No jargon", "Use one vivid analogy"], "evidence_rule": "Use one concrete example", "structure_rule": "Start with a simple real-world scene", "complexity": 1},
    {"id": "brief_02", "audience": "General adult reader", "tone": "Neutral explanatory", "constraints": ["Define 2 key terms", "Avoid first person"], "evidence_rule": "Use two everyday examples", "structure_rule": "Use a straightforward introduction-body-conclusion flow", "complexity": 1},
    {"id": "brief_03", "audience": "A skeptical reader", "tone": "Calm and precise", "constraints": ["State your thesis in one sentence", "Include one counterargument"], "evidence_rule": "Use one example and one rebuttal", "structure_rule": "Present claim, objection, response", "complexity": 2},
    {"id": "brief_04", "audience": "A policymaker", "tone": "Formal", "constraints": ["No filler", "End with recommendations"], "evidence_rule": "Use one policy case and one tradeoff", "structure_rule": "Problem, analysis, recommendation", "complexity": 2},
    {"id": "brief_05", "audience": "A business leader", "tone": "Strategic", "constraints": ["Focus on decisions", "No moral grandstanding"], "evidence_rule": "Include cost-benefit reasoning", "structure_rule": "Situation, options, decision", "complexity": 2},
    {"id": "brief_06", "audience": "A university student", "tone": "Academic but readable", "constraints": ["Define scope", "Use signposted paragraphs"], "evidence_rule": "Use two domain examples", "structure_rule": "Thesis, analysis sections, conclusion", "complexity": 2},
    {"id": "brief_07", "audience": "A local community group", "tone": "Practical and respectful", "constraints": ["Use concrete language", "Address concerns directly"], "evidence_rule": "Include one local-style scenario", "structure_rule": "Issue, impact, action steps", "complexity": 1},
    {"id": "brief_08", "audience": "A newspaper opinion page", "tone": "Persuasive", "constraints": ["Strong opening hook", "Memorable closing line"], "evidence_rule": "Include one statistic and one human example", "structure_rule": "Hook, argument, implication", "complexity": 3},
    {"id": "brief_09", "audience": "A classroom teacher", "tone": "Structured and clear", "constraints": ["Explicit topic sentences", "No rhetorical questions"], "evidence_rule": "Use three examples with explanation", "structure_rule": "Five-paragraph essay", "complexity": 1},
    {"id": "brief_10", "audience": "A technical but non-specialist reader", "tone": "Precise and accessible", "constraints": ["Explain one mechanism step by step", "No unexplained acronyms"], "evidence_rule": "Use one technical and one plain-language example", "structure_rule": "Concept, mechanism, implication", "complexity": 2},
    {"id": "brief_11", "audience": "A historian", "tone": "Analytical", "constraints": ["Use chronology carefully", "Avoid presentism"], "evidence_rule": "Use two turning points", "structure_rule": "Background, shift, consequences", "complexity": 3},
    {"id": "brief_12", "audience": "A scientist", "tone": "Evidence-focused", "constraints": ["Separate evidence from interpretation", "Acknowledge uncertainty"], "evidence_rule": "Include one limitation or confound", "structure_rule": "Claim, evidence, limits, implications", "complexity": 3},
    {"id": "brief_13", "audience": "An ethics committee", "tone": "Balanced and rigorous", "constraints": ["Present at least two ethical principles", "Avoid slogans"], "evidence_rule": "Include one edge case", "structure_rule": "Principles, conflict, judgment", "complexity": 3},
    {"id": "brief_14", "audience": "A startup team", "tone": "Action-oriented", "constraints": ["Focus on execution", "Include one failure mode"], "evidence_rule": "Use one market example", "structure_rule": "Opportunity, risk, next steps", "complexity": 2},
    {"id": "brief_15", "audience": "A museum visitor guide", "tone": "Engaging and informative", "constraints": ["Use vivid sensory detail", "Keep sentences varied"], "evidence_rule": "Use one historical anecdote", "structure_rule": "Scene, context, meaning", "complexity": 2},
    {"id": "brief_16", "audience": "A jury of peers", "tone": "Measured and convincing", "constraints": ["Define standards of proof", "Address strongest objection"], "evidence_rule": "Use a chain of reasoning", "structure_rule": "Issue, standards, argument, verdict", "complexity": 3},
    {"id": "brief_17", "audience": "A city council", "tone": "Pragmatic", "constraints": ["Discuss feasibility", "Mention implementation barriers"], "evidence_rule": "Use one budget or resource constraint", "structure_rule": "Need, options, tradeoffs, recommendation", "complexity": 3},
    {"id": "brief_18", "audience": "A peer review panel", "tone": "Critical and fair", "constraints": ["State evaluation criteria first", "Avoid personal attacks"], "evidence_rule": "Evaluate strengths and weaknesses evenly", "structure_rule": "Criteria, assessment, conclusion", "complexity": 3},
    {"id": "brief_19", "audience": "A parent deciding for a family", "tone": "Warm but clear", "constraints": ["Use no jargon", "Include practical consequences"], "evidence_rule": "Use one short scenario and one comparison", "structure_rule": "Decision context, options, recommendation", "complexity": 1},
    {"id": "brief_20", "audience": "A debate club", "tone": "Assertive and structured", "constraints": ["Use clear claims", "Include a rebuttal section"], "evidence_rule": "Use at least two arguments and one rebuttal", "structure_rule": "Resolution, arguments, rebuttal, closing", "complexity": 2},
    {"id": "brief_21", "audience": "A grant committee", "tone": "Serious and outcome-focused", "constraints": ["Define success metrics", "Explain why now"], "evidence_rule": "Use one measurable outcome", "structure_rule": "Need, plan, metrics, impact", "complexity": 3},
    {"id": "brief_22", "audience": "A documentary voiceover script", "tone": "Narrative and cinematic", "constraints": ["Open with a scene", "Use one recurring image"], "evidence_rule": "Include one historical or factual anchor", "structure_rule": "Scene, expansion, reflection", "complexity": 2},
    {"id": "brief_23", "audience": "A skeptical investor", "tone": "Hard-nosed and analytical", "constraints": ["Quantify upside and downside", "State assumptions"], "evidence_rule": "Use one numeric estimate and one risk scenario", "structure_rule": "Thesis, assumptions, risks, decision", "complexity": 4},
    {"id": "brief_24", "audience": "A public health board", "tone": "Evidence-based and cautious", "constraints": ["Distinguish correlation from causation", "Include equity implications"], "evidence_rule": "Use one population-level example", "structure_rule": "Problem, evidence, equity, policy", "complexity": 4},
    {"id": "brief_25", "audience": "A design review meeting", "tone": "Specific and solution-focused", "constraints": ["Prioritize user impact", "Name one design tradeoff"], "evidence_rule": "Use one user journey example", "structure_rule": "User need, options, tradeoff, choice", "complexity": 2},
    {"id": "brief_26", "audience": "A philosophy seminar", "tone": "Rigorous and nuanced", "constraints": ["Define your terms tightly", "Test one objection seriously"], "evidence_rule": "Use one thought experiment", "structure_rule": "Question, framework, objection, resolution", "complexity": 4},
    {"id": "brief_27", "audience": "A cross-functional leadership team", "tone": "Balanced and strategic", "constraints": ["Address technical and human factors", "Include implementation sequencing"], "evidence_rule": "Use one operational and one cultural example", "structure_rule": "Context, tensions, plan, metrics", "complexity": 4},
    {"id": "brief_28", "audience": "A global audience", "tone": "Context-sensitive", "constraints": ["Avoid country-specific assumptions", "Compare at least two regions"], "evidence_rule": "Use two cross-country examples", "structure_rule": "Global pattern, regional differences, synthesis", "complexity": 3},
    {"id": "brief_29", "audience": "A future generation reading an archive", "tone": "Reflective but precise", "constraints": ["Explain present-day assumptions", "State what may age badly"], "evidence_rule": "Use one present example and one long-run implication", "structure_rule": "Present context, hidden assumptions, legacy", "complexity": 4},
    {"id": "brief_30", "audience": "An expert roundtable", "tone": "Dense but organized", "constraints": ["State definitions up front", "Map tradeoffs explicitly"], "evidence_rule": "Use one counterfactual and one failure mode", "structure_rule": "Definitions, analysis, stress test, conclusion", "complexity": 4},
]

DIFFICULTY_PROFILES: Dict[str, Dict[str, Any]] = {
    "beginner": {
        "label": "Beginner",
        "essay_max_complexity": 2,
        "topic_max_complexity": 2,
        "lens_max_complexity": 2,
        "brief_max_complexity": 2,
        "word_count_range": "500 to 700 words",
        "difficulty_rules": [
            "Write a clear thesis or main point in the first paragraph.",
            "Use 2 body paragraphs minimum.",
            "Use simple, concrete examples.",
            "End with a short conclusion that restates the main insight.",
        ],
    },
    "intermediate": {
        "label": "Intermediate",
        "essay_max_complexity": 3,
        "topic_max_complexity": 3,
        "lens_max_complexity": 3,
        "brief_max_complexity": 3,
        "word_count_range": "700 to 950 words",
        "difficulty_rules": [
            "Include one counterargument or alternative interpretation.",
            "Define at least 2 important terms or assumptions.",
            "Use at least 2 examples from different contexts.",
            "Make the transitions between paragraphs explicit.",
        ],
    },
    "advanced": {
        "label": "Advanced",
        "essay_max_complexity": 4,
        "topic_max_complexity": 3,
        "lens_max_complexity": 4,
        "brief_max_complexity": 4,
        "word_count_range": "950 to 1300 words",
        "difficulty_rules": [
            "Include one counterargument and one rebuttal.",
            "Discuss at least one tradeoff and one limitation.",
            "Use evidence or examples from 2 different domains or time periods.",
            "Make your conclusion actionable or decision-oriented.",
        ],
    },
    "god_mode": {
        "label": "God Mode",
        "essay_max_complexity": 4,
        "topic_max_complexity": 3,
        "lens_max_complexity": 4,
        "brief_max_complexity": 4,
        "word_count_range": "1300 to 1800 words",
        "difficulty_rules": [
            "Include a steelman version of the strongest opposing view, then answer it fairly.",
            "Map at least one second-order effect or unintended consequence.",
            "Use one quantitative or quasi-quantitative point, even if estimated.",
            "State what evidence would change your mind.",
            "End with a high-clarity synthesis, not just a summary.",
        ],
    },
}

VALID_DIFFICULTY_ALIASES = {
    "beginner": "beginner",
    "intermediate": "intermediate",
    "advanced": "advanced",
    "god": "god_mode",
    "godmode": "god_mode",
    "god_mode": "god_mode",
    "god mode": "god_mode",
}


def _normalize_difficulty(difficulty: str) -> str:
    key = difficulty.strip().lower()
    key = VALID_DIFFICULTY_ALIASES.get(key, key)
    if key not in DIFFICULTY_PROFILES:
        valid = ", ".join(["beginner", "intermediate", "advanced", "god_mode"])
        raise ValueError(f"Invalid difficulty '{difficulty}'. Valid values: {valid}")
    return key


def _pick_with_complexity_cap(
    items: List[Dict[str, Any]],
    max_complexity: int,
    rng: random.Random,
) -> Dict[str, Any]:
    eligible = [item for item in items if item["complexity"] <= max_complexity]
    if not eligible:
        raise RuntimeError("No eligible items found for the requested complexity cap.")
    return rng.choice(eligible)


def _compose_assignment_prompt(
    difficulty_label: str,
    essay_type: Dict[str, Any],
    topic: Dict[str, Any],
    lens: Dict[str, Any],
    brief: Dict[str, Any],
    profile: Dict[str, Any],
) -> str:
    constraints_text = "; ".join(brief["constraints"])
    difficulty_rules_text = " ".join(profile["difficulty_rules"])

    return (
        f"Write a {essay_type['name'].lower()} essay on the topic '{topic['prompt_seed']}'. "
        f"Use the {lens['name']} to guide your reasoning, which means you should {lens['focus'].lower()}. "
        f"Write for {brief['audience']} in a {brief['tone'].lower()} tone. "
        f"Follow these rhetorical constraints: {constraints_text}. "
        f"Evidence rule: {brief['evidence_rule']}. "
        f"Structure rule: {brief['structure_rule']}. "
        f"Difficulty level: {difficulty_label}. Target length: {profile['word_count_range']}. "
        f"Additional challenge rules: {difficulty_rules_text}"
    )


def get_option_bank() -> Dict[str, Any]:
    return {
        "essay_types_count": len(ESSAY_TYPES),
        "topic_options_count": len(TOPIC_OPTIONS),
        "thinking_lenses_count": len(THINKING_LENSES),
        "rhetorical_briefs_count": len(RHETORICAL_BRIEFS),
        "essay_types": ESSAY_TYPES,
        "topic_options": TOPIC_OPTIONS,
        "thinking_lenses": THINKING_LENSES,
        "rhetorical_briefs": RHETORICAL_BRIEFS,
        "difficulty_profiles": DIFFICULTY_PROFILES,
    }


def propose_essay_assignment(
    difficulty: str,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    normalized = _normalize_difficulty(difficulty)
    profile = DIFFICULTY_PROFILES[normalized]
    rng = random.Random(seed)

    essay_type = _pick_with_complexity_cap(ESSAY_TYPES, profile["essay_max_complexity"], rng)
    topic = _pick_with_complexity_cap(TOPIC_OPTIONS, profile["topic_max_complexity"], rng)
    lens = _pick_with_complexity_cap(THINKING_LENSES, profile["lens_max_complexity"], rng)
    brief = _pick_with_complexity_cap(RHETORICAL_BRIEFS, profile["brief_max_complexity"], rng)

    prompt = _compose_assignment_prompt(profile["label"], essay_type, topic, lens, brief, profile)

    return {
        "difficulty": normalized,
        "difficulty_label": profile["label"],
        "variable_questions": {
            "variable_1": "What kind of essay will you write?",
            "variable_2": "What topic domain and prompt seed will you cover?",
            "variable_3": "What thinking lens will you use?",
            "variable_4": "What rhetorical brief will define the audience and constraints?",
        },
        "variables": {
            "essay_type": {
                "id": essay_type["id"],
                "name": essay_type["name"],
                "purpose": essay_type["purpose"],
            },
            "topic_domain_and_prompt": {
                "id": topic["id"],
                "domain": topic["domain"],
                "prompt_seed": topic["prompt_seed"],
            },
            "thinking_lens": {
                "id": lens["id"],
                "name": lens["name"],
                "focus": lens["focus"],
            },
            "rhetorical_brief": {
                "id": brief["id"],
                "audience": brief["audience"],
                "tone": brief["tone"],
                "constraints": list(brief["constraints"]),
                "evidence_rule": brief["evidence_rule"],
                "structure_rule": brief["structure_rule"],
            },
        },
        "difficulty_rules": list(profile["difficulty_rules"]),
        "target_length": profile["word_count_range"],
        "proposed_question": prompt,
    }


def propose_batch(
    difficulty: str,
    count: int,
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if count <= 0:
        raise ValueError("count must be greater than 0")

    master_rng = random.Random(seed)
    assignments: List[Dict[str, Any]] = []
    for _ in range(count):
        assignments.append(propose_essay_assignment(difficulty=difficulty, seed=master_rng.randint(0, 10**9)))
    return assignments


def get_assignment_by_ids(
    difficulty: str,
    essay_type_id: str,
    topic_id: str,
    lens_id: str,
    brief_id: str,
) -> Dict[str, Any]:
    normalized = _normalize_difficulty(difficulty)
    profile = DIFFICULTY_PROFILES[normalized]

    essay_type = next((x for x in ESSAY_TYPES if x["id"] == essay_type_id), None)
    topic = next((x for x in TOPIC_OPTIONS if x["id"] == topic_id), None)
    lens = next((x for x in THINKING_LENSES if x["id"] == lens_id), None)
    brief = next((x for x in RHETORICAL_BRIEFS if x["id"] == brief_id), None)

    if essay_type is None:
        raise ValueError(f"Unknown essay_type_id: {essay_type_id}")
    if topic is None:
        raise ValueError(f"Unknown topic_id: {topic_id}")
    if lens is None:
        raise ValueError(f"Unknown lens_id: {lens_id}")
    if brief is None:
        raise ValueError(f"Unknown brief_id: {brief_id}")

    prompt = _compose_assignment_prompt(profile["label"], essay_type, topic, lens, brief, profile)

    return {
        "difficulty": normalized,
        "difficulty_label": profile["label"],
        "variables": {
            "essay_type": {
                "id": essay_type["id"],
                "name": essay_type["name"],
                "purpose": essay_type["purpose"],
            },
            "topic_domain_and_prompt": {
                "id": topic["id"],
                "domain": topic["domain"],
                "prompt_seed": topic["prompt_seed"],
            },
            "thinking_lens": {
                "id": lens["id"],
                "name": lens["name"],
                "focus": lens["focus"],
            },
            "rhetorical_brief": {
                "id": brief["id"],
                "audience": brief["audience"],
                "tone": brief["tone"],
                "constraints": list(brief["constraints"]),
                "evidence_rule": brief["evidence_rule"],
                "structure_rule": brief["structure_rule"],
            },
        },
        "difficulty_rules": list(profile["difficulty_rules"]),
        "target_length": profile["word_count_range"],
        "proposed_question": prompt,
    }
