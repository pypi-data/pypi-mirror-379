# UnquoteMail

This library is intended to parse a given HTML and/or Text message and return only the new message without the previous conversation(s).

It is used in production at [Fernand](https://getfernand.com).

Parsing an email is quite difficult because of the amount of various mail providers and their specific approaches.
Unfortunately, there is no standard for separating the new content to the previous conversation so we need to rely on different tricks.

We took a progressive approach on parsing the document, in the following order:

1. We first try to identify and then remove all the known markup language, such as ".gmail_quote", ".protonmail_quote" and the likes
2. If we don't find it, we fallback on Regex to identify standard "On YYYY/MM/dd HH:mm:ss, bob <bob@example.com> wrote:" patterns

If we succeed at the point 1, we then re-generate the text data by converting the remaining HTML to markdown using the html2text library.

If we succeed at point 2, we parse the HTML (again) to locate the matched regex pattern from the text version. We then remove everything from that point (including the matched pattern) in the HTML structure.

If we fail to locate the pattern in the HTML structure, we re-create a new HTML by converting the text to HTML 

We allow ourselves to rewrite the text to HTML in that last resort because we consider that an email containing previous data is generally an human-written reply and not a marketing email with advanced structure, so the content should be basic to parse (link, bold/italic/underline, images and that's almost all; All of what a Markdown converter can do).


## Origin

Before building our own, we were hoping to find an awesome library that was doing all of dirty work for us, in Python, but unfortunately we couldn't find what were looking for.
Our criteria were:

1. Must be in Python
2. Must handle both text/html and text/plain (with a priority to HTML and a fallback to Text)
3. Be able to build back the HTML data from the parsed Plain, and vice-versa.

We found two main libraries from known providers: 

 * [Email Reply Parser - Crisp](https://github.com/crisp-oss/email-reply-parser/)
 * [Talon - Mailgun](https://github.com/mailgun/talon)

For Crisp, what is interesting is their extended set of regex patterns for identifying text emails, but they lack the HTML support we were needing.
Moreover, their code is in Javascript.

For Mailgun, they checked all the cases (in Python, handling both HTML and TXT), but they provide machine learning which we aren't looking for, and offer more advanced features (identifying signatures, ...) we are not interested either.

So we decided to build our own, by merging the Regex patterns from both libraries into one, and extending the tests from our own system in the hope it will help someone else :)


## Usage

The library is very straightforward:

```python
from unquotemail import Unquote

# You previously retrieved the text/html and text/plain version of an email

unquote = Unquote(email_html, email_text)
print(unquote.get_html())  # Will output the email without the included replies.
```

The `Unquote` class accepts 4 parameters:

 * html: A string containing the HTML data
 * text: A string containing the Text data
 * sender: (Optional) The message_id of the email, generally under the form <{hash}@{hostname}>
 * parse: (Optional) - Defaults to True. Will parse the message.

All the parameters are optional by default BUT you must past either a valid `html` or `text` value (otherwise it's kind of useless, isn't it?).

The `sender` parameter is not required and doesn't do anything for now, but it's possible in the future that we will rely on the sender to better parse an email. (A @yahoo.com email might help the parser better know what to do, and not lookup for a "gmail_quote" div for instance)

Finally, the `parse` boolean, if set to false, won't ... well, parse the email.

The reason for this is quite simple. Imagine the following:

```python
unquote = Unquote(email_html, email_text, parse=False)

if not is_new_email:
    # We don't unquote a new email as we want to keep the context
    # But for all following emails, we do want to remove that context since we already have it
    unquote.parse()

message = Message(unquote.get_html(), unquote.get_text())
message.save()  # in the database
```


## Special thanks

We used the regex from the following libraries to create our own.
Most of the regex patterns you see on UnquoteMail have been modified, but the root is from these two libraries:

 * [Talon (Mailgun)](https://github.com/mailgun/talon)
 * [Email Reply Parser (Crisp)](https://github.com/crisp-oss/email-reply-parser)

So, thank you to them!


## Testing

Our `test/` folder contains a suite of test.
Some of the files present in the test folder have been retrieved from Crisp and Talon (again, thanks) and we adjusted these to our test case.

To run the tests, do the following:

`pytest`

Or to run only one test:

`pytest -k "test_unquote[talon_9.html-talon_9.html]"`

**WARN**: For now, we only have 105 tests successfully passing for a total of 168 tests.
We need to continue a bit of work to improve the test suite