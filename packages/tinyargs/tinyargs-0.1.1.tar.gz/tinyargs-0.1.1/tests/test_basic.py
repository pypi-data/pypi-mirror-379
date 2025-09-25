# tests/test_tinyargs_all.py
import sys
import pytest

from tinyargs import get, flag, args, TinyArgsError

# ---------- Helpers ----------

def set_argv(*tokens: str):
    """Replace sys.argv with a fake command (program name + tokens)."""
    sys.argv = ["prog", *tokens]


# ---------- Basic fetching ----------

def test_get_simple_value():
    set_argv("--name", "Alice")
    assert get("--name") == "Alice"

def test_get_equals_syntax():
    set_argv("--name=Alice")
    assert get("--name") == "Alice"

def test_get_missing_with_default():
    set_argv()
    assert get("--age", type=int, default=18) == 18

def test_get_missing_required_raises():
    set_argv()
    with pytest.raises(TinyArgsError) as e:
        get("--name", required=True)
    assert "--name" in str(e.value)


# ---------- Types & casting ----------

def test_get_cast_int_float():
    set_argv("--age", "21", "--tax", "13.0")
    assert get("--age", type=int) == 21
    assert get("--tax", type=float) == 13.0

def test_get_cast_failure_raises():
    set_argv("--age", "twenty")
    with pytest.raises(TinyArgsError):
        get("--age", type=int)

def test_args_with_types_and_defaults_tuple_order():
    set_argv("--w", "640", "--h", "480")
    w, h = args("--w", "--h", types={"--w": int, "--h": int})
    assert (w, h) == (640, 480)

def test_args_with_missing_uses_defaults_in_order():
    set_argv("--w", "1024")
    w, h = args("--w", "--h", types={"--w": int, "--h": int},
                defaults={"--h": 768})
    assert (w, h) == (1024, 768)

def test_args_required_list_raises_for_any_missing():
    set_argv("--w", "320")
    with pytest.raises(TinyArgsError):
        args("--w", "--h", types={"--w": int, "--h": int},
             required=["--w", "--h"])


# ---------- Flags (booleans) ----------

def test_flag_present_true():
    set_argv("--verbose")
    assert flag("--verbose") is True

def test_flag_absent_false():
    set_argv()
    assert flag("--verbose") is False

def test_flag_with_value_is_still_true_when_present():
    # Even if someone passes "--verbose true", presence should count as True.
    set_argv("--verbose", "true")
    assert flag("--verbose") is True

def test_boolean_values_should_use_flag_not_get():
    # Documented behavior: bool("false") is True in Python, so advise flag()
    set_argv("--dry-run", "false")
    # We assert the recommended way works:
    assert flag("--dry-run") is True  # presence means True
    # And document that get(..., type=bool) isn't supported (no assert here)


# ---------- Mixed forms & precedence ----------

def test_mixed_equals_and_space_syntax():
    set_argv("--name=Alice", "--city", "Toronto")
    name, city = args("--name", "--city")
    assert (name, city) == ("Alice", "Toronto")

def test_last_value_wins_if_flag_repeated():
    set_argv("--w", "640", "--w", "800")
    (w,) = args("--w", types={"--w": int})
    assert w == 800

def test_unrelated_flags_are_ignored():
    set_argv("--foo", "bar", "--name", "Alice")
    assert get("--name") == "Alice"
    # Unknown ones don't break anything:
    assert flag("--nonexistent") is False


# ---------- Error messages & clarity ----------

def test_missing_required_error_message_includes_flag():
    set_argv()
    with pytest.raises(TinyArgsError) as e:
        args("--a", "--b", required=["--b"])
    msg = str(e.value)
    assert "--b" in msg and "Missing" in msg

def test_cast_error_message_includes_value_and_type():
    set_argv("--age", "twenty")
    with pytest.raises(TinyArgsError) as e:
        get("--age", type=int)
    msg = str(e.value)
    assert "twenty" in msg and "int" in msg


# ---------- Realistic use cases ----------

def test_use_case_quick_resize_script():
    # python resize.py --in photo.jpg --w 800 --h 600 --keep-aspect
    set_argv("--in", "photo.jpg", "--w", "800", "--h", "600", "--keep-aspect")
    src = get("--in", required=True)
    w, h = args("--w", "--h", types={"--w": int, "--h": int}, required=["--w", "--h"])
    keep = flag("--keep-aspect")
    assert src == "photo.jpg"
    assert (w, h) == (800, 600)
    assert keep is True

def test_use_case_data_filter_script_defaults_and_types():
    # python filter_csv.py --src data.csv --col price --min 10.5
    set_argv("--src", "data.csv", "--col", "price", "--min", "10.5")
    src = get("--src", required=True)
    col = get("--col", default="value")
    min_val = get("--min", type=float, default=0.0)
    max_val = get("--max", type=float, default=999999.0)
    assert (src, col, min_val, max_val) == ("data.csv", "price", 10.5, 999999.0)

def test_use_case_release_hook_with_tag_flag():
    # python bump_version.py --level patch --tag
    set_argv("--level", "patch", "--tag")
    level = get("--level", required=True)
    do_tag = flag("--tag")
    assert level == "patch"
    assert do_tag is True
