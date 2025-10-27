def switch(newselected_files):
    with open(newselected_files, 'r') as f:
        rstyle = f.read()
    return rstyle