import sys
sys.path.append("../svm/")
from svm_author_id import svm_author
from sshex import sshclient_execmd
sshclient_execmd(execmd=svm_author)
