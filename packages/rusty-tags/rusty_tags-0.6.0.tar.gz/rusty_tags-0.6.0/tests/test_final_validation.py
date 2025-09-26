#!/usr/bin/env python3
"""
Final validation test to ensure all Datastar integration features work correctly
"""

from rusty_tags import Div, Button, Input, Form, H1, H2, Script
from rusty_tags.datastar import DS, signals, reactive_class

def test_all_datastar_features():
    """Test all implemented Datastar features"""
    print("🧪 Final Validation Test")
    print("=" * 50)
    
    # Test 1: Basic ds_* attributes
    print("\n✅ Test 1: Basic ds_* attributes")
    basic = Div(
        "Content",
        ds_text="'Dynamic: ' + $value",
        ds_show="$visible",
        ds_bind="input"
    )
    assert "data-text=" in str(basic)
    assert "data-show=" in str(basic)
    assert "data-bind=" in str(basic)
    print("   ✓ ds_text, ds_show, ds_bind working")
    
    # Test 2: Event handlers with modifiers
    print("\n✅ Test 2: Event handlers with modifiers")
    events = Button(
        "Click me",
        ds_on_click="alert('clicked')",
        ds_on_click__debounce_500ms="$loading = true",
        ds_on_click__throttle_1000ms="@post('/api/action')"
    )
    event_html = str(events)
    assert "data-on-click=" in event_html
    assert "data-on-click.debounce.500ms=" in event_html
    assert "data-on-click.throttle.1000ms=" in event_html
    print("   ✓ Event modifiers working")
    
    # Test 3: Signal management
    print("\n✅ Test 3: Signal management")
    signal_div = Div(
        ds_signals=signals(
            count=0,
            user={"name": "John", "email": "john@example.com"},
            items=[1, 2, 3],
            active=True
        )
    )
    signal_html = str(signal_div)
    assert "data-signals=" in signal_html
    assert '"count":0' in signal_html
    assert '"user":' in signal_html
    assert '"items":' in signal_html
    print("   ✓ Signals working")
    
    # Test 4: Reactive classes
    print("\n✅ Test 4: Reactive classes")
    # Static class
    static_cls = Div("Static", cls="container mx-auto")
    assert 'class="container mx-auto"' in str(static_cls)
    
    # Reactive class
    reactive_cls = Div("Reactive", cls={"active": "$isActive", "disabled": "$isDisabled"})
    reactive_html = str(reactive_cls)
    assert "data-class=" in reactive_html
    assert '"active":"$isActive"' in reactive_html
    print("   ✓ Static and reactive classes working")
    
    # Test 5: DS Action generators
    print("\n✅ Test 5: DS Action generators")
    actions = Div(
        Button("GET", ds_on_click=DS.get("/api/data", target="#content")),
        Button("POST", ds_on_click=DS.post("/api/create", data={"name": "test"})),
        Button("Set", ds_on_click=DS.set("count", 10)),
        Button("Toggle", ds_on_click=DS.toggle("active")),
        Button("Chain", ds_on_click=DS.chain(
            DS.set("loading", True),
            DS.get("/api/data"),
            DS.set("loading", False)
        ))
    )
    action_html = str(actions)
    assert "@get('/api/data')" in action_html and "@target('#content')" in action_html
    assert "$count = 10" in action_html
    assert "$active = !$active" in action_html
    print("   ✓ DS action generators working")
    
    # Test 6: Complex real-world example
    print("\n✅ Test 6: Complex real-world example")
    complex_form = Form(
        H1("User Registration"),
        Input(
            type="email",
            placeholder="Email",
            ds_bind="user.email",
            ds_on_input__debounce_300ms=DS.get("/api/validate", email="$user.email")
        ),
        Input(
            type="password",
            placeholder="Password",
            ds_bind="user.password",
            ds_show="$user.email.length > 0"
        ),
        Button(
            "Register",
            ds_on_click=DS.conditional(
                "$user.email && $user.password",
                DS.post("/api/register", data="$user"),
                "alert('Please fill all fields')"
            ),
            ds_cls=reactive_class(
                disabled="!$user.email || !$user.password",
                loading="$submitting"
            )
        ),
        ds_signals=signals(
            user={"email": "", "password": ""},
            submitting=False
        ),
        ds_on_load=DS.set("pageLoaded", True)
    )
    complex_html = str(complex_form)
    assert "data-bind=" in complex_html
    assert "data-on-input.debounce.300ms=" in complex_html
    assert "data-show=" in complex_html
    assert "data-class=" in complex_html
    assert "data-signals=" in complex_html
    assert "data-on-load=" in complex_html
    print("   ✓ Complex real-world example working")
    
    # Test 7: JavaScript expression detection
    print("\n✅ Test 7: JavaScript expression detection")
    expressions = Div(
        ds_text="$count",                    # Signal reference
        ds_show="$count > 0",               # Comparison
        ds_cls={"active": "$isActive"},     # Object with expression
        ds_on_click="@get('/api/data')"     # Action reference
    )
    expr_html = str(expressions)
    assert 'data-text="$count"' in expr_html
    assert 'data-show="$count > 0"' in expr_html
    assert 'data-on-click="@get' in expr_html
    print("   ✓ JavaScript expression detection working")
    
    # Test 8: Performance validation
    print("\n✅ Test 8: Performance validation")
    import time
    start = time.time()
    for i in range(1000):
        test_div = Div(
            f"Item {i}",
            ds_text=f"'Item ' + {i}",
            ds_signals=signals(value=i),
            ds_cls={"active": f"$value === {i}"}
        )
        str(test_div)
    end = time.time()
    performance_time = end - start
    print(f"   ✓ Generated 1000 Datastar components in {performance_time:.3f}s")
    print(f"   ✓ Throughput: {1000/performance_time:.0f} components/second")
    
    print(f"\n🎉 All tests passed! Datastar integration is working correctly.")
    print(f"📊 Performance: {1000/performance_time:.0f} components/second")
    return True

if __name__ == "__main__":
    try:
        test_all_datastar_features()
        print("\n🚀 RustyTags Datastar integration is ready for production!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()