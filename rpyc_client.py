import rpyc

c = rpyc.connect("localhost", 18861)

remote_svc = c.root

my_answer = remote_svc.get_answer() # method call
real_answer = remote_svc.the_real_answer_though # attribute read

print("method answer:{}".format(my_answer))
print("attribute answer:{}".format(real_answer))
