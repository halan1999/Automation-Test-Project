import pytest, re
from playwright.sync_api import Page, expect

# Happy case: add a valid task
@pytest.mark.only_browser("chromium")
def test_add_todo_success(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/")
    page.fill("input.new-todo", "Learn Playwright")
    page.keyboard.press("Enter")
    expect(page.locator(".todo-list li label")).to_have_text("Learn Playwright")
    page.screenshot(path="screenshot_add_todo_success.png")


# Unhappy case: try to add an empty task
@pytest.mark.only_browser("chromium")
def test_add_empty_todo(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/")
    page.press("input.new-todo", "Enter")
    # Verify that no task was added
    expect(page.locator(".todo-list li")).to_have_count(0)
    page.screenshot(path="screenshot_add_empty_todo.png")


# Happy case: add multiple tasks and verify their count
@pytest.mark.only_browser("chromium")
def test_add_multiple_todos(page: Page):
    tasks = ["Task A", "Task B", "Task C"]
    page.goto("https://demo.playwright.dev/todomvc/")
    for task in tasks:
        page.fill("input.new-todo", task)
        page.keyboard.press("Enter")
    # Verify that all tasks are added
    expect(page.locator(".todo-list li")).to_have_count(len(tasks))
    page.screenshot(path="screenshot_add_multiple_todos.png")


# Mark a task as completed
@pytest.mark.only_browser("chromium")
def test_mark_task_completed(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/")
    page.fill("input.new-todo", "Complete this task")
    page.keyboard.press("Enter")
    # Click the checkbox to mark as completed
    page.locator(".todo-list li .toggle").click()
    # Verify task has completed class
    expect(page.locator(".todo-list li")).to_have_class(re.compile("completed"))
    page.screenshot(path="screenshot_mark_task_completed.png")


# Delete a task
@pytest.mark.only_browser("chromium")
def test_delete_task(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/")
    page.fill("input.new-todo", "Delete this task")
    page.keyboard.press("Enter")
    # Hover to show the delete button and click it
    page.hover(".todo-list li")
    page.click(".todo-list li .destroy")
    # Verify the list is empty
    expect(page.locator(".todo-list li")).to_have_count(0)
    page.screenshot(path="screenshot_delete_task.png")


# Filter completed tasks
@pytest.mark.only_browser("chromium")
def test_filter_completed_tasks(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/")
    page.fill("input.new-todo", "Task to complete")
    page.keyboard.press("Enter")
    page.locator(".todo-list li .toggle").click()  # Mark as completed
    # Click on "Completed" filter
    page.click("text=Completed")
    # Verify that only 1 completed task is shown
    expect(page.locator(".todo-list li")).to_have_count(1)
    expect(page.locator(".todo-list li")).to_have_class(re.compile("completed"))
    page.screenshot(path="screenshot_filter_completed_tasks.png")

