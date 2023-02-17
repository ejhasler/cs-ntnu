import time

T_sleep = 3
print("Specified sleep time = ", T_sleep)

t_before = time.time()
time.sleep(T_sleep)
t_after = time.time()

print("t_before = ", t_before)
print("t_after = ", t_after)
print("Real sleep time = ", t_after - t_before)