''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' 開かれているすべてのブックを保存します。
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Sub すべて保存()
    Dim book As Workbook

    For Each book In Application.Workbooks
        If Not book.ReadOnly And Windows(book.Name).Visible Then
            book.Save
        End If
    Next
End Sub
