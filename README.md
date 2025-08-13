# Text Readability Score Analyzer

A comprehensive Python tool for analyzing text readability using multiple established readability indices. This project implements three different readability formulas to assess how easy or difficult a text is to read and understand.

## 📋 Features

- **Multiple Readability Indices**: Implements three widely-used readability formulas:
  - Automated Readability Index (ARI)
  - Flesch-Kincaid Readability Test
  - Dale-Chall Readability Index

- **Comprehensive Text Analysis**: Analyzes various text metrics including:
  - Character count (excluding whitespace and newlines)
  - Word count using advanced tokenization
  - Sentence count using NLTK sentence tokenization
  - Syllable count using pyphen hyphenation
  - Difficult words identification using Longman Communication 3000 wordlist

- **Age-Based Readability Assessment**: Provides age recommendations for text comprehension
- **Average Readability Score**: Calculates an overall average age recommendation across all indices

## 🚀 Quick Start

### Prerequisites

Make sure you have Python 3.6+ installed on your system.

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd readability-score-analyzer
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
pip install pyphen  # Additional dependency for syllable counting
```

3. Download NLTK data (if not already installed):
```python
import nltk
nltk.download('punkt')
```

### Usage

Run the readability analyzer from the command line:

```bash
python "Readability Score (Python)/task/readability/readability.py" <text_file.txt> <longman_words.txt>
```

**Example:**
```bash
python "Readability Score (Python)/task/readability/readability.py" "Readability Score (Python)/task/readability/test_file.txt" "Readability Score (Python)/task/readability/longman_words.txt"
```

### Sample Output

```
Text: A book is a set of printed sheets of paper held together between two covers...

Characters: 550
Sentences: 8
Words: 97
Difficult Words: 12
Syllables: 134

Automated Readability Index: 7 (about the 11-12 year olds).
Flesch–Kincaid Readability Test: 8 (about the 12-13 year olds).
Dale-Chall Readability Index: 6. The text can be understood by 10-11 year olds.

This text should be understood in average by 11.5 year olds.
```

## 📊 Readability Indices Explained

### 1. Automated Readability Index (ARI)
- **Formula**: `4.71 × (characters/words) + 0.5 × (words/sentences) - 21.43`
- **Focus**: Character-based measurement, useful for texts with varying word lengths
- **Age Mapping**: Scores 1-14+ correspond to ages 5-6 through 18-22

### 2. Flesch-Kincaid Readability Test
- **Formula**: `0.39 × (words/sentences) + 11.8 × (syllables/words) - 15.59`
- **Focus**: Syllable-based measurement, widely used in education
- **Age Mapping**: Same as ARI (1-14+ → ages 5-6 through 18-22)

### 3. Dale-Chall Readability Index
- **Formula**: `0.1579 × (difficult_words/words × 100) + 0.0496 × (words/sentences)`
- **Additional**: +3.6365 if difficult words > 5% of total words
- **Focus**: Vocabulary difficulty using the Dale-Chall word list
- **Age Mapping**: Same as other indices

## 📁 Project Structure

```
readability-score-analyzer/
├── Readability Score (Python)/
│   └── task/
│       └── readability/
│           ├── readability.py          # Main analysis script
│           ├── test_file.txt           # Sample text for testing
│           ├── longman_words.txt       # Longman Communication 3000 wordlist
│           └── file_path_verification.py
├── requirements.txt                     # Project dependencies
├── LICENSE                             # MIT License
└── README.md                           # This file
```

**Note**: This repository is configured to only track the core readability analysis files. All other course materials and auxiliary files are git-ignored to keep the repository focused on the essential readability functionality.

## 🔧 Technical Details

### Dependencies
- **nltk**: Natural Language Toolkit for text processing and tokenization
- **pyphen**: Hyphenation library for accurate syllable counting
- **argparse**: Command-line argument parsing (built-in)
- **re**: Regular expressions for pattern matching (built-in)
- **math**: Mathematical operations (built-in)

### Text Processing Pipeline
1. **Input Validation**: Validates command-line arguments for file paths
2. **Text Extraction**: Reads and processes input text file
3. **Tokenization**: Uses NLTK for sentence and word tokenization
4. **Metrics Calculation**: Computes characters, words, sentences, syllables, and difficult words
5. **Score Calculation**: Applies three readability formulas
6. **Age Mapping**: Converts scores to age recommendations
7. **Average Calculation**: Provides overall readability assessment

### Word Difficulty Assessment
The tool uses the Longman Communication 3000 wordlist to identify difficult words. Words not present in this list are considered "difficult" and factor into the Dale-Chall Readability Index calculation.

## 🎯 Use Cases

- **Educational Content**: Assess reading level appropriateness for different age groups
- **Content Writing**: Optimize content readability for target audiences
- **Academic Research**: Analyze text complexity in research papers
- **Publishing**: Ensure manuscripts meet readability standards
- **Web Content**: Optimize website content for better user engagement

## 🧪 Testing

The project includes test files for validation:
- `test_file.txt`: Sample text about books for testing functionality
- Various test cases in the `test/` directory

Run tests using:
```bash
python "Readability Score (Python)/task/tests.py"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 References

- [Automated Readability Index](https://en.wikipedia.org/wiki/Automated_readability_index)
- [Flesch-Kincaid Readability Tests](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests)
- [Dale-Chall Readability Formula](https://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formula)
- [Longman Communication 3000](https://www.longmandictionaries.com/about/longman-communication-3000)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Created as part of a Hyperskill AI Engineer Bootcamp 2025 course project focusing on text analysis and readability assessment.

---

**Note**: This tool is designed for educational and research purposes. Readability scores should be used as guidelines rather than absolute measures, as text comprehension can vary based on reader experience, context, and subject matter familiarity.