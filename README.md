
# Product JSON Creator 🛍️📦

A simple Python-based JSON extractor that uses generative AI to convert structured product description data (e.g., CSV) into well-formatted JSON. The project includes a Streamlit interface for interactive use. 

---

## 🚀 Overview

**Product JSON Creator** is a tool designed to help you generate structured JSON for product data **automatically** using an AI model. It’s especially useful for preparing product catalogs, ecommerce feeds, or demo datasets from raw input descriptions like CSV files. 
---

## 📋 Features

✔ Generate structured JSON from product descriptions  
✔ Works with a CSV dataset  
✔ Simple Python script and Streamlit UI included  
✔ Easy to extend for new fields or formats 

---

## 🧰 Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| UI (optional) | Streamlit |
| AI Backend | Generative API (configured in code) |
| Data Input | CSV |

---

## 🛠️ Getting Started

### 📌 Prerequisites

Make sure you have Python (3.12) installed.

### 🔧 Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/sisira214/product_json_creator.git
   cd product_json_creator
````

2. **Create & activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your AI key**

   * Add your API key or credentials to the script/config as needed.

---

## 💡 How to Use

### 🧪 From Python

Run the extractor script:

```bash
python grok_json.py
```

The script reads `products.csv`, processes product descriptions, and generates a structured JSON output.

### 📊 With Streamlit UI

For an interactive interface:

```bash
streamlit run json_streamlit.py
```

This will launch a browser UI where you can upload a product CSV and view the generated JSON.

---

## 📦 Example Output

Here’s a simple example of generated product JSON format:

```json
[
  {
    "id": "001",
    "name": "Red T-Shirt",
    "price": "15.99",
    "description": "Comfortable cotton tee",
    "category": "Apparel"
  },
  ...
]
```

---

## 🧠 Customization

You can extend the JSON schema by modifying the parsing logic in `grok_json.py`, adding new fields, and improving prompts used for the AI generation.

---

## 📁 Project Structure

```
product_json_creator/
├── .gitignore
├── LICENSE
├── README.md
├── grok_json.py            # Core JSON extraction logic
├── json_streamlit.py       # Streamlit interactive UI
├── products.csv            # Sample input data
└── requirements.txt.txt    # Python dependencies
```

---

## 🤝 Contributing

Contributions are welcome! You can:

* Improve JSON schema handling
* Add support for more input formats
* Enhance the UI/UX of the Streamlit app

Please open issues or pull requests on GitHub.

---

## 📜 License

This project is licensed under the **MIT License** — see the `LICENSE` file for details. 



