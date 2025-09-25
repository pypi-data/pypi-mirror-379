import shlex, tempfile, pathlib, os
import pandas as pd

def vd(df):
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        in_ = str(d / 'in.csv')
        out = str(d / 'out.csv')
        df.to_csv(in_)
        os.system(f"vd -o {shlex.quote(out)} {shlex.quote(in_)}")
        return pd.read_csv(out)
