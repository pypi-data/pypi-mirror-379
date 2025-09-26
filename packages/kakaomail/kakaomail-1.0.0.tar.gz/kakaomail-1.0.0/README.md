# Kakaomail

A Python library for sending emails using Kakao Mail.

## Installation

You can install `kakaomail` using pip:

```shell
pip install kakaomail
```

Alternatively, you can install it from the source:

```shell
git clone https://github.com/aloecandy/kakaomail.git
cd kakaomail
python setup.py install
```

## Configuration

For authentication, you can use a `.env` file to store your Kakao Mail credentials. Create a `.env` file in your project's root directory with the following content:

```.env
KAKAO_ID=your_kakao_id
KAKAO_PASSWORD=your_kakao_password
```

The library will automatically load these credentials.

## Usage

### Login

There are two ways to log in:

1.  **Using `.env` file (recommended):**

    If you have configured your credentials in a `.env` file, you can log in without passing any arguments:

    ```python
    import kakaomail

    if kakaomail.login():
        print("Successfully logged in!")
    else:
        print("Failed to log in.")
    ```

2.  **Passing credentials directly:**

    You can also pass your ID and password directly to the `login` function:

    ```python
    import kakaomail

    if kakaomail.login("your_kakao_id", "your_kakao_password"):
        print("Successfully logged in!")
    else:
        print("Failed to log in.")
    ```

### Sending Emails

Once logged in, you can send emails using the `send` function.

**Basic Text Email:**

```python
import kakaomail

if kakaomail.login():
    kakaomail.send(
        recipient='recipient@domain.com',
        subject='Hello from Kakaomail!',
        text='This is a test email.'
    )
```

**HTML Email:**

To send an HTML email, set the `subtype` parameter to `'html'`.

```python
import kakaomail

if kakaomail.login():
    html_content = "<h1>Hello</h1><p>This is an HTML email.</p>"
    kakaomail.send(
        recipient='recipient@domain.com',
        subject='HTML Email Test',
        text=html_content,
        subtype='html'
    )
```

**Email with Attachments:**

You can send attachments by providing a list of file paths to the `attachments` parameter.

```python
import kakaomail

if kakaomail.login():
    kakaomail.send(
        recipient='recipient@domain.com',
        subject='Email with Attachments',
        text='Please find the attached files.',
        attachments=['/path/to/file1.jpg', '/path/to/file2.pdf']
    )
```