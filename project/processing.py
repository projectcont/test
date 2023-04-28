
from typing import List, Dict, TypedDict, Optional, Union

def go (ans:Dict[int, str]) -> str:
    '''
    фукция принимает словорь из 70 ответов на вопросы
    возвращает тип личности
    :param ans:
    :return:
    '''

    user_ie = 0
    user_sn = 0
    user_tf = 0
    user_jp = 0

    user_i = 'I'
    user_n = 'N'
    user_f = 'F'
    user_p = 'P'

    ans.pop(0)
    print(len(ans))
    ans_=dict()

    if len(ans)<70:
        for i in range(1,71):
            if i>len(ans): ans_[i]='a'
            else: ans_[i]=ans[i]
        print("answers filled",  ans_ )
        ans=ans_


    if (ans[1]== 'a'): user_ie = user_ie + 1
    if (ans[2]== 'a'): user_sn = user_sn + 1
    if (ans[3]== 'a'):  user_sn = user_sn + 1
    if (ans[4]== 'a'): user_tf = user_tf + 1
    if (ans[5]== 'a'): user_tf = user_tf + 1
    if (ans[6]== 'a'): user_jp = user_jp + 1
    if (ans[7]== 'a'): user_jp = user_jp + 1
    if (ans[8]== 'a'): user_ie = user_ie + 1
    if (ans[9]== 'a'): user_sn = user_sn + 1
    if (ans[10]== 'a'):  user_sn = user_sn + 1
    if (ans[11]== 'a'):  user_tf = user_tf + 1
    if (ans[12]== 'a'): user_tf = user_tf + 1
    if (ans[13]== 'a'): user_jp = user_jp + 1
    if (ans[14]== 'a'): user_jp = user_jp + 1
    if (ans[15]== 'a'): user_ie = user_ie + 1
    if (ans[16]== 'a'): user_sn = user_sn + 1
    if (ans[17]== 'a'):  user_sn = user_sn + 1
    if (ans[18]== 'a'):  user_tf = user_tf + 1
    if (ans[19]== 'a'): user_tf = user_tf + 1
    if (ans[20]== 'a'): user_jp = user_jp + 1
    if (ans[21]== 'a'): user_jp = user_jp + 1
    if (ans[22]== 'a'): user_ie = user_ie + 1
    if (ans[23]== 'a'): user_sn = user_sn + 1
    if (ans[24]== 'a'):  user_sn = user_sn + 1
    if (ans[25]== 'a'):  user_tf = user_tf + 1
    if (ans[26]== 'a'): user_tf = user_tf + 1
    if (ans[27]== 'a'): user_jp = user_jp + 1
    if (ans[28]== 'a'): user_jp = user_jp + 1
    if (ans[29]== 'a'): user_ie = user_ie + 1
    if (ans[30]== 'a'): user_sn = user_sn + 1
    if (ans[31]== 'a'):  user_sn = user_sn + 1
    if (ans[32]== 'a'):  user_tf = user_tf + 1
    if (ans[33]== 'a'): user_tf = user_tf + 1
    if (ans[34]== 'a'): user_jp = user_jp + 1
    if (ans[35]== 'a'): user_jp = user_jp + 1
    if (ans[36]== 'a'): user_ie = user_ie + 1
    if (ans[37]== 'a'): user_sn = user_sn + 1
    if (ans[38]== 'a'):  user_sn = user_sn + 1
    if (ans[39]== 'a'):  user_tf = user_tf + 1
    if (ans[40]== 'a'): user_tf = user_tf + 1
    if (ans[41]== 'a'): user_jp = user_jp + 1
    if (ans[42]== 'a'): user_jp = user_jp + 1
    if (ans[43]== 'a'): user_ie = user_ie + 1
    if (ans[44]== 'a'): user_sn = user_sn + 1
    if (ans[45]== 'a'):  user_sn = user_sn + 1
    if (ans[46]== 'a'):  user_tf = user_tf + 1
    if (ans[47]== 'a'): user_tf = user_tf + 1
    if (ans[48]== 'a'): user_jp = user_jp + 1
    if (ans[49]== 'a'): user_jp = user_jp + 1
    if (ans[50]== 'a'): user_ie = user_ie + 1
    if (ans[51]== 'a'): user_sn = user_sn + 1
    if (ans[52]== 'a'):  user_sn = user_sn + 1
    if (ans[53]== 'a'):  user_tf = user_tf + 1
    if (ans[54]== 'a'): user_tf = user_tf + 1
    if (ans[55]== 'a'): user_jp = user_jp + 1
    if (ans[56]== 'a'): user_jp = user_jp + 1
    if (ans[57]== 'a'): user_ie = user_ie + 1
    if (ans[58]== 'a'): user_sn = user_sn + 1
    if (ans[59]== 'a'):  user_sn = user_sn + 1
    if (ans[60]== 'a'):  user_tf = user_tf + 1
    if (ans[61]== 'a'): user_tf = user_tf + 1
    if (ans[62]== 'a'): user_jp = user_jp + 1
    if (ans[63]== 'a'): user_jp = user_jp + 1
    if (ans[64]== 'a'): user_ie = user_ie + 1
    if (ans[65]== 'a'): user_sn = user_sn + 1
    if (ans[66]== 'a'):  user_sn = user_sn + 1
    if (ans[67]== 'a'):  user_tf = user_tf + 1
    if (ans[68]== 'a'): user_tf = user_tf + 1
    if (ans[69]== 'a'): user_jp = user_jp + 1
    if (ans[70]== 'a'): user_jp = user_jp + 1

    if (user_ie > 5): user_i = 'E'
    else:user_i = 'I'
    if (user_sn > 10): user_n = 'S'
    else: user_n = 'N'
    if (user_tf > 10): user_f = 'T'
    else: user_f = 'F'
    if (user_jp > 10): user_p = 'J'
    else: user_p = 'P'

    user_nnnn = user_i+user_n+user_f+user_p;

    print(user_nnnn)

    result=user_nnnn
    return result


