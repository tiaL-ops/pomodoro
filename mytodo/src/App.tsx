import React, { useState, useEffect } from "react";
import "./App.css";

// Define the Task type
interface Task {
  Description: string;
  Status: "Open" | "Done";
}

const App: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [taskDescription, setTaskDescription] = useState<string>("");

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    const response = await fetch("http://127.0.0.1:5000/tasks");
    const data = await response.json();
    setTasks(data);
  };

  const addTask = async () => {
    if (taskDescription.trim()) {
      await fetch("http://127.0.0.1:5000/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description: taskDescription }),
      });
      setTaskDescription("");
      fetchTasks();
    }
  };

  const markTaskDone = async (index: number) => {
    await fetch(`http://127.0.0.1:5000/tasks/${index}`, {
      method: "PUT",
    });
    fetchTasks();
  };

  const removeTask = async (index: number) => {
    await fetch(`http://127.0.0.1:5000/tasks/${index}`, {
      method: "DELETE",
    });
    fetchTasks();
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>MyTodo</h1>
        <div>
          <input
            type="text"
            value={taskDescription}
            onChange={(e) => setTaskDescription(e.target.value)}
            placeholder="Enter a task"
          />
          <button onClick={addTask}>Add Task</button>
        </div>
        <ul>
          {tasks.map((task, index) => (
            <li key={index}>
              {task.Description} - {task.Status}
              {task.Status === "Open" && (
                <button onClick={() => markTaskDone(index)}>Mark Done</button>
              )}
              <button onClick={() => removeTask(index)}>Remove</button>
            </li>
          ))}
        </ul>
      </header>
    </div>
  );
};

export default App;
