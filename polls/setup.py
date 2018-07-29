from .custommodels import Question
from .custommodels import Answer
global_question_class = Question()
global_answer_class = Answer()
def setglobal():
	global global_question_class, global_answer_class

setglobal()
