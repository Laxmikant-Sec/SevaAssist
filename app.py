from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from difflib import SequenceMatcher
from urllib.parse import urlparse, parse_qs
from html import escape
with open("knowledge_base.json", "r", encoding="utf-8") as file:
    knowledge_data = json.load(file)

knowledge_base = knowledge_data["knowledge_base"]

def get_subject(question):
    words = question.casefold().split()

    if any(word.strip("?.!,") in ("volunteer", "volunteers") for word in words):
        return "volunteer"

    if any(word.strip("?.!,") in ("teacher", "teachers") for word in words):
        return "teacher"

    return None


def find_answer(user_question):
    question = user_question.strip().casefold()
    
    user_subject = get_subject(question)
 

    best_score = 0.0
    best_entry = None


    for entry in knowledge_base:
    
        approved_questions = [entry["question"]] + entry.get("alternative_questions", [])
    

    
        for approved_question in approved_questions:

            approved_subject = get_subject(approved_question)
            if user_subject != approved_subject and (user_subject is not None or approved_subject is not None):
                continue

    
            score = SequenceMatcher(None, question, approved_question.casefold()).ratio()

            if score > best_score:
                best_score = score
                best_entry = entry


            if question == approved_question.casefold():
                return {
                "answer": entry["answer"],
                "source": entry["source"]
            }

    
    if best_entry is not None and best_score >= 0.80:
       return {
          "answer": best_entry["answer"],
        "source": best_entry["source"]
       }

    return {
        "answer": "I couldn't find an approved answer to that question.",
        "source": "No matching source found"
    }
class SevaAssistHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_parameters = parse_qs(parsed_url.query)
        user_question = query_parameters.get("question", [""])[0]
        if user_question.strip():
            result = find_answer(user_question)
        else:
            result = None
        answer_html = ""

        if result is not None:
            safe_answer = escape(result["answer"])
            safe_source = escape(result["source"])

            answer_html = f"""
            <section>
                <h2>SevaAssist Answer</h2>
                <p>{safe_answer}</p>
                <p><strong>Source:</strong> {safe_source}</p>
            </section>
            """
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>SevaAssist</title>
     
<style>
    body {{
        font-family: Arial, sans-serif;
        background-color: #f4f7fb;
        color: #243247;
        max-width: 900px;
        margin: 40px auto;
        padding: 24px;
        line-height: 1.6;
    }}

    h1 {{
        color: #176b85;
        font-size: 36px;
    }}

    h2 {{
        color: #176b85;
    }}

input[type="text"] {{
    width: 70%;
    padding: 14px;
    font-size: 16px;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    box-sizing: border-box;
}}

button {{
    background-color: #176b85;
    color: white;
    padding: 14px 22px;
    font-size: 16px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
}}

button:hover {{
    background-color: #10546a;
}}

section {{
    background-color: #ffffff;
    padding: 24px;
    margin-top: 30px;
    border-radius: 12px;
    border-left: 5px solid #176b85;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}}

    </style>
       
        </head>
        <body>
            <h1>Welcome to SevaAssist</h1>
            <p>Secure Knowledge Assistant for Volunteers and Teachers</p>
            <p>Our application is running successfully!</p>
<h2>Ask SevaAssist</h2>

<form action="/" method="GET">
    <label for="question">Enter your question:</label>
    <br><br>
    <input
        type="text"
        id="question"
        name="question"
        placeholder="Type your question here..."

        value="{escape(user_question, quote=True)}"

        size="50"
        maxlength="200"
        required
    >
    <button type="submit">Ask Question</button>
</form>

{answer_html}

        </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8501), SevaAssistHandler)
    print("SevaAssist running at http://127.0.0.1:8501")
    server.serve_forever()