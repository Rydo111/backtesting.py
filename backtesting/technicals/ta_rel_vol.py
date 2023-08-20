import pandas as pd
import sma


# -----------------------------------------------------------------------------
def ta_rvol(_df: pd.DataFrame, length: int = 20, **kwargs):
    """
    Can be modified for any type of ma if desired, particularly if pandas_ta is used
    """
    vol = _df['volume']

    close = _df["Close"]

    _ma = sma.sma(
        close=close,
        length=length,
        offset=None,
    )
    rvol = (vol / _ma.iloc[:, 0]).to_numpy()

    df = pd.DataFrame(
        {
            'rvol': rvol,
        },
        index=_df.index
    )

    if "fillna" in kwargs:
        df['rvol'].fillna(value=kwargs["fillna"], inplace=True)

    if "fill_method" in kwargs:
        df['rvol'].fillna(method=kwargs["fill_method"], inplace=True)

    return df

# -----------------------------------------------------------------------------
