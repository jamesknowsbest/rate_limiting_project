# rate_limiting_project
sample project using flask to explore different rate limiting algorithums


## see rate limiting working

**start the flask server**
```bash
python app.py
```

**send more than 10 requests**
```powershell
for ($i=1; $i -le 12; $i++) {
    curl.exe -H "X-User: alice" "http://127.0.0.1:5000/hello"
}
```

**output**
```
{
  "message": "Hello!"
}
{
  "message": "Hello!"
}
{
  "message": "Hello!"
}
{
  "message": "Hello!"
}
{
  "message": "Hello!"
}
{
  "message": "Hello!"
}
{
  "error": "Rate limit exceeded"
}
{
  "error": "Rate limit exceeded"
}
{
  "error": "Rate limit exceeded"
}
{
  "error": "Rate limit exceeded"
}
{
  "error": "Rate limit exceeded"
}
{
  "error": "Rate limit exceeded"
}
```