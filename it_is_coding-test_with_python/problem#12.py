def check_func(answer):
    for now in answer:
        x, y, stuff = now
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        elif stuff == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, m = frame
        if m:
            answer.append([x, y, stuff])
            if check_func(answer) == False:
                answer.remove([x, y, stuff])
        else:
            answer.remove([x, y, stuff])
            if check_func(answer) == False:
                answer.append([x, y, stuff]) 
    return sorted(answer)