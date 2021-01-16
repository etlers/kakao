def solution(in_string):
    
    # 문자열을 하나의 문자 리스트로 생성
    def make_list_char():
        idx = 0
        list_char = []
        while idx < len(in_string):
            list_char.append(in_string[idx:idx+1])    
            idx += 1
        return list_char

    # 순서대로 동일한 문자 줄이기
    def find_seq_char(list_char):
        temp_char = ""
        agg_char = ""
        prefix_num = 1
        for idx_char in list_char:
            if temp_char != "":
                if temp_char == idx_char:
                    prefix_num += 1
                else:
                    if prefix_num < 2:
                        agg_char = agg_char + temp_char
                    else:
                        agg_char = agg_char + str(prefix_num) + temp_char
                    prefix_num = 1
            temp_char = idx_char

        if prefix_num < 2:
            agg_char = agg_char + temp_char  
        else:
            agg_char = agg_char + str(prefix_num) + temp_char

        return agg_char

    result_list = make_list_char()
    sequence_string = find_seq_char(result_list)

    # 문자열 패턴으로 자르기
    def find_pattern_num():
        list_num = []
        for idx in range(int(len(in_string) / 2)):
            list_num.append(idx + 1)

        result_string = ""
        for idx in list_num:
            repeat_string = ""
            temp_string = ""            
            i = 0
            ix = 1
            while i*idx < len(in_string):
                if temp_string != "":
                    if temp_string == in_string[i*idx:i*idx+idx]:
                        ix += 1
                    else:
                        repeat_string += str(ix) + temp_string
                        ix = 1
                temp_string = in_string[i*idx:i*idx+idx]        
                i += 1
            repeat_string += str(ix) + temp_string                
            repeat_string = repeat_string.replace("1", "")
            if len(result_string) > len(repeat_string):
                result_string = repeat_string
            elif len(result_string) == 0:
                result_string = repeat_string
        return result_string

    pattern_string = find_pattern_num()

    if (len(pattern_string) == 0) or (len(pattern_string) > len(sequence_string)):
        answer = len(sequence_string)
    else:
        answer = len(pattern_string)
        
    return answer

if __name__ == "__main__":
    s = "ajshdfyhfuidnjdcjfjkdhsklalejejkajshdfyhfuidnjdcjfjkdhsklalejejk"
    print(solution(s))    