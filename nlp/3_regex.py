import re

def extract_phone_number(text):
    # Define a regex pattern for phone numbers
    phone_pattern = r'\d{10} | \(\d{3}\)-\d{3}-\d{4} | \d{3}-\d{3}-\d{4}'
    
    # Search for the pattern in the text
    res = re.findall(phone_pattern, text)
    
    print(res)


def extract_email(text):
    # Define a regex pattern for email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]*\.[a-zA-Z]{2,}'
    
    # Search for the pattern in the text
    res = re.findall(email_pattern, text)
    
    print(res)


if __name__ == "__main__":
    #extract phone number and email from the text

    chat1="""
    Hello, my name is John Doe. You can reach me at 123-456-7890 or 
    email me at john.doe@example.com
    """

    chat2="""
    Hi, I'm Jane Smith. My phone number is (123)-456-7890 
    and my email is jane.smith@example.com
    """

    chat3="""
    Hey, I'm Bob Johnson. You can contact me at 1234567890 or  
    email me at bob.johnson@example.com
    """

    extract_phone_number(chat1)
    extract_phone_number(chat2)
    extract_phone_number(chat3)
    extract_email(chat1)
    extract_email(chat2)
    extract_email(chat3)