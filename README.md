
# SevaAssist

**Secure Knowledge Assistant for Volunteers and Teachers**

Art of Living Hackathon 2026 | Prototype

## Overview

SevaAssist is a Python-based knowledge assistant designed to help volunteers and teachers find information from a curated knowledge base.

The prototype prioritizes source transparency, predictable answers, and responsible handling of unsupported questions.

## The Problem

Volunteers and teachers may need quick answers about event registration, onboarding, training resources, and responsibilities.

Information can be difficult to locate, and conventional chatbots may provide answers without reliable supporting sources.

## Our Solution

SevaAssist retrieves answers from a predefined JSON knowledge base and displays the associated source.

The application uses question matching to recognize supported wording variations while applying safeguards to reduce incorrect matches.

## Features

- Browser-based question-and-answer interface
- Python HTTP server
- JSON knowledge base
- Exact and alternative-question matching
- Similarity matching using Python's SequenceMatcher
- Subject checks for volunteer and teacher questions
- Source-labelled answers
- Safe fallback when no suitable answer is found
- Input and output HTML escaping

## Technology

- Python
- HTML and CSS
- JSON
- Python standard libraries

No external AI API is required.

## Running Locally

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python app.py
```

5. Open:

http://127.0.0.1:8501

## Demonstration Questions

Try these questions:

- How can I become a volunteer?
- How do I volunteer?
- What do volunteers do?
- What is expected of a volunteer?
- Where can I find training materials?

For a safety demonstration, ask:

- What is expected of a teacher?
- What is the office Wi-Fi password?

The prototype should decline questions without an approved matching answer.

## Responsible Use and Limitations

**All current knowledge-base entries are fictional demonstration examples, not official Art of Living policies or documentation.**

SevaAssist uses text similarity rather than full natural-language understanding. Its safeguards reduce some incorrect matches but do not guarantee accuracy.

The prototype is intended for local demonstration. It does not currently provide authentication, authorization, encrypted transport, or production-grade access controls.

Real deployment would require approved source documents, stronger validation, appropriate access controls, and comprehensive security testing.

## Future Improvements

- Administrator-managed approved documents
- Improved matching and ambiguity detection
- Authentication and role-based access
- Audit logging
- Expanded volunteer and teacher knowledge
- Accessible user interface improvements
- Automated tests

## Project Author

Laxmikant Sharma

GitHub: https://github.com/Laxmikant-Sec

Cybersecurity Portfolio: https://lscyber.ca

## Disclaimer

This is an independent hackathon prototype. It is not an official Art of Living application and is not endorsed by the organization.
