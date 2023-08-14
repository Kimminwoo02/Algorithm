def solution(players, callings):
    answer = [] 
    player_dict = {player : idx+1 for idx, player in enumerate(players)}
    rank_dict = {idx+1 : player for idx, player in enumerate(players)}

    for call in callings:
        rank = player_dict[call]
    
        player_dict[rank_dict[rank-1]], player_dict[rank_dict[rank]] = player_dict[rank_dict[rank]], player_dict[rank_dict[rank-1]]
        rank_dict[rank-1], rank_dict[rank] = rank_dict[rank], rank_dict[rank-1]

        
    
    return list(rank_dict.values())