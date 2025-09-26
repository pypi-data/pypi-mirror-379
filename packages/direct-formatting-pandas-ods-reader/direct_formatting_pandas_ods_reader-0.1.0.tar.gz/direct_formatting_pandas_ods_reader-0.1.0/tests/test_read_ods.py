# tests/test_read_ods.py
import pandas as pd
import pytest
from direct_formatting_pandas_ods_reader import read_ods

# Expected data for each format
EXPECTED_DATA = {
    "asciidoc": pd.DataFrame([
        ["Column 1", "Column 2", "Column 3", "Column 4"],
        ["Some content in roman", "__Some other content in italics__", "", ""],
        ["**Some content in bold**", "**__Some content in bold and italics__**", "__Value__", ""],
        ["A __word __and another__ w__o__rd__ in italics", "[.underline]#Some underlines#", "", ""]
    ]),
    "markdown": pd.DataFrame([
        ["Column 1", "Column 2", "Column 3", "Column 4"],
        ["Some content in roman", "__Some other content in italics__", "", ""],
        ["**Some content in bold**", "**__Some content in bold and italics__**", "__Value__", ""],
        ["A __word __and another__ w__o__rd__ in italics", "<u>Some underlines</u>", "", ""]
    ]),
    "html": pd.DataFrame([
        ["Column 1", "Column 2", "Column 3", "Column 4"],
        ["Some content in roman", "<i>Some other content in italics</i>", "", ""],
        ["<b>Some content in bold</b>", "<b><i>Some content in bold and italics</i></b>", "<i>Value</i>", ""],
        ["A <i>word </i>and another<i> w</i>o<i>rd</i> in italics", "<u>Some underlines</u>", "", ""]
    ]),
}


# List of formats to test
FORMATS = ["asciidoc", "markdown", "html"]

@pytest.mark.parametrize("fmt", FORMATS)
def test_read_ods_formats(fmt):
    df = read_ods("tests/test.ods", format=fmt)
    
    # Use pandas testing utility for clean comparison
    pd.testing.assert_frame_equal(df, EXPECTED_DATA[fmt])
