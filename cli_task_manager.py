#!/usr/bin/env python3
"""
CLI Task Manager for AI-Powered Calendar Assistant
Simple command-line interface to manage tasks
"""

import requests
import json
from datetime import datetime, timedelta
import argparse

API_BASE_URL = "http://localhost:8000"

def add_task():
    """Interactive task creation"""
    print("\n📝 Add New Task")
    print("-" * 30)
    
    user_id = int(input("User ID: ") or "1")
    title = input("Task Title: ")
    
    print("\nPriority options: high, medium, low")
    priority = input("Priority (medium): ") or "medium"
    
    duration = int(input("Duration in minutes (60): ") or "60")
    
    print("\nDeadline (YYYY-MM-DD HH:MM or leave empty for tomorrow):")
    deadline_input = input("Deadline: ").strip()
    
    if not deadline_input:
        deadline = (datetime.now() + timedelta(days=1)).replace(hour=17, minute=0, second=0, microsecond=0)
    else:
        try:
            if len(deadline_input) == 10:  # Just date
                deadline = datetime.strptime(deadline_input, "%Y-%m-%d").replace(hour=17, minute=0)
            else:  # Date and time
                deadline = datetime.strptime(deadline_input, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date format. Using tomorrow 5 PM.")
            deadline = (datetime.now() + timedelta(days=1)).replace(hour=17, minute=0, second=0, microsecond=0)
    
    print("\nTask type options: focus, admin, flex")
    task_type = input("Type (focus): ") or "focus"
    
    task_data = {
        "user_id": user_id,
        "title": title,
        "priority": priority,
        "duration": duration,
        "deadline": deadline.isoformat(),
        "type": task_type
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/add-task", json=task_data)
        if response.status_code == 200:
            task = response.json()
            print(f"\n✅ Task created successfully! ID: {task['id']}")
        else:
            print(f"❌ Error creating task: {response.text}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure the server is running.")

def list_tasks():
    """List all tasks for a user"""
    user_id = int(input("User ID (1): ") or "1")
    
    try:
        response = requests.get(f"{API_BASE_URL}/get-tasks/{user_id}")
        if response.status_code == 200:
            tasks = response.json()
            if not tasks:
                print(f"\nNo tasks found for user {user_id}")
                return
                
            print(f"\n📋 Tasks for User {user_id}")
            print("-" * 50)
            for task in tasks:
                status = "✅" if task['completed'] else "⏳"
                deadline = datetime.fromisoformat(task['deadline']).strftime("%Y-%m-%d %H:%M")
                print(f"{status} [{task['id']}] {task['title']}")
                print(f"    Priority: {task['priority']} | Duration: {task['duration']}min | Deadline: {deadline}")
                print(f"    Type: {task['type']}")
                print()
        else:
            print(f"❌ Error fetching tasks: {response.text}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure the server is running.")

def complete_task():
    """Mark a task as completed"""
    task_id = int(input("Task ID to complete: "))
    
    try:
        response = requests.patch(f"{API_BASE_URL}/complete-task/{task_id}")
        if response.status_code == 200:
            task = response.json()
            print(f"✅ Task '{task['title']}' marked as completed!")
        else:
            print(f"❌ Error: {response.text}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure the server is running.")

def delete_task():
    """Delete a task"""
    task_id = int(input("Task ID to delete: "))
    
    confirm = input(f"Are you sure you want to delete task {task_id}? (y/N): ")
    if confirm.lower() != 'y':
        print("Cancelled.")
        return
    
    try:
        response = requests.delete(f"{API_BASE_URL}/delete-task/{task_id}")
        if response.status_code == 200:
            print("✅ Task deleted successfully!")
        else:
            print(f"❌ Error: {response.text}")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure the server is running.")

def main():
    print("🤖 AI-Powered Calendar Assistant - Task Manager")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Add new task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
