from .custommodels import Question
from .custommodels import Answer
from .custommodels import Account
from .custommodels import Subject
from .custommodels import Session
global_question_class = Question()
global_answer_class = Answer()
global_account_class = Account()
global_subject_class = Subject()
global_session_class = Session()
def setglobal():
	global global_question_class, global_answer_class, global_account_class, global_subject_class, global_session_class

setglobal()
