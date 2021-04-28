Attribute VB_Name = "Thecarlosmff"
Sub Transfer_From_Word()
    'Declare variables
    Dim enable_translation As Boolean
    Dim pos As Integer
    Dim translated As String
    Dim InputLang As String
    Dim OutputLang As String
    
    '______________________________________________________________________________________________

    Application.DisplayAlerts = False 'Disable all the Alerts from excel
    Application.ScreenUpdating = False 'After opening Word Doc, Document will not be visible
    'Create a New Object for Microsoft Word Application
    Dim objWord As New Word.Application
    'Create a New Word Document Object
    Dim objDoc As New Word.Document
    'Open a Word Document and Set it to the newly created object above
    Set objDoc = objWord.documents.Open("D:\test.docx")
    '---------------------------------TRANSLATION-------------------------------------------------
    enable_translation = True
    pos = 1 'pos 1 on the right, pos 0 overwrites the original text, pos -1 on the left.
    translated = ""
    InputLang = "en"
    OutputLang = "ja"
    'en = english, ja = japonese, pt = portuguese ...

    '-------------------------------------------------------------------------------------------
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
        If enable_translation Then
            translated = GTranslate(currentRow, InputLang, OutputLang)
            Cells(j, Col + pos).Value = translated
        End If
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

Public Function GTranslate(strInput As String, strFromSourceLanguage As String, strToTargetLanguage As String) As String
    'https://www.youtube.com/watch?v=RsyqqzholVk full credits
    Dim strURL As String
    Dim objHTTP As Object
    Dim objHTML As Object
    Dim objDivs As Object, objDiv As Object
    Dim strTranslated As String

    ' send query to web page
    strURL = "https://translate.google.com/m?hl=?" & strFromSourceLanguage & _
        "&sl=" & strFromSourceLanguage & _
        "&tl=" & strToTargetLanguage & _
        "&ie=UTF-8&prev=_m&q=" & strInput

    Set objHTTP = CreateObject("MSXML2.ServerXMLHTTP") 'late binding
    objHTTP.Open "GET", strURL, False
    objHTTP.setRequestHeader "User-Agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"
    objHTTP.send ""

    ' create an html document
    Set objHTML = CreateObject("htmlfile")
    With objHTML
        .Open
        .Write objHTTP.responsetext
        .Close
    End With
    
    'Range("H1") = objHTTP.responsetext
    
    Set objDivs = objHTML.getElementsByTagName("div")
    
    For Each objDiv In objDivs

        If objDiv.ClassName = "result-container" Then
            strTranslated = objDiv.innerText
            GTranslate = strTranslated
        End If
        
    Next objDiv
    
    Set objHTML = Nothing
    Set objHTTP = Nothing

End Function
