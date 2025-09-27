from akris_desktop.timeline import Timeline, Annotation, BEFORE, AFTER

def test_add_message():
    timeline = Timeline()
    message = {
        "body": "test",
        "self_chain": "foo",
        "net_chain": "bar",
        "timestamp": 100
    }
    index = timeline.add_message(message)
    assert index == 1

def test_messages_ordered_by_chain():
    timeline = Timeline()
    m1 = {
        "body": "test",
        "self_chain": "foo",
        "net_chain": "bar",
        "timestamp": 100,
        "message_hash": "baz"
    }
    m2 = {
        "body": "test",
        "self_chain": "baz",
        "net_chain": "baz",
        "timestamp": 100,
        "message_hash": "xyz",
    }
    timeline.add_message(m1)
    index = timeline.add_message(m2)
    assert index == 2

def test_add_annotation():
    timeline = Timeline()
    message = {
        "body": "test",
        "self_chain": "foo",
        "net_chain": "bar",
        "timestamp": 100
    }
    timeline.add_message(message)
    annotation = Annotation(100, "test", BEFORE)
    index = timeline.add_annotation(annotation)
    assert index == 1

def test_annotated_message_index():
    timeline = Timeline()
    message = {
        "body": "test",
        "self_chain": "foo",
        "net_chain": "bar",
        "timestamp": 100
    }
    timeline.add_message(message)
    annotation = Annotation(100, "test", BEFORE)
    timeline.add_annotation(annotation)
    index = timeline.calculate_message_index(message)
    assert index == 2

def test_account_for_antecedent_timestamp_groups():
    timeline = Timeline()
    m1 = {
        "body": "test",
        "self_chain": "foo",
        "net_chain": "bar",
        "timestamp": 100,
        "message_hash": "baz"
    }
    m2 = {
        "body": "test",
        "self_chain": "baz",
        "net_chain": "baz",
        "timestamp": 100,
        "message_hash": "xyz",
    }
    m3 = {
        "body": "test",
        "self_chain": "baz",
        "net_chain": "baz",
        "timestamp": 300,
        "message_hash": "xyz",
    }
    timeline.add_message(m1)
    timeline.add_message(m2)
    timeline.add_message(m3)
    index = timeline.calculate_message_index(m3)
    assert index == 3

def test_account_for_newlines():
    timeline = Timeline()
    m1 = {
        "body": "test\n test\n test",
        "self_chain": "foo",
        "net_chain": "bar",
        "timestamp": 100,
        "message_hash": "baz"
    }
    m2 = {
        "body": "test",
        "self_chain": "baz",
        "net_chain": "baz",
        "timestamp": 100,
        "message_hash": "xyz",
    }
    timeline.add_message(m1)
    timeline.add_message(m2)
    index = timeline.calculate_message_index(m2)
    assert index == 4

def test_account_for_newlines_in_antecedent_ts_groups():
    timeline = Timeline()
    m1 = {
        "body": "test\n test\n test",
        "self_chain": "foo",
        "net_chain": "bar",
        "timestamp": 100,
        "message_hash": "baz"
    }
    m2 = {
        "body": "test",
        "self_chain": "baz",
        "net_chain": "baz",
        "timestamp": 200,
        "message_hash": "xyz",
    }
    timeline.add_message(m1)
    timeline.add_message(m2)
    index = timeline.calculate_message_index(m2)
    assert index == 4
