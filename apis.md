/submit/expense/
POST, returns a json
Input: token, date(optional), amount, text
Output: {"status": "ok"}


/submit/income/
POST, returns a json
Input: token, date(optional), amount, text
Output: {"status": "ok"}


/accounts/register/
  step1:
    POST
    Input: username, email, password
    Output: {"status": "ok"}
  step2: #click on link with the code in the email
    GET
    Input: email, code
    Output: {"status": "ok"}  (shows the token)


/q/generalstat/
  POST
  Input: fromdate(optional), todate(optional), token
  Output: json from some general stats related to this user
