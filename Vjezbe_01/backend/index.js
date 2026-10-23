import express from "express";
import cors from "cors";

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// Privremena pohrana podataka
let nextId = 3;

let tasks = [
  { id: 1, title: "Izraditi dizajn stranice", done: true },
  { id: 2, title: "Povezati API", done: false },
];

// Početna ruta
app.get("/", (req, res) => {
  res.json({
    message: "TaskFlow REST API radi!",
    version: "1.0.0",
  });
});

// GET /api/tasks - Dohvati sve zadatke
app.get("/api/tasks", (req, res) => {
  res.json(tasks);
});

// GET /api/tasks/:id - Dohvati jedan zadatak
app.get("/api/tasks/:id", (req, res) => {
  const task = tasks.find((task) => task.id === Number(req.params.id));

  if (!task) {
    return res.status(404).json({
      error: "Zadatak nije pronađen.",
    });
  }

  res.json(task);
});

// POST /api/tasks - Kreiraj novi zadatak
app.post("/api/tasks", (req, res) => {
  const title = req.body?.title;

  if (typeof title !== "string" || !title.trim()) {
    return res.status(400).json({
      error: "Naslov zadatka je obavezan.",
    });
  }

  const task = {
    id: nextId++,
    title: title.trim(),
    done: false,
  };

  tasks.push(task);

  res.status(201).json(task);
});

// PATCH /api/tasks/:id - Ažuriraj zadatak
app.patch("/api/tasks/:id", (req, res) => {
  const task = tasks.find((task) => task.id === Number(req.params.id));

  if (!task) {
    return res.status(404).json({
      error: "Zadatak nije pronađen.",
    });
  }

  const { title, done } = req.body ?? {};

  if (title !== undefined && (typeof title !== "string" || !title.trim())) {
    return res.status(400).json({
      error: "Naslov mora biti neprazan tekst.",
    });
  }

  if (done !== undefined && typeof done !== "boolean") {
    return res.status(400).json({
      error: "Polje done mora biti boolean.",
    });
  }

  if (title !== undefined) task.title = title.trim();
  if (done !== undefined) task.done = done;

  res.json(task);
});

// DELETE /api/tasks/:id - Obriši zadatak
app.delete("/api/tasks/:id", (req, res) => {
  const index = tasks.findIndex((task) => task.id === Number(req.params.id));

  if (index === -1) {
    return res.status(404).json({
      error: "Zadatak nije pronađen.",
    });
  }

  tasks.splice(index, 1);

  res.status(204).end();
});

// Obrada nepostojećih ruta
app.use((req, res) => {
  res.status(404).json({
    error: "Ruta nije pronađena.",
  });
});

// Pokretanje poslužitelja
app.listen(PORT, () => {
  console.log(`REST API radi na http://localhost:${PORT}`);
});
