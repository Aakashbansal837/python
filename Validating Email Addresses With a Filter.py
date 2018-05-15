def fun(s):
    arr = list(s)
    if ("@" not in arr) or ("." not in arr):
        return False
    arr.remove("@");arr.remove(".")
    if ("@" in arr) or ("." in arr):
        return False
    a = s.split("@")
    b = a[1].split(".")
    user=a[0];web = b[0];ext = b[1]
    ul  =list(user)
    if len(ul) == 0:
        return False
    for i in ul:
        tmp = i.isalnum()
        if  (tmp == False) and (i != "-") and (i != "_"):
            return False
    wl = list(web)
    if len(wl) == 0:
        return False
    for i in wl:
        tmp = i.isalnum()
        if  (tmp == False):
            return False
    el = list(ext)
    if len(el) > 3:
        return False
    return True



def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
