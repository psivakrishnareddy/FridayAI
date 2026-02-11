## FridayAI

**FridayAI** is an Artificial Digital Assistant developed using Deep Neural Networks.

Welcome to the FridayAI Wiki.

#### NOTE 2026: 
This was my Bachelor's final year project and my passion project inspired by Jarvis. I built a Neural network that will understand my intent and processes the request
with a beautiful live animation indicating thinking,talking and listening etc and a sleep mode for fun.

This was build in 2020 which works kind of similar to how agents call tools in a loop. My agent keeps listening for instructions and based on the intent classification after 
Speech to text -> NLP Tokenization -> DNN ->  intent -> Tool Calling. This is very similar to LLM agents but the most early version of it kind off. 

---

## Feature Highlights

### 📧 Mail Management

* Sends emails using the SMTP protocol
* Reads the user’s top 5 unread emails via Google Gmail API

### 📰 News Updates

* Fetches latest and trending news using News API

### 📅 Calendar Events

* Retrieves user calendar information for any requested date with super flexible natural language like "What events do I know for next month or today or this week etc?"
* Supports flexible natural language date queries (day, week, month, etc.) using logical pattern matching
* create events for user using natural language on google calendar.

### 🌐 Information Gathering

* Fetches information using Wikipedia or Google
* Can read out search results and optionally open them in a browser
* Supports voice-based Wikipedia and Google search

### 🖥 Application Automation

* Opens and controls user applications via voice using PyAutomation
* Supports actions such as:

  * Open/close applications
  * Browser tab management, like changing tabs and text input
  * Play, pause, and control media volume
  * Take screenshots or make quick notes.
  * Shutdown, log off, or turn off the assistant

### 🌍 Web Automation

* Performs basic web automation using Selenium integrated with voice commands like search something on youtube

### 🌦 Weather Information

* Retrieves weather details for any location using OpenWeather API
* Extracts location directly from voice commands

### ⏰ Quick Reminders & Notes

* Creates quick reminders
* Stores short notes via voice command
* Can randomly ask to type something if the cursor is at input.

### 🔐 Face Authentication

* Uses OpenCV-based facial recognition to activate the assistant

### 🎙 Wake Trigger

* Always-on wake word detection for instant activation

### 🏠 Home Automation (Future enhancement)

* Uses PyFirmata with Arduino for IoT-based home automation via voice control

### 🔋 System Monitor

* Monitors system status and battery level
* Notifies user when charging is recommended

### 🎲 Bored User Feature

* Suggests random activities when the user is idle ,tells a joke or plays a random game.

### 💬 General Conversations

* Conversational AI powered by a Deep Learning model

### 🖼 Tkinter UI

* Compact graphical interface displaying:

  * User commands
  * Assistant responses
  * AI actions
  * Visual orb animation

---

![Python](https://img.shields.io/badge/Python-3.x-blue)
![AI](https://img.shields.io/badge/AI-Deep%20Learning-purple)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Desktop-lightgrey)
![UI](https://img.shields.io/badge/UI-Tkinter-orange)
![Automation](https://img.shields.io/badge/Automation-Voice%20Controlled-blueviolet)
![API](https://img.shields.io/badge/APIs-Gmail%20%7C%20News%20%7C%20Weather-informational)

## Video

[![Watch the video](https://img.youtube.com/vi/bzIWpOiLYDg/3.jpg)](https://www.youtube.com/watch?v=bzIWpOiLYDg)
