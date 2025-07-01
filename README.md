# 🔍 Pathfinder Visualizer (BFS, DFS, DLS) – Flask Web App

This project is a **Flask-based web visualizer** for graph pathfinding algorithms like **BFS**, **DFS**, and **DLS**.  
It includes two modes:

- ✅ **Auto-Generate Graph** — Randomly generate a graph & visualize the search
- ✅ **Manual-Generate Graph** — Let users build the graph manually (via Tkinter or planned frontend UI)

---

## 🌐 Features

- 📊 Visualizes **BFS**, **DFS**, and **DLS** step-by-step
- 🎨 Beautiful front-end using **HTML**, **CSS**, and **Bootstrap**
- 🔄 Dynamic interaction with the **Python (Flask) backend**
- ⚙️ Integration with `autogenrate.py` logic to display:
  - Nodes
  - Edges
  - Traversal steps
  - Final path
- 📁 Organized and scalable **Flask project structure**
- ✅ Future support for **manual graph generation** via `megenrate.py`

---

## 🖱️ Usage Instructions

1. **Launch the application**
2. Navigate to the **Visualizer** page
3. Click the **Auto-Generate** button

You will see:
- Nodes & edges of the generated graph
- BFS traversal steps (Enqueue, Dequeue)
- The final path found from source to destination

> 🔧 Manual generation (`megenrate.py`) is under development and will allow users to draw their own graphs.

---

## 🛠️ Future Improvements

- [ ] 🧠 Draw actual graph using **D3.js** or **vis.js** in-browser
- [ ] 🖱️ Add a **user-controlled graph builder** UI on the frontend
- [ ] 🌐 Deploy to **Render**, **Vercel**, or **Netlify** (with a backend-compatible service)
- [ ] 🎞️ Add **animations**, edge highlighting, and traversal arrows

---

## 📌 Project Structure

