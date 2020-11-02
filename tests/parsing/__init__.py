
def load_testdata(filespec: str) -> str:
    with open(filespec) as f:
        return f.read()
