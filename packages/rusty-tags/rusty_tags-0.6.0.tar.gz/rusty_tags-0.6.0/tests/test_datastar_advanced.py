#!/usr/bin/env python3
"""
Advanced tests for RustyTags Datastar integration with Python API
"""

import rusty_tags
from rusty_tags import Div, Button, Input, Form, H1, H2, Ul, Li
from rusty_tags.datastar import DS, signals, reactive_class

def test_ds_action_generators():
    """Test DS action generator methods"""
    print("=== DS Action Generator Tests ===\n")
    
    # Test GET action
    button1 = Button("Load Data", ds_on_click=DS.get("/api/data", target="#content"))
    print("GET action:")
    print(str(button1))
    print()
    
    # Test POST action with data
    button2 = Button("Submit", ds_on_click=DS.post("/api/submit", data="$user"))
    print("POST action with signal data:")
    print(str(button2))
    print()
    
    # Test POST with dictionary data
    button3 = Button("Create", ds_on_click=DS.post("/api/create", data={"type": "user"}))
    print("POST action with dict data:")
    print(str(button3))
    print()

def test_signal_manipulation():
    """Test signal manipulation helpers"""
    print("=== Signal Manipulation Tests ===\n")
    
    # Test signal setters
    button1 = Button("Set Name", ds_on_click=DS.set("user.name", "John"))
    print("Set signal:")
    print(str(button1))
    print()
    
    # Test toggle
    button2 = Button("Toggle Active", ds_on_click=DS.toggle("isActive"))
    print("Toggle signal:")
    print(str(button2))
    print()
    
    # Test increment
    button3 = Button("Increment", ds_on_click=DS.increment("count"))
    print("Increment signal:")
    print(str(button3))
    print()
    
    # Test chain multiple actions
    button4 = Button("Complex Action", 
                    ds_on_click=DS.chain(
                        DS.set("loading", True),
                        DS.post("/api/process"),
                        DS.set("loading", False)
                    ))
    print("Chained actions:")
    print(str(button4))
    print()

def test_convenience_functions():
    """Test convenience functions"""
    print("=== Convenience Function Tests ===\n")
    
    # Test signals function
    form = Form(
        H1("Dashboard"),
        ds_signals=signals(
            count=0,
            user={"name": "", "email": ""},
            isLoading=False
        )
    )
    print("Signals convenience:")
    print(str(form))
    print()
    
    # Test reactive_class function
    div = Div("Status", cls=reactive_class(
        active="$isActive",
        loading="$isLoading",
        disabled="$count === 0"
    ))
    print("Reactive class convenience:")
    print(str(div))
    print()

def test_real_world_example():
    """Test a real-world interactive dashboard"""
    print("=== Real-world Interactive Dashboard ===\n")
    
    dashboard = Div(
        H1("User Management Dashboard", ds_text="'Dashboard - ' + $stats.totalUsers + ' users'"),
        
        # Search section
        Div(
            H2("Search Users"),
            Input(
                type="text",
                placeholder="Search by name or email...",
                ds_bind="search.query",
                ds_on_input__debounce_300ms=DS.chain(
                    DS.set("search.loading", True),
                    DS.get("/api/users/search", query="$search.query"),
                    DS.set("search.loading", False)
                )
            ),
            cls="search-section",
            ds_cls=reactive_class(loading="$search.loading")
        ),
        
        # Action buttons
        Div(
            Button(
                "Add User",
                ds_on_click=DS.chain(
                    DS.set("modal.visible", True), 
                    DS.set("modal.mode", "create")
                ),
                cls="btn-primary"
            ),
            Button(
                "Refresh",
                ds_on_click=DS.chain(
                    DS.set("isRefreshing", True),
                    DS.get("/api/users"),
                    DS.set("isRefreshing", False)
                ),
                ds_cls=reactive_class(loading="$isRefreshing")
            ),
            Button(
                "Export CSV",
                ds_on_click=DS.get("/api/users/export", format="csv"),
                ds_show="$stats.totalUsers > 0"
            ),
            cls="action-buttons"
        ),
        
        # User list
        Div(
            H2("Users", ds_text="'Users (' + $stats.totalUsers + ')'"),
            Div(
                "Loading users...",
                ds_show="$isLoading",
                cls="loading-spinner"
            ),
            Div(
                "No users found",
                ds_show="!$isLoading && $users.length === 0",
                cls="empty-state"
            ),
            # User items would be dynamically populated by Datastar
            cls="user-list"
        ),
        
        # Global signals for the entire dashboard
        ds_signals=signals(
            users=[],
            search={"query": "", "loading": False},
            stats={"totalUsers": 0},
            modal={"visible": False, "mode": "create"},
            isLoading=True,
            isRefreshing=False
        ),
        
        cls="dashboard",
        ds_cls=reactive_class(
            loading="$isLoading",
            refreshing="$isRefreshing"
        ),
        
        # Load initial data when dashboard mounts
        ds_on_load=DS.chain(
            DS.get("/api/users"),
            DS.get("/api/stats"),
            DS.set("isLoading", False)
        )
    )
    
    print("Interactive dashboard:")
    print(str(dashboard))
    print()

def test_conditional_actions():
    """Test conditional action patterns"""
    print("=== Conditional Action Patterns ===\n")
    
    # Conditional button
    button = Button(
        "Save Changes",
        ds_on_click=DS.conditional(
            "$form.isValid",
            DS.chain(
                DS.set("saving", True),
                DS.post("/api/save", data="$form"),
                DS.set("saving", False)
            ),
            DS.set("showErrors", True)
        ),
        ds_cls=reactive_class(
            disabled="!$form.isValid || $saving",
            loading="$saving"
        )
    )
    print("Conditional save button:")
    print(str(button))
    print()

def test_list_operations():
    """Test list/array manipulation"""
    print("=== List Operation Tests ===\n")
    
    todo_list = Div(
        H2("Todo List"),
        Input(
            type="text",
            placeholder="Add new todo...",
            ds_bind="newTodo",
            ds_on_keydown__enter=DS.chain(
                DS.append("todos", "$newTodo"),
                DS.set("newTodo", "")
            )
        ),
        Button(
            "Add Todo",
            ds_on_click=DS.chain(
                DS.append("todos", "$newTodo"),
                DS.set("newTodo", "")
            ),
            ds_show="$newTodo.length > 0"
        ),
        Button(
            "Clear Completed",
            ds_on_click="$todos = $todos.filter(todo => !todo.completed)",
            ds_show="$todos.some(todo => todo.completed)"
        ),
        ds_signals=signals(
            todos=[],
            newTodo=""
        ),
        cls="todo-app"
    )
    
    print("Todo list with array operations:")
    print(str(todo_list))
    print()

if __name__ == "__main__":
    print("Testing RustyTags Advanced Datastar Integration\n")
    
    try:
        test_ds_action_generators()
        test_signal_manipulation()
        test_convenience_functions()
        test_conditional_actions()
        test_list_operations()
        test_real_world_example()
        
        print("✅ All advanced tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()