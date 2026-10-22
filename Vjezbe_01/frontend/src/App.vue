<script setup>
import { ref, computed } from "vue";

const newTask = ref("");

const tasks = ref([
  { id: 1, title: "Izraditi dizajn stranice", done: true },
  { id: 2, title: "Dodati navigaciju", done: true },
  { id: 3, title: "Povezati API", done: false },
  { id: 4, title: "Testirati aplikaciju", done: false },
]);

const completed = computed(
  () => tasks.value.filter((task) => task.done).length,
);

function addTask() {
  const title = newTask.value.trim();

  if (!title) return;

  tasks.value.push({
    id: Date.now(),
    title,
    done: false,
  });

  newTask.value = "";
}

function deleteTask(id) {
  tasks.value = tasks.value.filter((task) => task.id !== id);
}
</script>

<template>
  <div class="app">
    <header class="navbar">
      <a class="logo" href="#">✦ TaskFlow</a>
      <span class="tag">Vue 3 aplikacija</span>
    </header>

    <main class="container">
      <section class="hero">
        <span class="eyebrow">TVOJ OSOBNI PLANER</span>
        <h1>Organiziraj svoj dan.</h1>
        <p>Prati zadatke, ostani fokusiran i ostvari svoje ciljeve.</p>
      </section>

      <section class="stats">
        <article class="stat-card">
          <span>Ukupno zadataka</span>
          <strong>{{ tasks.length }}</strong>
        </article>

        <article class="stat-card">
          <span>Završeno</span>
          <strong>{{ completed }}</strong>
        </article>

        <article class="stat-card">
          <span>Preostalo</span>
          <strong>{{ tasks.length - completed }}</strong>
        </article>
      </section>

      <section class="task-panel">
        <div class="panel-heading">
          <div>
            <h2>Moji zadaci</h2>
            <p>Upravljaj svojim dnevnim obavezama.</p>
          </div>
          <span class="counter">{{ completed }}/{{ tasks.length }}</span>
        </div>

        <form class="task-form" @submit.prevent="addTask">
          <input
            v-model="newTask"
            type="text"
            placeholder="Unesi novi zadatak..."
            aria-label="Novi zadatak"
          />
          <button type="submit">+ Dodaj</button>
        </form>

        <div v-if="tasks.length" class="task-list">
          <article v-for="task in tasks" :key="task.id" class="task-item">
            <label class="task-label">
              <input v-model="task.done" type="checkbox" />
              <span :class="{ completed: task.done }">
                {{ task.title }}
              </span>
            </label>

            <button
              class="delete-btn"
              type="button"
              aria-label="Obriši zadatak"
              @click="deleteTask(task.id)"
            >
              ×
            </button>
          </article>
        </div>

        <p v-else class="empty-state">
          Nema zadataka. Dodaj svoj prvi zadatak!
        </p>

        <div class="progress-section">
          <div class="progress-label">
            <span>Napredak</span>
            <strong>
              {{
                tasks.length ? Math.round((completed / tasks.length) * 100) : 0
              }}%
            </strong>
          </div>
          <div class="progress-track">
            <div
              class="progress-fill"
              :style="{
                width:
                  (tasks.length ? (completed / tasks.length) * 100 : 0) + '%',
              }"
            ></div>
          </div>
        </div>
      </section>

      <footer>Izrađeno s Vue.js 3 · Jednostavno i učinkovito.</footer>
    </main>
  </div>
</template>

<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap");

:root {
  font-family: "Inter", sans-serif;
  color: #1e293b;
  background: #f8fafc;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  min-width: 320px;
}

button,
input {
  font: inherit;
}

.navbar {
  height: 76px;
  padding: 0 max(6%, calc((100% - 1080px) / 2));
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: white;
  border-bottom: 1px solid #e2e8f0;
}

.logo {
  font-size: 22px;
  font-weight: 800;
  color: #4f46e5;
  text-decoration: none;
}

.tag,
.counter {
  background: #eef2ff;
  color: #4f46e5;
  border-radius: 20px;
  padding: 8px 12px;
  font-size: 12px;
  font-weight: 600;
}

.container {
  max-width: 920px;
  margin: auto;
  padding: 56px 24px 24px;
}

.hero {
  margin-bottom: 32px;
}

.eyebrow {
  color: #6366f1;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 2px;
}

h1 {
  font-size: clamp(30px, 5vw, 46px);
  letter-spacing: -1.8px;
  margin: 14px 0;
}

.hero p,
.panel-heading p {
  color: #64748b;
  line-height: 1.7;
}

.stats {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}

.stat-card,
.task-panel {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 22px;
}

.stat-card span {
  display: block;
  font-size: 13px;
  color: #64748b;
}

.stat-card strong {
  display: block;
  font-size: 30px;
  margin-top: 12px;
}

.task-panel {
  padding: 28px;
  box-shadow: 0 10px 35px #0f172a08;
}

.panel-heading {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
}

.panel-heading h2 {
  margin: 0;
  font-size: 21px;
}

.panel-heading p {
  margin-bottom: 0;
  font-size: 13px;
}

.task-form {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.task-form input {
  flex: 1;
  min-width: 0;
  padding: 13px 14px;
  border: 1px solid #cbd5e1;
  border-radius: 9px;
  outline: none;
}

.task-form input:focus {
  border-color: #6366f1;
  box-shadow: 0 0 0 3px #6366f120;
}

.task-form button {
  padding: 12px 18px;
  color: white;
  background: #4f46e5;
  border: 0;
  border-radius: 9px;
  cursor: pointer;
  font-weight: 600;
}

.task-item {
  min-height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  border-bottom: 1px solid #f1f5f9;
}

.task-label {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  overflow-wrap: anywhere;
}

.task-label input {
  accent-color: #4f46e5;
  width: 17px;
  height: 17px;
  flex-shrink: 0;
}

.completed {
  color: #94a3b8;
  text-decoration: line-through;
}

.delete-btn {
  background: transparent;
  border: 0;
  color: #94a3b8;
  font-size: 24px;
  cursor: pointer;
}

.delete-btn:hover {
  color: #dc2626;
}

.empty-state {
  color: #64748b;
  padding: 20px 0;
  text-align: center;
}

.progress-section {
  margin-top: 26px;
}

.progress-label {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
  margin-bottom: 10px;
}

.progress-track {
  height: 8px;
  border-radius: 20px;
  overflow: hidden;
  background: #e2e8f0;
}

.progress-fill {
  height: 100%;
  background: #6366f1;
  border-radius: inherit;
  transition: width 0.25s ease;
}

footer {
  text-align: center;
  color: #94a3b8;
  font-size: 12px;
  padding: 32px 0 12px;
}

@media (max-width: 600px) {
  .container {
    padding: 36px 16px 20px;
  }

  .stats {
    gap: 8px;
  }

  .stat-card {
    padding: 14px 10px;
  }

  .stat-card span {
    font-size: 11px;
  }

  .stat-card strong {
    font-size: 25px;
  }

  .task-panel {
    padding: 18px;
  }

  .task-form {
    flex-wrap: wrap;
  }

  .task-form input {
    width: 100%;
    flex-basis: 100%;
  }
}
</style>
