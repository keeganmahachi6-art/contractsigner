import re

def signing(sign, saved):
    fillable_fields = [
    "[Date]",
    "[Provider Name]",
    "[Provider Address]",
    "[Client Name]",
    "[Client Address]",
    "[Start Date]",
    "[End Date]",
    "[£Amount]",
    "[e.g., 50% upfront, 50% on completion]",
    "[Bank transfer / PayPal / Other]",
    "[Number]",
    "[Jurisdiction]",
    "provname",
    "name"
    ]
    print("The contract has been signed the contract is below")
    with open(sign) as f:
        content = f.read()
    for options in fillable_fields:
        x = input(f"Can you enter{options}")
        content = content.replace(options,x)
    with open(saved, "w") as f:
        f.write(content)
        print("saved successfully")
        print(content)
    
    


    

def keywords(file):
    core= [
    "Service Agreement",
    "Agreement",
    "Provider",
    "Client",
    "Services",
    "Term",
    "Payment",
    "Responsibilities",
    "Intellectual Property",
    "Confidentiality",
    "Termination",
    "Limitation of Liability",
    "Governing Law",
    "Entire Agreement",
    "Signed"
    ]
    action = [
    "perform",
    "deliver",
    "pay",
    "provide",
    "own",
    "keep confidential",
    "terminate",
    "resolve disputes"
]

    results = [x for words in (core,action) for x in words ]
    keyword = re.search(results,file)
    if keyword:
        print(f"These keywords were found {keyword}")
    else:
        print("This contract does not have keywords")

def opener (file):
    with open(file) as f:
        openit = f.read()
        print(openit)
        return openit
    



        
def options(option, name):
    user = input("What do you want to do(R to read, X to search for keywords, L to sign)").lower()
    if user.lower() not in ("r","x","l"):
        raise TypeError("Input Entered is invalid")
    
    match user:
        case "r":
            opener(option)
        case "x":
            keywords(option)
        case "l":
            signing(option,name)

options("lesson1/projects/contract.txt","Wesley")





