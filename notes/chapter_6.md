Chapter 6: Email support with Flask-Mail (6a)
=============================================
Wrapper around the smtp library.
If config, uses port 25 on localhost.

Abstract this function for sending emails:

def send_email(to, subject, template, **kwargs):
msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)



Chapter 6: Asynchronous emails (6b)
===================================
Move the email function to a background thread to avoid delays and make website more responsive.
Best idea is to use Flask-Celery to handle asynchronous requests.

