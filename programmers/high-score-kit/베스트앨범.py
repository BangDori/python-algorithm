def solution(genres, plays):
    genres_dict = {}
    plays_dict = {}
    
    for idx in range(len(genres)):
        if not genres_dict.get(genres[idx]):
            genres_dict[genres[idx]] = [(idx, plays[idx])]
            plays_dict[genres[idx]] = plays[idx]
        else:
            genres_dict[genres[idx]].append((idx, plays[idx])) 
            plays_dict[genres[idx]] += plays[idx]
    
    playList = []
    for genre in plays_dict.keys():
        playList.append((genre, plays_dict.get(genre)))
    # 장르 내림차순 정렬
    playList.sort(reverse=True, key=lambda value: value[1])
    
    answer = []
    for genre, tot in playList:
        cur_list = genres_dict.get(genre)
                
        if len(cur_list) == 1:
            # 장르가 하나라면?
            answer.append(cur_list[0][0])
        else:
            # 장르 내림차순 정렬
            cur_list.sort(reverse=True, key=lambda value: (value[1]))
            answer.append(cur_list[0][0])
            answer.append(cur_list[1][0])
    
    print(answer)
    return answer