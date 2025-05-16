# 🧬 Matrix Terminal Rain Effect

A beautiful **Matrix-style digital rain** animation for your terminal, written in pure Python using `colorama` and ANSI cursor control. Fully customizable and mesmerizing to watch.

---

## 🌌 Features

- 🌧️ Real-time "digital rain" animation
- 🎨 Bright green/white character streams (Matrix-like)
- 🖥️ Adapts to terminal width and height
- 🌀 Smooth falling motion with randomized characters
- ⌨️ Press `Ctrl+C` to gracefully exit

---

## 📦 Requirements

Install `colorama` if not already installed:

```bash
pip install colorama
```

---

## 🚀 How to Run

```bash
python matrix.py
```

⚠️ Works best in a Windows Command Prompt or PowerShell window (uses `os.system("color 0a")`).

---

## ⚙️ Configuration

Inside the script, you can adjust:

```python
cols = 200  # Width of terminal (in characters)
rows = 80   # Height of terminal (in lines)
```

And customize the character set:

```python
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&*()"
```

---

## 🧠 How It Works

- Each column gets a random "drop" position
- White characters represent the head of the stream
- Green characters form the tail
- ANSI escape codes via `colorama` and `Cursor.POS` move the cursor precisely
- Graceful exit on `Ctrl+C` resets terminal color and clears screen

---

## ❗ Notes

- Designed for Windows terminals
- Will clear your screen and change terminal color during execution
- You can tweak sleep time (`time.sleep(0.05)`) for faster or slower animation
