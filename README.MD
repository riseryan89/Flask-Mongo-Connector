## Flask Server to Access MongoDB
#### Purposes
* This Server is design to be functioning as a gateway to access mongoDB from other back-end servers pointing RDB.
* JWT Token Authentication Purpose
* Other Functions can be added

#### Limits
* Do NOT make any API calls to other servers as it's a gateway.(For Speed)
* MUST make sure the benchmark score or time can be taken to measure the performance.
* Do NOT make this server do any CPU-Intensive works.


#### Maintain
* Keep It Simple and Stupid


#### USAGE
Reqeust : /auth

with Json Body(POST):
```json
{
  "token": <ValidJWTToken>,
  "func": "user"
}
```

Currently support only 'user' func.<br><br>

Sample Response on Success:
```json
{
    "data": {
        "SN": <SN-Integer>,
        "_id": <DocId-String>,
        "email": <Email-String>,
        "flag": <Flag-String>,
        "kycID": <KYCID-String>,
        "nick": <NickName-String>,
        "signupDate": <SignUpDate-DateTime>,
        "state": <ActiveStatus-String>,
        "wSN": <wSN-Integer>
    },
    "result": "ok"
}
```


Sample Response on Fail: 
```json
{
    "data": "invalid signature",
    "result": "failed"
}
```