blocked_word= ['destroy','bad_word','suscide','hack','money'] # we have libraries ==toxicity ==
def validation(prompt):
    flag = False
    for word in prompt.lower().split():
        if word in blocked_word:
            flag = True
            return flag
        
    return flag


