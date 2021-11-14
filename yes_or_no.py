
from ask import Question, Answers, qt 
def yes_or_no(question:str, answer:bool=None, debug_mode:bool=True):
    if answer != None or debug_mode:
        return ' '.join([question,('yes' if answer else 'no')])
    question = Question(question, qt.Confirm,'yes_or_no',choices=['yes', 'no'])
    return Answers([question]).answer()
