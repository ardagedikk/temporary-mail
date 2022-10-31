# Temporary Mail
It allows you to generate disposable emails.
## Usage
```python
from temp_mail import TempMail
temp_mail = TempMail()
temp_mail.set_email(temp_mail.get_random_email())
```
## Usage
```python
# If there is not a mail then mailbox[0] is status code, mailbox[1] is error message
# If there is a mail then mailbox[0] is status code, mailbox[1] is mail list. You can get a mail with mailbox[1][n].
mailbox = temp_mail.check_mailbox()
if(mailbox[0] == 200):
    mail = temp_mail.get_mail_from_mailbox(mailbox[1][0])
    print(mail.get("textBody"))
```
```python
# Mail result.
{
	"id": 639,
	"from": "someone@example.com",
	"subject": "Some subject",
	"date": "2018-06-08 14:33:55",
	"attachments": [{
		"filename": "iometer.pdf",
		"contentType": "application\/pdf",
		"size": 47412
	}],
	"body": "Some message body\n\n",
	"textBody": "Some message body\n\n",
	"htmlBody": ""
}
    
```



## License
MIT
