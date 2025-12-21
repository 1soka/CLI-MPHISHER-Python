# 🎣 Mphisher Pro Elite Edition
Version 1.0.0 | Educational Security Tool
A multi-platform educational phishing tool with elegant CLI interface and automatic ngrok tunneling.

<img width="532" height="428" alt="Image" src="https://github.com/user-attachments/assets/6e84e828-b551-4825-8a3f-f0f2afa37417" />

⚠️ Warning
```
┌─────────────────────────────────────────────────────────┐
│  ⚡ FOR EDUCATIONAL PURPOSES ONLY ⚡                   │
│                                                         │
│  Using this tool for malicious activities is ILLEGAL.   │
│  The author disclaims all responsibility for misuse.    │
│                                                         │
│  Use only in a legal context with explicit permission.  │
└─────────────────────────────────────────────────────────┘
```
✨ Features

🎨 Colorful CLI interface with Rich
🌐 12 ready-to-use phishing templates
🔒 Automatic ngrok tunneling
📊 Real-time data capture
💾 Automatic save to phish.txt
🎯 Victim IP capture
🚀 Instant deployment

<img width="714" height="593" alt="{12ACBF20-E13A-44E7-8713-C00E234A0596}" src="https://github.com/user-attachments/assets/db266ce0-6198-4f29-aa85-a8cc64180812" />


🛠️ Installation
Prerequisites

Python 3.7+
Ngrok account (free)

Steps
bash# Clone the repository
```
git clone https://github.com/Blackholeisoka/mphisher.git
cd mphisher
```
# Install dependencies
```
pip install rich flask pyngrok python-dotenv
```
# Configure ngrok token
```
nano .env
.env file:
NGROK_TOKEN=your_ngrok_token_here
```
Get an ngrok token:

Create an account on ngrok.com
Copy your authtoken from the dashboard
Paste it in .env


🚀 Usage
bashpython index.py
Workflow
```
┌─────────────────────────────────────────────────────────┐
│ 1. Select a platform (01-12)                            │
│ 2. Server starts automatically                          │
│ 3. Ngrok URL generated → https://xxxx.ngrok.io          │
│ 4. Send URL to target (educational context)             │
│ 5. Captured data displays in real-time                  │
│ 6. Automatic save to phish.txt                          │
└─────────────────────────────────────────────────────────┘
```

📁 Project Structure
```
mphisher/
├── index.py              # Main script
├── .env                  # Ngrok configuration
├── phish.txt            # Captured data
└── site/
    ├── facebook/
    │   ├── index.html
    │   ├── index.js     # Submission logic
    │   ├── css/
    │   │   └── styles.css
    │   ├── js/
    │   │   ├── toggleEyeIcon.js
    │   │   └── changeBackgroundImage.js
    │   └── images/
    ├── instagram/
    ├── snapchat/
    └── ...
```

🔧 Flask Endpoints
RouteMethodDescription/GETPhishing page/<path>GETStatic resources/userPOSTData reception

📊 Captured Data Format
```
=== NEW ENTRY ===
IP address: 192.168.1.100
email: victim@example.com
password: ********
```

<img width="891" height="476" alt="{8D578FB0-4798-460A-90D7-0DEE06798C4B}" src="https://github.com/user-attachments/assets/f650c1cf-fc71-44c7-a789-48c5b9e61802" />


🎨 Customization
Add a New Platform

Create folder:
```
bashmkdir -p site/new_platform/{css,js,images}
```
Add files:
index.html - Page template
index.js - Submission logic
css/styles.css - Styles

🐛 Troubleshooting
404 Error on Resources

Check paths in index.html
Use css/styles.css instead of ./css/styles.css

Ngrok Won't Connect
bash# Verify token
```
cat .env
```

# Test manually
ngrok http 5000
Port 5000 Already in Use
python# Modify in index.py line 128
PORT = 8080  # Instead of 5000

🤝 Contributing
Contributions are welcome!
```
bash# Fork → Clone → Branch → Commit → Push → PR
git checkout -b feature/new-feature
```

<img width="615" height="618" alt="{051E4CB8-6264-44AB-B9E4-A50423D81A33}" src="https://github.com/user-attachments/assets/f01fb0c1-b867-4f0b-be36-6527b691954b" />


📜 License
MIT License - see LICENSE
