$headers = @{
    "Content-Type" = "application/json"
}

$body = @{
    "id" = 1
    "title" = "First Memo"
    "content" = "This is the content of the first memo"
}

$bodyJson = $body | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:8000/memos/" -Method Post -Headers $headers -Body $bodyJson

##curl http://127.0.0.1:8000/memos/
