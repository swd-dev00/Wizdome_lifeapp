# 🧠 Wizdome_Lifeapp  
*A guardian for children with cerebral palsy (CP) and complex care needs.*

---

## 🌍 Overview  

**Wizdome_Lifeapp** is an AI-assisted companion platform designed to support children living with **cerebral palsy (CP)**, particularly those with **ostomy or medical monitoring needs**, by combining wearable data, intelligent alerts, and caregiver assistance in one integrated system.

The project merges **compassionate caregiving** with **applied AI**, helping families monitor health, manage routines, and respond early to distress signs — all while ensuring privacy, regulatory compliance, and usability for children and caregivers.

This repository contains the **working MVP (minimum viable product)** codebase and outlines the broader vision described in [Wizdome Comp.pdf](./Wizdome%20Comp.pdf).

---

## ⚙️ Core Modules  

| Module | Description |
|--------|--------------|
| `memory.py` | Encrypted local storage and retrieval of all system data (vitals, alerts, battery states). |
| `vitals_monitor.py` | Simulates or reads vital signs (heart rate, motion, step count, bag weight) for periodic logging. |
| `battery_manager.py` | Tracks power levels of multiple devices (tablet, wearables) and triggers low-battery alerts. |
| `scheduler.py` | Issues regular care or maintenance reminders (e.g., ostomy bag changes). |
| `distress_detection.py` | Detects anomalous or distress situations with probability-based triggers. |
| `ai_companion.py` | Empathetic conversational module providing encouragement or safety prompts based on vitals. |
| `alert_system.py` | Central hub for all alerts, aggregating memory logs and generating console or external notifications. |
| `config.py` | Placeholder for thresholds and configurable parameters. |
| `utils.py` | Utilities placeholder for future shared helpers. |

---

## 🧩 System Architecture  

Below is a simplified diagram of component interaction:

```mermaid
flowchart TD
    A[Vitals Monitor] -->|logs vitals| M[Memory]
    B[Battery Manager] -->|updates battery level| M
    C[Scheduler] -->|adds scheduled alerts| M
    D[Distress Detection] -->|detects distress| M
    E[AI Companion] -->|reads vitals to respond| M
    M -->|new alerts| F[Alert System]
    F -->|prints or sends notifications| U((User))
