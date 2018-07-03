# Q1: Extract the user id, domain name and suffix from the following email addresses.
# emails = "zuck26@facebook.com" "page33@google.com"
# "jeff42@amazon.com"
import re
emails =  ["zuck26@facebook.com", "page33@google.com", "jeff42@amazon.com"]
def split(email):
    username = email.split('@')[0]
    domain = email.split('@')[1]
    domain_name = domain.split('.')[0]
    domain_type = domain.split('.')[1]
    print('username: ',username)
    print('domain: ',domain_name)
    print('domain type: ',domain_type)
for email in emails:
        split(email)

#Q2: Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
import re
text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."""
list = re.findall(r'\b[bB]\w+',text)
matched = []
for i in list:
    if i not in matched:
        matched.append(i)
        print matched

#Q.3- Split the following irregular sentence into words 
to_remove = ".,;_"
sen = """A, very very; irregular_sentence"""
for x in to_remove:
    sen = sen.replace(x,'')
print(sen)