# 🧠 Keyword Extraction Script

This script processes user-submitted questions from a CSV file and extracts up to 4 meaningful keywords per question. It removes common conversational words, stopwords, and number words to clean the data for further use (e.g., chatbot training, analysis).

---

## 📂 File Structure

```
project-folder/
├── keyword_extraction.py         # Main script for keyword extraction
├── README.md                     # Project documentation
├── input/
│   └── initial_data.csv          # Original questions (update the filename as needed)
└── output/
    └── processed_data.csv        # Processed file with extracted keywords
```

---

## 🚀 Features

- Tokenizes each question using NLTK
- Filters out:
  - Stopwords (`the`, `is`, `at`, etc.)
  - Conversational filler words (`hi`, `thanks`, etc.)
  - Number words (`one`, `two`, etc.)
- Outputs top 4 keywords into new columns:
  - `context2`, `context3`, `context4`, `context5`

---

## 💻 Requirements

Install the required packages:

```bash
pip install pandas nltk
```

Also, download necessary NLTK resources (only once):

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## 🧾 Input Format

Input CSV should contain at least one column:

```
question
"What are the health benefits of honey?"
"Tell me more about beeswax usage."
...
```

---

## 🛠️ How to Use

1. Update the input and output file paths in the script:
   ```python
   file_path = 'your/input/file/path.csv'
   file_path2 = 'your/output/file/path.csv'
   ```

2. Run the script:

   ```bash
   python keyword_extraction.py
   ```

3. Output CSV will include the original data plus 4 keyword columns.

---

## ✅ Example Output

| question                                | context2 | context3 | context4 | context5 |
|-----------------------------------------|----------|----------|----------|----------|
| What are the health benefits of honey?  | health   | benefits | honey    |          |
| Tell me more about beeswax usage.       | beeswax  | usage    |          |          |

---

## 📬 Contact

Created by Plilian – Contributions welcome!
