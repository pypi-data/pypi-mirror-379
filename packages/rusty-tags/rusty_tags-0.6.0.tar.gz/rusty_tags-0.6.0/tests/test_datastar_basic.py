#!/usr/bin/env python3
"""
Basic tests for RustyTags Datastar integration
"""

import rusty_tags
from rusty_tags import Div, Button, Input, Form, H1

def test_basic_datastar_attributes():
    """Test basic ds_* attribute processing"""
    print("=== Basic Datastar Attribute Tests ===\n")
    
    # Test ds_signals
    button1 = Button("Click me", ds_signals={"count": 0})
    print("Button with ds_signals:")
    print(str(button1))
    print()
    
    # Test ds_on_click
    button2 = Button("Click me", ds_on_click="$count += 1")
    print("Button with ds_on_click:")
    print(str(button2))
    print()
    
    # Test ds_text
    div1 = Div(ds_text="'Count: ' + $count")
    print("Div with ds_text:")
    print(str(div1))
    print()

def test_reactive_class_binding():
    """Test reactive class binding"""
    print("=== Reactive Class Binding Tests ===\n")
    
    # Static class
    div1 = Div("Static", cls="container mx-auto")
    print("Static class:")
    print(str(div1))
    print()
    
    # Reactive class
    div2 = Div("Reactive", cls={"active": "$isActive", "disabled": "$isDisabled"})
    print("Reactive class:")
    print(str(div2))
    print()

def test_event_modifiers():
    """Test event modifiers and timing"""
    print("=== Event Modifier Tests ===\n")
    
    # Test debounce
    input1 = Input(
        type="text",
        ds_on_input__debounce_500ms="$query = this.value"
    )
    print("Input with debounce modifier:")
    print(str(input1))
    print()
    
    # Test throttle
    button3 = Button(
        "Submit",
        ds_on_click__throttle_2000ms="@post('/api/submit')"
    )
    print("Button with throttle modifier:")
    print(str(button3))
    print()

def test_complex_datastar_example():
    """Test a more complex example with multiple Datastar features"""
    print("=== Complex Datastar Example ===\n")
    
    form = Form(
        H1("User Registration", ds_text="'Registration - ' + $currentTime"),
        
        Input(
            type="email",
            placeholder="Email",
            ds_bind="user.email",
            ds_on_input__debounce_500ms="@get('/api/validate-email', {email: $user.email})"
        ),
        
        Input(
            type="password",
            placeholder="Password", 
            ds_bind="user.password",
            ds_show="$user.email.length > 0"
        ),
        
        Button(
            "Register",
            ds_on_click="@post('/api/register', $user)",
            ds_show="$user.email && $user.password",
            ds_cls={"btn-loading": "$submitting"}
        ),
        
        ds_signals={
            "user": {"email": "", "password": ""},
            "currentTime": "new Date().toLocaleTimeString()",
            "submitting": False
        },
        ds_cls={"form-loading": "$submitting"}
    )
    
    print("Complex registration form:")
    print(str(form))
    print()

def test_javascript_expressions():
    """Test JavaScript expression detection"""
    print("=== JavaScript Expression Detection Tests ===\n")
    
    # Test various expression patterns
    div1 = Div("Counter", ds_text="$count")
    print("Simple signal reference:")
    print(str(div1))
    print()
    
    div2 = Div("Expression", ds_text="$count > 0 ? 'Positive' : 'Zero or negative'")
    print("Complex expression:")
    print(str(div2))
    print()
    
    div3 = Div("Date", ds_text="new Date().toISOString()")
    print("JavaScript constructor:")
    print(str(div3))
    print()

if __name__ == "__main__":
    print("Testing RustyTags Datastar Integration\n")
    
    try:
        test_basic_datastar_attributes()
        test_reactive_class_binding()
        test_event_modifiers()
        test_javascript_expressions()
        test_complex_datastar_example()
        
        print("✅ All tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()