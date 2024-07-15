import psutil

cpu_percent = psutil.cpu_percent(interval=1)
print("cpu 활용률 : ", cpu_percent, "%")

cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True)
print("cpu 코어 개수 : ", len(cpu_percent_per_core),"개")

print("cpu 코어별 활용률")
for i in range(len(cpu_percent_per_core)):
    print(i+1 , "번째 cpu 활용률 : ", cpu_percent_per_core[i])

print("전체 메모리 공간 : ", psutil.virtual_memory().total / (1024 ** 3),  "GB")
print(f"사용 가능한 메모리: {psutil.virtual_memory().available / (1024 ** 3):.2f} GB")
virtual_memory_percent = psutil.virtual_memory().percent
print("메모리 활용률 : ", virtual_memory_percent, "%");