''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' すべてのふりがなを削除します。
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Sub ふりがな削除()
    Dim range As range

    For Each range In ActiveSheet.UsedRange
        range.Characters.PhoneticCharacters = ""
    Next range
End Sub
