"""Constants for te_quiz package including question mappings and keys."""

# Communication style questions (10 total)
# Questions 1, 3, 5, 7, 11: a=extrovert, b=introvert
EXTROVERT_INTROVERT_QUESTIONS = {1, 3, 5, 7, 11}

# Questions 9, 10, 12, 13, 14: a=thinker, b=feeler
THINKER_FEELER_QUESTIONS = {9, 10, 12, 13, 14}

# All communication style questions
COMMUNICATION_STYLE_QUESTIONS = (
    EXTROVERT_INTROVERT_QUESTIONS | THINKER_FEELER_QUESTIONS
)

# SD (Self-Deceptive positivity) questions (4 total)
# Questions 2, 4, 6, 8: Likert scale a-e with reverse scoring
SD_QUESTIONS = {2, 4, 6, 8}

# All valid question IDs
ALL_QUESTIONS = COMMUNICATION_STYLE_QUESTIONS | SD_QUESTIONS

# Valid answers for communication style questions
VALID_COMMUNICATION_ANSWERS = {'a', 'b'}

# Valid answers for SD questions (Likert scale)
# a=Strongly Disagree, b=Disagree, c=Neutral, d=Agree, e=Strongly Agree
VALID_SD_ANSWERS = {'a', 'b', 'c', 'd', 'e'}

# Reverse scoring mapping for SD questions
# Original: a=1, b=2, c=3, d=4, e=5 -> Reversed: a=5, b=4, c=3, d=2, e=1
REVERSE_SCORE_MAPPING = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}

# SD level thresholds
SD_THRESHOLDS = {
    'low': 3.5,
    'moderate': 4.5
}
