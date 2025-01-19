def solution(edges):
    answer = [0, 0, 0, 0] # 생성 정점, 도넛, 막대, 8자
    max_val = max(map(max, edges)) + 1  # +1 은 인덱스 맞춰주기 위함
    in_cnt, out_cnt = [0] * max_val, [0] * max_val
        
    for out_edge, in_edge in edges:  # in, out 간선 저장
        out_cnt[out_edge] += 1
        in_cnt[in_edge] += 1
            
    for node in range(1, max_val):
        if in_cnt[node] == 0 and out_cnt[node] >= 2: # 생성 노드
            answer[0] = node 
        # 생성 노드의 간선을 제거 하면 in_cnt[node] == 1   
        elif in_cnt[node] >= 1 and out_cnt[node] == 0: # 막대 그래프
            answer[2] += 1
        # 생성 노드의 간선을 제거 하면 in_cnt[node] == 2   
        elif in_cnt[node] >= 2 and out_cnt[node] == 2: # 8자 그래프 
            answer[3] += 1
    answer[1] = out_cnt[answer[0]] - sum(answer[2:])    # 도넛 그래프
    
    return answer

ans = solution([[2,3], [4,3], [1,1], [2,1]])
print(ans)