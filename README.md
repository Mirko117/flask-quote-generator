# Flask Quote Generator

This is a simple Flask application that generates images with random quotes.

## Installation

Clone the repository:

```bash
git clone https://github.com/Mirko117/flask-quote-generator
cd flask-quote-generator
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Setting Up Environment Variables

Before running the application, you need to set up the required environment variables. 

On Windows, you can use the `set` command:

```bash
set PIXABAY_API_KEY="[Your API Key]"
set FLASK_SECRET_KEY='[SomeRandomString]'
```

On Unix-based systems like Linux and macOS, use the export command:
```bash
export PIXABAY_API_KEY="[Your API Key]"
export FLASK_SECRET_KEY='[SomeRandomString]'
```

## Usage
Start the server:
```bash
python main.py
```
Navigate to http://localhost:5000 in your web browser to view the application.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

