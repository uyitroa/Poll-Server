from .custommodels import Question
from .custommodels import Answer
from .custommodels import Account
global_question_class = Question()
global_answer_class = Answer()
global_account_class = Account()
def setglobal():
	global global_question_class, global_answer_class, global_account_class

setglobal()
