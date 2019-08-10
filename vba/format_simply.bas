''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' シートを簡易整形します。
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Sub 簡易整形()
    ' すべてのセルを選択
    Cells.Select

    ' セルのフォントを設定
    With Selection.Font
        .Name = "Yu Gothic UI"
        .Size = 9
        .Strikethrough = False
        .Superscript = False
        .Subscript = False
        .OutlineFont = False
        .Shadow = False
        .Underline = xlUnderlineStyleNone
        .TintAndShade = 0
        .ThemeFont = xlThemeFontNone
    End With

    ' セルの縦幅を自動設定
    Cells.EntireRow.AutoFit
    Selection.End(xlUp).Select
    Selection.End(xlToLeft).Select

    ' ウィンドウの拡大率を設定
    ActiveWindow.Zoom = 100

    ' セルの位置を一番左上にする
    range("A1").Select
End Sub
