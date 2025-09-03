def run_tests():
    obj1 = {"a": {"b": {"c": "d"}}}
    obj2 = {"x": {"y": {"z": "a"}}}
    
    assert get_value(obj1, "a/b/c") == "d"
    assert get_value(obj2, "x/y/z") == "a"
    
    try:
        get_value(obj1, "a/b/x")  # invalid key
    except KeyError:
        print("Test passed: KeyError raised for invalid key")
    else:
        print("Test failed: No error raised for invalid key")
    
    print("All other tests passed!")


if __name__ == "__main__":
    run_tests()