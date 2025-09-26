from cpp_fwd_sorter import sorter


def run_sort(text: str) -> str:
    return sorter.process_full_text(text)


def test_basic_sorting():
    inp = """class ZClass;\nclass AClass;\nstruct BStruct;\nclass MClass; // keep\nstruct AStruct;\n"""
    out = run_sort(inp)
    # Check ordering: class AClass, MClass, ZClass then structs AStruct, BStruct
    assert "class AClass;" in out
    assert out.index("class AClass;") < out.index("class MClass;")
    assert out.index("class MClass;") < out.index("class ZClass;")
    assert out.index("struct AStruct;") < out.index("struct BStruct;")


def test_keep_comments_and_indent():
    inp = """    class z; // z comment\n    class A;\n"""
    out = run_sort(inp)
    # Comments should remain attached to their declaration
    assert "// z comment" in out
    # Indentation preserved
    assert out.startswith("    class A;")


def test_selection_range():
    text = "line1\nclass Z;\nclass A;\nline4\n"
    # Select only the middle two lines (compute byte offsets)
    b = text.encode("utf-8")
    start = b.find(b"class Z;")
    length = b.find(b"line4") - start

    out = sorter.process_with_ranges(text, [(start, length)])
    # After processing the selected region, the classes should be sorted
    assert "class A;" in out
    assert out.index("class A;") < out.index("class Z;")
