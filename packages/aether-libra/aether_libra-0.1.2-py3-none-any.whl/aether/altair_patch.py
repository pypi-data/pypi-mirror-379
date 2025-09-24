import altair as alt


def set_altair_axis_padding(label_padding: int = 10) -> None:
    """
    Altair の X軸のタイトル・ラベル余白を共通テーマとして設定する。
    X軸ラベルの下側が切れてしまうバグ(？)に対するパッチ。
    
    Parameters
    ----------
    label_padding : int, optional
        軸ラベルと軸との余白（デフォルト: 10）
    
    Notes
    -----
    - 呼び出すと即座にテーマが有効になる
    - 他のグラフ作成コードより前に実行すること
    """
    alt.themes.register(
        'my_theme',
        lambda: {
            "config": {
                "axisX": {
                    "labelPadding": label_padding
                }
            }
        }
    )
    alt.themes.enable('my_theme')
