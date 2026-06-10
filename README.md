# 📧 Hacker News Email Scraper & Sender

A Python automation project that scrapes the latest **Hacker News top stories** and sends them directly to your email using SMTP.

---

## 🚀 Features

- Scrapes real-time top stories from Hacker News
- Extracts news using BeautifulSoup
- Formats data into a clean HTML email
- Sends automated emails via Gmail SMTP
- Secure credential handling using `.env`
- Timestamped email subject

---

## 🧠 Project Architecture

- **requests** → Fetches webpage data (HTTP GET)
- **BeautifulSoup (bs4)** → Parses and extracts news titles
- **smtplib** → Handles email sending via SMTP
- **email.mime** → Builds HTML email body
- **datetime** → Adds timestamp to emails
- **dotenv** → Loads secure environment variables

---

## 📦 Installation

Install required dependencies:

```bash
pip install requests beautifulsoup4 lxml python-dotenv