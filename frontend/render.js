const list = document.getElementById("task-list");

export function renderTask(task) {
  list.innerHTML += `<li>${task.title}</li>`;
}

export function saveSession(token) {
  localStorage.setItem("adminToken", token);
}
