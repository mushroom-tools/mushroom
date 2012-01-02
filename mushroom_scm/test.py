import pysvn
client = pysvn.Client()

client.checkout('svn://210.118.56.213/SVN_TEST', './test')


