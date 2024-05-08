class process:

    own_time = 0
    started = False
    finished = False

    def __init__(self, ID, duration, mat_ID):
        self.ID = ID               # ЧИСЛО
        self.duration = duration   # ЧИСЛО
        self.mat_ID = mat_ID       # СПИСОК!!!


def TIME(list_of_processes):
    global_time = 0

    ID_Finished_bool = dict()
    ID_Finished_bool[0] = True
    for proc in list_of_processes:
        ID_Finished_bool[proc.ID] = proc.finished

    while not check_dict(ID_Finished_bool):
        num_of_actual_proc = 0
        for proc in list_of_processes:
            if proc.started and not proc.finished:
                proc.own_time += 1
                num_of_actual_proc += 1
                if proc.own_time == proc.duration:
                    proc.finished = True

        for proc in list_of_processes:
            if not proc.started:
                flag = True
                for id in proc.mat_ID:
                    if not ID_Finished_bool[id]:
                        flag = False
                        break
                if flag:
                    proc.started = True
                    proc.own_time += 1
                    num_of_actual_proc += 1
                    if proc.own_time == proc.duration:
                        proc.finished = True

        for proc in list_of_processes:             # Обновляем инфу о законченных процессах
            ID_Finished_bool[proc.ID] = proc.finished

        global_time += 1
        print(num_of_actual_proc, end=" ")

    print()
    print(global_time)


def check_dict(a):
    flag = True
    for i in a:
        if not a[i]:
            flag = False
            break
    return flag


processes = list()
for i in range(int(input())):
    b = input().split("\t")
    ID = int(b[0])
    duration = int(b[1])
    mat_ID = [int(j) for j in b[2].split(" ")]

    a = process(ID, duration, mat_ID)
    processes.append(a)

TIME(processes)

