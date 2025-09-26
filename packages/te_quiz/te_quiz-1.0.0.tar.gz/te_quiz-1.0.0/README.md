# te_quiz

A Python package for evaluating quiz results to determine communication styles, self-deceptive positivity levels, and stress journey mapping.

## Features

- **Communication Style Analysis**: Calculates percentages for four communication styles (Red, Yellow, Blue, Green)
- **Self-Deceptive Positivity Detection**: Evaluates authenticity levels (Low, Moderate, High)
- **Stress Journey Mapping**: Maps stress levels 1-10 to dominant communication colors based on percentages
- **Flexible Input**: Handles questions in any order
- **Simple API**: Single function interface


## Installation

```bash
pip install te_quiz
```

## Quick Start

```python
from te_quiz import evaluate_quiz

# Define quiz answers (questions can be in any order)
answers = {
    1: 'a',  # Communication style questions use 'a' or 'b'
    2: 'c',  # SD questions use letters 'a'-'e'
    3: 'b',
    4: 'b',
    5: 'a',
    6: 'd',
    7: 'b',
    8: 'a',
    9: 'a',
    10: 'b',
    11: 'a',
    12: 'a',
    13: 'a',
    14: 'b'
}

# Evaluate the quiz
result = evaluate_quiz(answers)

print(result)
# Output:
# {
#     'communication_style': {
#         'red': 0.35,
#         'yellow': 0.25,
#         'blue': 0.25,
#         'green': 0.15
#     },
#     'sd_level': 'moderate',
#     'stress_journey': {
#         1: 'red', 2: 'red', 3: 'red', 4: 'red',
#         5: 'yellow', 6: 'yellow', 7: 'blue',
#         8: 'blue', 9: 'green', 10: 'green'
#     }
# }
```

## API Reference

### `evaluate_quiz(answers: Dict[int, str]) -> Dict`

Evaluates complete quiz results.

**Parameters:**
- `answers`: Dictionary mapping question IDs (1-14) to answers

**Returns:**
- Dictionary with:
  - `communication_style`: Color percentages (red, yellow, blue, green)
  - `sd_level`: Self-deceptive positivity level string
  - `stress_journey`: Mapping of stress levels (1-10) to colors

**Raises:**
- `InvalidQuestionError`: Missing or invalid question IDs
- `InvalidAnswerError`: Invalid answer format

## License

Not to be distributed.