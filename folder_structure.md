flask_expense_app/
│
├── app.py # The main Flask app
├── config.py # Configuration settings for the app
├── routes/
│ ├── **init**.py # Blueprint registration
│ ├── upload_routes.py # Routes related to uploading PDFs
│ └── categorize_routes.py # Routes related to categorization
├── services/
│ ├── **init**.py # Service package initializer
│ ├── pdf_service.py # PDF extraction and parsing logic
│ └── chart_service.py # Future chart rendering logic (optional)
├── templates/
│ ├── upload.html # Template for uploading the PDF
│ ├── categorize.html # Template for categorizing transactions
│ └── layout.html # Common layout template
├── uploads/ # Directory for uploaded PDFs
└── static/ # Static assets (CSS, JS, etc.)
