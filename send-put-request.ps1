$url = "http://127.0.0.1:8000/memos/1"
$body = @{
    id = 1
    title = "Updated Memo"
    content = "This is the updated content"
}

$jsonBody = $body | ConvertTo-Json

$headers = @{
    "Content-Type" = "application/json"
}

Invoke-RestMethod -Uri $url -Method Put -Headers $headers -Body $jsonBody
