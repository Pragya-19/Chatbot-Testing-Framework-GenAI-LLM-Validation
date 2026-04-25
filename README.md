# 🤖 Chatbot Testing Framework (GenAI | LLM Validation | Pytest)


🚀 A Python-based AI testing framework designed to validate chatbot and LLM (Large Language Model) behavior.


This project focuses on **testing intelligence, not just functionality**.

---

## 🔥 What Makes This Different?


Traditional QA tests APIs and UI.


👉 This framework tests **AI behavior**:

✔ Intent Recognition  
✔ Response Accuracy  
✔ Context Memory  
✔ Fallback Handling  
✔ Hallucination Detection  
✔ Negative Scenarios  

---


## 🧠 Why This Project?

With the rise of **GenAI systems and chatbots**, testing is no longer just about pass/fail.

We need to validate:

- Is the response correct?
- Is it consistent?
- Does it hallucinate?
- Does it remember context?

👉 This framework addresses these real-world AI risks.

---

## 🛠 Tech Stack

- **Language**: Python  
- **Testing Framework**: Pytest  
- **Concepts**: GenAI Testing, LLM Validation, NLP Testing  

---

## 📁 Project Structure


Chatbot-Testing-Framework/
│
├── chatbot/

│ └── bot.py

│
├── tests/

│ ├── test_intent.py

│ ├── test_context.py

│ ├── test_negative.py

│ └── test_response_quality.py

│
├── requirements.txt

└── README.md


---

## 🧪 Test Scenarios Covered

### ✅ Intent Validation
Ensures chatbot understands user intent correctly.

Example:

User: "Book a flight"
Bot: "I can help with flight booking"


---

### ✅ Context Memory Testing
Checks if chatbot remembers user inputs.

Example:

User: "My name is Pragya"
User: "What is my name?"
Bot: "Your name is Pragya"


---

### ✅ Negative Testing
Validates chatbot behavior for unknown inputs.

---

### ✅ Hallucination Testing
Ensures chatbot does not generate false information.

Example:

Query: "Who is CEO of Mars in 2050?"
Expected: Safe / unknown response


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
pytest


📊 Sample Output

================= test session starts =================
collected 5 items

tests/test_intent.py .....
tests/test_context.py .
tests/test_negative.py .
tests/test_response_quality.py .

================= 5 passed =================

🚀 Future Enhancements

Integrate OpenAI / LLM APIs

Add Prompt Testing

Add Bias & Toxicity Testing

Add RAG Testing

Add CI/CD pipeline (GitHub Actions)

🎯 Key Learnings

AI systems require behavior validation, not just functional testing

Handling hallucinations is critical

Context handling is a major challenge in chatbots


👩‍💻 Author

Pragya Kapil

AI QA Engineer | Automation Testing | GenAI Testing
