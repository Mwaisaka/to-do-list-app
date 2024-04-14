import React, { useState } from "react";
import TodoItem from './TodoItem';

function TodoList() {

    const [tasks, setTasks] = useState([
        {
            id: 1,
            text: "Doctor's appointment",
            completed: true
        },
        {
            id: 2,
            text: "Meeting at School",
            completed: false
        },
        {
            id: 3,
            text: "Playing Golf",
            completed: false
        },
        {
            id: 4,
            text: "Go shopping",
            completed: false
        },
    ]);

    const [text, setText] = useState('');

    function addTask(text) {
        const newTask = {
            id: Date.now(),
            text,
            completed: false
        };
        setTasks([...tasks, newTask]);
        setText('');
    }

    function deleteTask(id) {
        setTasks(tasks.filter(task => task.id !== id))
    }

    function toggleCompleted(id) {
        setTasks(tasks.map(task => {
            if (task.id === id) {
                return { ...task, completed: !task.completed }
            } else {
                return task;
            }
        }));
    }
    return (

        <div classname="todo-list">
            
                {tasks.map(task => (
                    <TodoItem
                        key={task.id}
                        task={task}
                        deleteTask={deleteTask}
                        toggleCompleted={toggleCompleted}
                    />
                ))}
                
                <input
                    value={text}
                    placeholder="Enter task name here..."
                    onChange={e => setText(e.target.value)}
                />
                <button onClick={() => addTask(text)}>Add New Task</button>
            

        </div>
    );
}

export default TodoList;