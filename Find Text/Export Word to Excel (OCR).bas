Attribute VB_Name = "Thecarlosmff"
Sub Transfer_From_Word()

    Application.DisplayAlerts = False 'Disable all the Alerts from excel
    Application.ScreenUpdating = False 'After opening Word Doc, Document will not be visible
    'Create a New Object for Microsoft Word Application
    Dim objWord As New Word.Application
    'Create a New Word Document Object
    Dim objDoc As New Word.Document
    'Open a Word Document and Set it to the newly created object above
    Set objDoc = objWord.documents.Open("C:\test.docx")
        
    Dim Col As Integer
    Col = 1
    Dim i As Integer
    i = 0
    Dim j As Integer
    j = 1
    Dim currentRow As String
    currentRow = ""
    
    Do While i < objDoc.Range.End                               'until the end of the file
    strTemp = objDoc.Range(i, i + 1)                            'checks char by char
    If strTemp = Chr(12) Then                                   'break page
        currentRow = Left(currentRow, Len(currentRow) - 1)
        'deletes the last new line of the string since isn't needed
        Cells(j, Col).Value = currentRow                        'writes in a new row
        j = j + 1                                               'advances for the next row
        currentRow = ""                                         'Reset the string that stores the
        ElseIf strTemp = Chr(13) Then                           'new line
            'strTemp = " "                                       'replaces the new line for a space
            strTemp = Chr(10)                                   'Excel Alt+ENTER
            currentRow = currentRow + strTemp                   'adds the space to the current string
            'this process will add an "\n" at the end of the currentRow in the last
            'interation before the break page, so we need to remove it.
        Else
            currentRow = currentRow + strTemp                   'is a normal letter/char
    End If
    i = i + 1                                                   'next char
    Loop
  
    objDoc.Close SaveChanges:=wdDoNotSaveChanges
    objWord.Quit

End Sub
